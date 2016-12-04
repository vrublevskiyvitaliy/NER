# coding=utf-8
import codecs

MAX_USED_DATA = 1000
TRAIN_DATA_PERCENT = 0.25
eng_text = []


def get_words_from_sentence(sentence):
    blocks = sentence.split(' ')
    correct_format = []
    for block in blocks:
        parts = block.split('|')
        b = (parts[0], parts[1], parts[2])
        correct_format.append(b)
    return correct_format


def get_all_text():
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


def get_eng_train_data(block=0):
    text = get_all_text()
    global TRAIN_DATA_PERCENT
    size = len(text)
    size = int(TRAIN_DATA_PERCENT * size)
    f = block * size
    return text[f:f+size]


def get_eng_test_data(exclude=0):
    text = get_all_text()
    global TRAIN_DATA_PERCENT
    size = len(text)
    size = int(TRAIN_DATA_PERCENT * size)
    begin = text[:exclude * size]
    end = text[(exclude + 1) * size + 1:]
    return begin + end