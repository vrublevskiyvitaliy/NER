from en_data_provider import get_eng_test_data, get_eng_train_data
from ner import train
from tester import test


def run():
    train_file = 'trained_models/english.crfsuite'
    train_d = get_eng_train_data()
    test_d = get_eng_test_data()
    train(train_d, train_file)
    print(test(test_d, train_file))



run()



