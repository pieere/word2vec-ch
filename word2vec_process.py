import re
import codecs
import jieba


def get_stopwords():
    with open('chineseStopWords.txt', 'r', encoding='gb2312') as f:
        a = f.readlines()
        stopwords = [w.strip() for w in a]
        return stopwords


stopwords = get_stopwords()


def filte(input_file):
    p1 = re.compile('（）')
    p2 = re.compile('《》')
    p3 = re.compile('「')
    p4 = re.compile('」')
    p5 = re.compile('<doc (.*)>')
    p6 = re.compile('</doc>')
    outfile = codecs.open('wiki.zh.txt', 'a+', 'utf-8')
    with codecs.open(input_file, 'r', 'utf-8') as myfile:
        for line in myfile:
            line = p1.sub('', line)
            line = p2.sub('', line)
            line = p3.sub('', line)
            line = p4.sub('', line)
            line = p5.sub('', line)
            line = p6.sub('', line)
            outfile.write(line)
    outfile.close()

'''使用命令行 opencc -i wiki.zh.txt -o wiki.zh.simp.txt -c t2s.json 将繁体中文转换为简体中文'''
def cut_and_clean():
    with open('/Users/wangzifeng/PycharmProject/word2vec/extracted/wiki.zh.simp.txt', 'r') as f:
        words = f.readlines()

        words = list(jieba.cut(str(words)))
        # clean words whos length<2 and with only numbers and characters
        words = [w for w in words if len(w) > 1 and not re.match('^[a-z|A-Z|0-9|.]*$', w)]

        # clean stop_words
        words = [w for w in words if w not in stopwords]
        return words


def run():
    data_path = '/Users/wangzifeng/PycharmProject/word2vec/extracted/AA/'
    data_names = ['wiki_00', 'wiki_01']
    for data_name in data_names:
        filte(data_path + data_name)
        print('{0} has been processed !'.format(data_name))
    result = cut_and_clean()
    return result


if __name__ == '__main__':
    result = run()
    with open('wiki_result.csv', 'w') as f:
        f.write(' '.join(result))


