# coding: GBK
import jieba


# 如果有一些词语需要合并可以添加个人词典
jieba.load_userdict('D://userdict.txt')
# 创建停用词列表
import io
def creadstoplist(stopwordspath):
    stwlist = [line.strip()
               for line in io.open(stopwordspath, 'r', encoding='utf-8').readlines()]
    return stwlist


# 对句子进行分词
def seg_sentence(sentence):
    wordList = jieba.cut(sentence.strip())
    stwlist = creadstoplist('D://stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in wordList:
        if word not in stwlist:
            if len(word) > 1:  # 去掉长度小于1的词
                if word != '\t':
                    outstr += word
                    outstr += " "
    return outstr

infile = io.open('D://Document.txt', 'r', encoding='GBK')  # 非要GBK才能读取，我也不懂为什么
outfile = io.open('D://LDA.txt', 'w', encoding='UTF-8')
for line in infile:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    s = unicode(line_seg)    # 把str转换为Unicode
    outfile.write(s + '\n')
outfile.close()
infile.close()
