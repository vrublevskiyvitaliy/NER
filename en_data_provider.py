# coding=utf-8
import codecs
import nltk

MAX_USED_DATA = 1000
eng_text = []
MODE_PURE_TYPES = 'PURE_TYPES'
MODE_BINARY = 'BINARY'
MODE_B_NAME = 'B, NAME'
MODE = None


def get_words_from_sentence(sentence):
    blocks = sentence.split(' ')
    correct_format = []
    for block in blocks:
        parts = block.split('|')
        b = (parts[0], parts[1], parts[2])
        correct_format.append(b)
    return correct_format


def get_all_text():
    t_1 = list(nltk.corpus.conll2002.iob_sents('esp.train'))
    t_2 = list(nltk.corpus.conll2002.iob_sents('esp.testa'))
    t_3 = list(nltk.corpus.conll2002.iob_sents('esp.testb'))
    return t_1 + t_2 + t_3


'''def get_all_text():
    global eng_text, MAX_USED_DATA
    if len(eng_text):
        return eng_text
    else:
        file = codecs.open("data/aij-wikiner-en-wp2.txt", "r", "utf_8_sig")
        i = 0
        for line in file:
            line = line.strip()
            if line != '':
                i += 1
                eng_text.append(get_words_from_sentence(line))
                if i == MAX_USED_DATA:
                    break
        file.close()
    return eng_text
'''


def get_eng_train_data(train_data_percent, block=0):
    # text = get_all_text()
    # size = len(text)
    # size = int(train_data_percent * size)
    # f = block * size
    # data = text[f:f+size]
    data = list(nltk.corpus.conll2002.iob_sents('esp.train'))
    if MODE == MODE_PURE_TYPES:
        data = process_data_mode_pure_types(data)
    if MODE == MODE_BINARY:
        data = process_data_mode_binary(data)
    if MODE == MODE_B_NAME:
        data = process_data_mode_b_name(data)
    return data


def get_eng_test_data(train_data_percent, exclude):
    # text = get_all_text()
    # size = len(text)
    # size = int(train_data_percent * size)
    # begin = text[:exclude * size]
    # end = text[(exclude + 1) * size + 1:]
    # data = begin + end
    data = list(nltk.corpus.conll2002.iob_sents('esp.testa'))
    if MODE == MODE_PURE_TYPES:
        data = process_data_mode_pure_types(data)
    if MODE == MODE_BINARY:
        data = process_data_mode_binary(data)
    if MODE == MODE_B_NAME:
        data = process_data_mode_b_name(data)
    return data


def process_data_mode_pure_types(data):
    correct_data = []
    for s in data:
        correct_s = []
        for word in s:
            t = word[2]
            if len(t) > 1:
                t = t[2:]
            correct_s.append((word[0], word[1], t))
        correct_data.append(correct_s)
    return correct_data


def process_data_mode_binary(data):
    correct_data = []
    for s in data:
        correct_s = []
        for word in s:
            t = word[2]
            if len(t) > 1:
                t = 'NAME'
            correct_s.append((word[0], word[1], t))
        correct_data.append(correct_s)
    return correct_data


def process_data_mode_b_name(data):
    correct_data = []
    for s in data:
        correct_s = []
        for word in s:
            t = word[2]
            if len(t) > 1:
                if t[0] == 'B':
                    t = 'B-NAME'
                else:
                    t = 'NAME'
            correct_s.append((word[0], word[1], t))
        correct_data.append(correct_s)
    return correct_data


