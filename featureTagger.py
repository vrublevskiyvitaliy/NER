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


def add_lower_feature(words):
    res = []
    if words['pre']:
        res.append('-1:word.lower=' + words['pre'].lower())
    res.append('word.lower=' + words['current'].lower())
    if words['next']:
        res.append('+1:word.lower=' + words['next'].lower())

    return res


def add_isupper_feature(words):
    res = []
    if words['pre']:
        res.append('-1:word.isupper=%s' % words['pre'].isupper())
    res.append('word.isupper=%s' % words['current'].isupper())
    if words['next']:
        res.append('+1:word.isupper=%s' % words['next'].isupper())

    return res


def add_pos_tag_feature(pos_tags):
    res = []
    if pos_tags['pre']:
        res.append('pos_tag=' + pos_tags['pre'])
    res.append('-1:pos_tag=' + pos_tags['current'])
    if pos_tags['next']:
        res.append('+1:pos_tag=' + pos_tags['next'])

    return res


def add_pos_tag_2_feature(pos_tags):
    res = []
    if pos_tags['pre']:
        res.append('pos_tag[:2]=' + pos_tags['pre'][:2])
    res.append('-1:pos_tag[:2]=' + pos_tags['current'][:2])
    if pos_tags['next']:
        res.append('+1:pos_tag[:2]=' + pos_tags['next'][:2])

    return res


def word2features(sent, i, feature_config):
    word = sent[i][0]
    features = [
        'bias',
        'word=%s' % word,
        ##'word.isalnum=%s' % word.isalnum(),##
        ##'word.isalpha=%s' % word.isalpha(),##
        ##'word.islower=%s' % word.islower(),##
        ##'word.isspace=%s' % word.isspace(),##
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        #'word.issrsra=%s' % isSrSra(word),
    ]
    words = get_three_words(sent, i)
    pos_tags = get_three_pos_tags(sent, i)

    if feature_config[0]:
        features.extend(add_len_feature(words))
    if feature_config[1]:
        features.extend(add_lower_feature(words))
    if feature_config[2]:
        features.extend(add_isupper_feature(words))
    if feature_config[3]:
        features.extend(add_pos_tag_feature(pos_tags))
    if feature_config[4]:
        features.extend(add_pos_tag_2_feature(pos_tags))

    if i > 0:
        word1 = sent[i-1][0]
        features.extend([
            '-1:word=%s' % word1,
            ##'-1:word.isalnum=%s' % word.isalnum(),
            ##'-1:word.isalpha=%s' % word.isalpha(),
            ##'-1:word.islower=%s' % word.islower(),
            ##'-1:word.isspace=%s' % word.isspace(),
            '-1:word.istitle=%s' % word1.istitle(),
            #'-1:word.issrsra=%s' % isSrSra(word1),
        ])
    else:
        features.append('BOS')

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        features.extend([
            '+1:word.istitle=%s' % word1.istitle(),
        ])
    else:
        features.append('EOS')

    features = sorted(features)
    return features
