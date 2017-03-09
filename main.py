from en_data_provider import get_eng_test_data, get_eng_train_data
from ner import train
from tester import test


def get_feature_configuration(n, max):
    config = [0] * max
    g = 0
    while n > 0:
        a = n % 2
        n = int(n/2)
        config[g] = a
        g += 1
    return config


def run():
    train_file = 'trained_models/english.crfsuite'
    train_data_percent = 1
    blocks = int(1 / train_data_percent)
    max_c = 6
    all_config = 2**max_c
    best_f1 = 0
    best_config = 0
    for c in range(all_config):
        #c = 2**max_c - 1
        config = get_feature_configuration(c, max_c)
        total_f1 = 0
        for i in range(blocks):
            train_d = get_eng_train_data(train_data_percent, i)
            test_d = get_eng_test_data(train_data_percent, i)
            train(train_d, train_file, config)
            f1 = test(test_d, train_file, config)
            total_f1 += f1
            print(f1)
        total_f1 /= blocks
        print("Config = " + str(config))
        print("Final F1 = " + str(total_f1))
        if total_f1 > best_f1:
            best_f1 = total_f1
            best_config = config
        #break
    print("Best config = " + str(best_config))
    print("Best F1 = " + str(best_f1))


def d_location():
    train_d = get_eng_train_data(0.25, 0)
    s = set()
    for sent in train_d:
        for i in range(len(sent)):
            if sent[i][2] == 'I-LOC':
                if i > 0 and sent[i-1][2] != 'I-LOC':
                    s.add(sent[i-1][0].lower())
                    #print(sent[i-1])
    print(s)
    y = 0


run()



