"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

import os
import argparse
import nltk
from nltk.corpus import stopwords

stop_words = stopwords.words('russian') + stopwords.words('english')
# print(stop_words)

parser = argparse.ArgumentParser(description="Top 100 words")
parser.add_argument("filename")
args = parser.parse_args()

if not os.path.exists(args.filename):
    print('Файла не существует!')
    exit()

our_file = open(args.filename)
text = our_file.read()
words = nltk.word_tokenize(text)

words = [word for word in words
        if len(word) > 2
        and not word.isnumeric()
        and word not in stop_words]

print('Топ-100 слов в файле:')
freq_dist = nltk.FreqDist(words)
for word, frequency in freq_dist.most_common(100):
    print(word,' : ',frequency)

#print(words)