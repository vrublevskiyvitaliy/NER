# coding=utf-8
import codecs

TRAIN_DATA_PERCENT = 0.1
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
    global eng_text
    if len(eng_text):
        return eng_text
    else:
        file = codecs.open("data/aij-wikiner-en-wp2.txt", "r", "utf_8_sig")
        #file = codecs.open("data/1.txt", "r", "utf_8_sig")
        i = 0
        for line in file:
            line = line.strip()
            if line != '':
                i += 1
                eng_text.append(get_words_from_sentence(line))
                if i == 50000:
                    break
        file.close()
    return eng_text


def get_eng_train_data():
    text = get_all_text()
    global TRAIN_DATA_PERCENT
    size = len(text)
    size = int(TRAIN_DATA_PERCENT * size)
    return text[:size]


def get_eng_test_data():
    text = get_all_text()
    global TRAIN_DATA_PERCENT
    size = len(text)
    size = int(TRAIN_DATA_PERCENT * size)
    return text[size + 1:]