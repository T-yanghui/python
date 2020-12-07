import logging
from gensim.models import word2vec

def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence("D:\\Code\\python\\基于SGNS的汉语词向量学习和评估\\train.txt")
    # size：单词向量的维度
    # window: 窗口大小
    # sg=1: 使用skip-gram
    # hs=0: 使用negative sample
    model = word2vec.Word2Vec(sentences, size=100, window=5, sg=1, hs=0, negative=5)
    # 保存模型  必须3个一起用
    # model.save("./model/wiki_corpus.bin")
    # model.save("./model/wiki_corpus.model")

    # 训练为一个单独二进制压缩文件  可独立使用
    model.wv.save_word2vec_format("D:\\Code\\python\\基于SGNS的汉语词向量学习和评估\\model_binary.bin", binary=True)

if __name__ == "__main__":
    main()