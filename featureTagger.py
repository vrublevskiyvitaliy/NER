# coding=utf-8
from features import is_month
from features import is_sr_sra


def sent2features(sent, feature_config):
    return [word2features(sent, i, feature_config) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, pos_tag, label in sent]


def sent2tokens(sent):
    return [token for token, pos_tag, label in sent]


def get_three_words(sent, i):
    word = sent[i][0]
    if i > 0:
        pre_word = sent[i - 1][0]
    else:
        pre_word = None
    if i < len(sent)-1:
        next_word = sent[i + 1][0]
    else:
        next_word = None
    d = dict()
    d['pre'] = pre_word
    d['current'] = word
    d['next'] = next_word

    return d


def get_three_pos_tags(sent, i):
    pos = sent[i][1]
    if i > 0:
        pre_pos = sent[i - 1][1]
    else:
        pre_pos = None
    if i < len(sent)-1:
        next_pos = sent[i + 1][1]
    else:
        next_pos = None
    d = dict()
    d['pre'] = pre_pos
    d['current'] = pos
    d['next'] = next_pos

    return d


def add_len_feature(words):
    res = []
    if words['pre']:
        res.append('-1:word.len=%s' % len(words['pre']))
    res.append('word.len=%s' % len(words['current']))
    if words['next']:
        res.append('+1:word.len=%s' % len(words['next']))

    return res


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
        ##'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        #'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        #'word.issrsra=%s' % isSrSra(word),
        'pos_tag=' + pos_tag,
        'pos_tag[:2]=' + pos_tag[:2],
    ]
    words = get_three_words(sent, i)
    if feature_config[0]:
        features.extend(add_len_feature(words))
    if feature_config[1]:
        features.append('word.lower=' + word.lower())
    if feature_config[2]:
        features.append('word.isupper=%s' % word.isupper())

    if i > 0:
        word1 = sent[i-1][0]
        pos_tag1 = sent[i-1][1]
        features.extend([
            '-1:word=%s' % word1,
            ##'-1:word.isalnum=%s' % word.isalnum(),
            ##'-1:word.isalpha=%s' % word.isalpha(),
            ##'-1:word.islower=%s' % word.islower(),
            ##'-1:word.isspace=%s' % word.isspace(),
            #'-1:word.len=%s' % len(word1),
            #'-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            #'-1:word.isupper=%s' % word1.isupper(),
            #'-1:word.issrsra=%s' % isSrSra(word1),
            '-1:pos_tag=' + pos_tag1,
            '-1:pos_tag[:2]=' + pos_tag1[:2],
        ])
        if feature_config[1]:
            features.append('-1:word.lower=' + word.lower())
        if feature_config[2]:
            features.append('-1:word.isupper=%s' % word.isupper())
    else:
        features.append('BOS')

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        pos_tag1 = sent[i+1][1]
        features.extend([
            #'+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            #'+1:word.isupper=%s' % word1.isupper(),
            '+1:pos_tag=' + pos_tag1,
            '+1:pos_tag[:2]=' + pos_tag1[:2],
        ])
        if feature_config[1]:
            features.append('+1:word.lower=' + word1.lower())
        if feature_config[2]:
            features.append('+1:word.isupper=%s' % word1.isupper())
    else:
        features.append('EOS')

    return features
