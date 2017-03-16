# coding=utf-8
import codecs


def get_log():
    file = codecs.open("logs/NAME_L.txt", "r", "utf_8_sig")
    return file


def get_f1():
    file = get_log()
    i = 0
    for line in file:
        if i % 6 == 0:
            pieces = line.split(' ')
            try:
                number = float(pieces[2])
            except ValueError as e:
                continue
            except IndexError as e:
                continue
            print '%.2f' % round(number, 2)
        i += 1


def get_pre():
    file = get_log()
    i = 0
    for line in file:
        if i % 6 == 1:
            pieces = line.split(' ')
            try:
                number = float(pieces[2])
            except ValueError as e:
                continue
            except IndexError as e:
                continue
            print '%.2f' % round(number, 2)
        i += 1


def get_recall():
    file = get_log()
    i = 0
    for line in file:
        if i % 6 == 2:
            pieces = line.split(' ')
            try:
                number = float(pieces[2])
            except ValueError as e:
                continue
            except IndexError as e:
                continue
            print '%.2f' % round(number, 2)
        i += 1

#get_f1()
#get_pre()
get_recall()