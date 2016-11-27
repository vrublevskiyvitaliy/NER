# coding=utf-8
from __future__ import print_function
import nltk
import pycrfsuite
from subprocess import call
import featureTagger

##print test data files
# print(nltk.corpus.conll2002.fileids())
train_sents = list(nltk.corpus.conll2002.iob_sents('esp.train'))


def sent2features(sent):
    return [featureTagger.word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, postag, label in sent]


def sent2tokens(sent):
    return [token for token, postag, label in sent]


X_train = [sent2features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]


# To train the model, we create pycrfsuite.Trainer,
# load the training data and call 'train' method.
# First, create pycrfsuite.Trainer and load the training data to CRFsuite:
trainer = pycrfsuite.Trainer(verbose=False)

for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 50,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
})

trainer.params()

trainer.train('conll2002-esp.crfsuite')

call('ls -lh ./conll2002-esp.crfsuite', shell=True)

print("File conll2002-esp.crfsuite created")
