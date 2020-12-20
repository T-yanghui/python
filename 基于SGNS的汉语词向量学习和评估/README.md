# 基于SGNS的汉语词向量学习和评估作业

## 一、概述

1.训练语料来源：train.txt（小规模已切分数据）

2.用word2vec训练词向量，并用所学得的词向量，计算 pku_sim_test.txt 文件 中每行两个词间的相似度

3.词相似度结果文本result_sim.txt
$$
词间相似度计算公式:
sim(wi,wj)= (10*max-min -9*dij) / (max-min)
其中:
	dij为两词之间的欧氏距离;
	max和min为所有同行两个词间dij的最大值和最小值
$$

## 二、数据准备及预处理

1.word2vec模型的训练

当前目录下的train.py中word2vec的参数设置(size=100, window=5, sg=1, hs=0, negative=5)，符合实验要求(前后2窗口，100维，SGNS)。

其中：size：单词向量的维度；window: 窗口大小；sg=1: 使用skip-gram；hs=0: 使用negative sample

```python
#训练源码：train.py
import logging
from gensim.models import word2vec

def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence("D:\\Code\\python\\基于SGNS的汉语词向量学习和评估\\train.txt")
    
    model = word2vec.Word2Vec(sentences, size=100, window=5, sg=1, hs=0, negative=5)
    # 保存模型 
   
    # 训练为一个单独二进制压缩文件  可独立使用
    model.wv.save_word2vec_format("D:\\Code\\python\\基于SGNS的汉语词向量学习和评估\\model_binary.bin", binary=True)

if __name__ == "__main__":
    main()
```

2.计算两个词的相似度
（1）读取训练得到的模型，以及待计算相似的pku_sim_test.txt文件
（2）字符串以\t\n为分隔符切分为列表格式，并计算欧式距离，保存结果distance.txt(未获得词向量的一行欧氏距离标记为OOV)
（3）读取distance.txt,计算词间相似度，某行中存在任一个词没有获得词向量时，对应的该行的词间相似度为1，保存结果result_sim.txt,同行词间以\t分隔

```python
#compute_similarity.py
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

#计算词间相似度    
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
```

