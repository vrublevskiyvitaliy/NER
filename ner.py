# coding=utf-8
from __future__ import print_function
import pycrfsuite
from featureTagger import *


def train(train_sent, name_of_file, feature_config):
    x_train = [sent2features(s, feature_config) for s in train_sent]
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
    trainer.train(name_of_file)
