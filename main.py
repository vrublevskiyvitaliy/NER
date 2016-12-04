from en_data_provider import get_eng_test_data, get_eng_train_data
from ner import train
from tester import test


def run():
    train_file = 'trained_models/english.crfsuite'
    train_data_percent = 0.25
    blocks = int(1 / train_data_percent)
    total_f1 = 0
    for i in range(blocks):
        train_d = get_eng_train_data(train_data_percent, i)
        test_d = get_eng_test_data(train_data_percent, i)
        train(train_d, train_file)
        f1 = test(test_d, train_file)
        total_f1 += f1
        print(f1)
    total_f1 /= blocks
    print("Final F1 = " + str(total_f1))

run()



