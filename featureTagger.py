# coding=utf-8
from features import is_month
from features import is_sr_sra


def sent2features(sent, feature_config):
    return [word2features(sent, i, feature_config) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, pos_tag, label in sent]


def sent2tokens(sent):
    return [token for token, pos_tag, label in sent]

def word2features(sent, i, feature_config):
    word = sent[i][0]
    pos_tag = sent[i][1]
    features = [
        'bias',
        'word=%s' % word,
        ##'word.isalnum=%s' % word.isalnum(),##
        ##'word.isalpha=%s' % word.isalpha(),##
        ##'word.islower=%s' % word.islower(),##
        ##'word.isspace=%s' % word.isspace(),##
        ##'word.len=%s' % len(word), ##,
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        #'word.issrsra=%s' % isSrSra(word),
        'pos_tag=' + pos_tag,
        'pos_tag[:2]=' + pos_tag[:2],
    ]
    if feature_config[0]:
        features.append('word.len=%s' % len(word))

    if i > 0:
        word1 = sent[i-1][0]
        pos_tag1 = sent[i-1][1]
        features.extend([
            '-1:word=%s' % word1,
            ##'-1:word.isalnum=%s' % word.isalnum(),
            ##'-1:word.isalpha=%s' % word.isalpha(),
            ##'-1:word.islower=%s' % word.islower(),
            ##'-1:word.isspace=%s' % word.isspace(),
            '-1:word.len=%s' % len(word1),
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            #'-1:word.issrsra=%s' % isSrSra(word1),
            '-1:pos_tag=' + pos_tag1,
            '-1:pos_tag[:2]=' + pos_tag1[:2],
        ])
        ##if (word1 == "en") and (word.istitle()):
        ##    features.extend([
        ##        'word=True'
        ##    ])
    else:
        features.append('BOS')

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        pos_tag1 = sent[i+1][1]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:pos_tag=' + pos_tag1,
            '+1:pos_tag[:2]=' + pos_tag1[:2],
        ])
    else:
        features.append('EOS')

    return features
