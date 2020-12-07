import re
import numpy as np
from gensim.models import KeyedVectors


def compute_dist():
    global max,min
    # 读取待计算数据
    model = KeyedVectors.load_word2vec_format("./model_binary.bin", binary=True)
    f = open('./pku_sim_test.txt', encoding='utf-8')
    out = open('./distance.txt', 'w', encoding='utf-8')
    
    # 字符串切分为列表
    wordlist = []
    while True:
        line = f.readline()
        if not line:
            break
        wordlist.append(re.split(r'[\t\n]', line))
    
    # 计算欧式距离并存储
    cnt = 0
    for i in range(len(wordlist)):
        words = wordlist[i]
        try:
            vi = model[words[0]]
            vj = model[words[1]]
            vec1 = np.array(vi)
            vec2 = np.array(vj)
            dist = np.linalg.norm(vec1-vec2)
        except KeyError:
            words[2] = "OOV"
            wordlist[i] = words
            # print(words)
            continue

        words[2] = str("%.1f"%dist)
        wordlist[i] = words
        #print(words)
        cnt += 1
        if dist > max :
            max = dist
        if dist < min :
            min = dist
    print("查到的比例为：%.1f"%(cnt/len(wordlist)))
    print('max:{0}  min:{1}'.format(max,min))
    
    # 结果保存
    lines = []
    for i in range(len(wordlist)):
        line = wordlist[i]
        oneline = line[0] + '\t' + line[1] + '\t' + line[2] + '\t\n'
        lines.append(oneline)
    out.writelines(lines)
    f.close()
    out.close()

def compute_sim():
    global max,min
    # 读取待计算数据
    f = open('./distance.txt', encoding='utf-8')
    out = open('./result_sim.txt', 'w', encoding='utf-8')
    # 字符串切分为列表
    wordlist = []
    while True:
        line = f.readline()
        if not line:
            break
        wordlist.append(re.split(r'[\t]', line))
    print(wordlist)
    # 计算sim(wi,wj)= (10*max-min -9*dij) / (max-min)
    dij = 0.0
    cnt = 0
    for i in range(len(wordlist)):
        words = wordlist[i]
        if words[2] != "OOV":
            dij = float(words[2])
            sim = (10*max-min -9*dij) / (max-min)
            words[2] = str("%.1f"%sim)
            # print('dij = {0} max = {3} min = {4} sim = {1} words[2] = {2}'.format(dij,sim,words[2],max,min))
            print(words)
            cnt += 1
        else:
            words[2] = "1"
        wordlist[i] = words
    print("查到的比例为：%.1f"%(cnt/len(wordlist)))
    
    # 结果保存
    lines = []
    for i in range(len(wordlist)):
        line = wordlist[i]
        oneline = line[0] + '\t' + line[1] + '\t' + line[2] + '\n'
        lines.append(oneline)
    out.writelines(lines)
    f.close()
    out.close()
    

if __name__ == '__main__':
    max = 0.0
    min = 100.0
    compute_dist()
    compute_sim()