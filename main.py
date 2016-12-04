from en_data_provider import get_eng_test_data, get_eng_train_data
from ner import train
from tester import test


def run():
    train_file = 'trained_models/english.crfsuite'
    for i in range(4):
        train_d = get_eng_train_data(i)
        test_d = get_eng_test_data(i)
        train(train_d, train_file)
        print(test(test_d, train_file))

run()



