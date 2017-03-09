# coding=utf-8
from __future__ import print_function
from itertools import chain
from sklearn.metrics import classification_report, precision_recall_fscore_support
from sklearn.preprocessing import LabelBinarizer
import pycrfsuite
from featureTagger import *
import numpy as np


def get_correct_f1(y_true, y_predicted, labels):
    p, r, f1, s = precision_recall_fscore_support(
        y_true,
        y_predicted,
        labels=labels,
        average=None,
        sample_weight=None
    )
    f1 = np.average(f1, weights=s)
    return f1


def bio_classification_report(y_true, y_predicted):
    lb = LabelBinarizer()
    y_true_combined = lb.fit_transform(list(chain.from_iterable(y_true)))
    y_predicted_combined = lb.transform(list(chain.from_iterable(y_predicted)))

    tag_set = set(lb.classes_) - {'O'}
    tag_set = sorted(tag_set, key=lambda tag: tag.split('-', 1)[::-1])
    class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}
    labels = [class_indices[cls] for cls in tag_set]

    f1 = get_correct_f1(y_true_combined, y_predicted_combined, labels)
    report = classification_report(
        y_true_combined,
        y_predicted_combined,
        labels=labels,
        target_names=tag_set,
    )
    print(report)

    return f1


def test(test_data, train_file, feature_config):
    x_test = [sent2features(s, feature_config) for s in test_data]
    y_test = [sent2labels(s) for s in test_data]

    tagger = pycrfsuite.Tagger()
    tagger.open(train_file)

    y_predicted = [tagger.tag(x_seq) for x_seq in x_test]

    f1 = bio_classification_report(y_test, y_predicted)

    return f1

'''
from collections import Counter
info = tagger.info()


def print_transitions(trans_features):
    for (label_from, label_to), weight in trans_features:
        print("%-6s -> %-7s %0.6f" % (label_from, label_to, weight))

print("Top likely transitions:")
print_transitions(Counter(info.transitions).most_common(5))

print("\nTop unlikely transitions:")
print_transitions(Counter(info.transitions).most_common()[-5:])


def print_state_features(state_features):
    for (attr, label), weight in state_features:
        print("%0.6f %-6s %s" % (weight, label, attr))

print("Top positive:")
print_state_features(Counter(info.state_features).most_common(20))

print("\nTop negative:")
print_state_features(Counter(info.state_features).most_common()[-20:])
'''