# coding: GBK
import jieba


# �����һЩ������Ҫ�ϲ�������Ӹ��˴ʵ�
jieba.load_userdict('D://userdict.txt')
# ����ͣ�ô��б�
import io
def creadstoplist(stopwordspath):
    stwlist = [line.strip()
               for line in io.open(stopwordspath, 'r', encoding='utf-8').readlines()]
    return stwlist


# �Ծ��ӽ��зִ�
def seg_sentence(sentence):
    wordList = jieba.cut(sentence.strip())
    stwlist = creadstoplist('D://stopwords.txt')  # �������ͣ�ôʵ�·��
    outstr = ''
    for word in wordList:
        if word not in stwlist:
            if len(word) > 1:  # ȥ������С��1�Ĵ�
                if word != '\t':
                    outstr += word
                    outstr += " "
    return outstr

infile = io.open('D://Document.txt', 'r', encoding='GBK')  # ��ҪGBK���ܶ�ȡ����Ҳ����Ϊʲô
outfile = io.open('D://LDA.txt', 'w', encoding='UTF-8')
for line in infile:
    line_seg = seg_sentence(line)  # ����ķ���ֵ���ַ���
    s = unicode(line_seg)    # ��strת��ΪUnicode
    outfile.write(s + '\n')
outfile.close()
infile.close()
