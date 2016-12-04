# coding=utf-8
from __future__ import print_function
import pycrfsuite
import featureTagger

from en_data_provider import get_eng_train_data

#train_sents = get_eng_train_data()

def sent2features(sent):
    return [featureTagger.word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, pos_tag, label in sent]


def sent2tokens(sent):
    return [token for token, pos_tag, label in sent]


def train(train_sent, name_of_file):
    x_train = [sent2features(s) for s in train_sent]
    y_train = [sent2labels(s) for s in train_sent]

    trainer = pycrfsuite.Trainer(verbose=False)

    for x_seq, y_seq in zip(x_train, y_train):
        trainer.append(x_seq, y_seq)

    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier

        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.params()

    #trainer.train('english.crfsuite')
    trainer.train(name_of_file)
