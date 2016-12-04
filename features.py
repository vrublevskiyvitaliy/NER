# coding=utf-8

months = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"]
srs = ["señora", "señor", "sr", "sra","sr.","sra."]


def is_month(text):
    lower_case_text = text.lower()
    return is_in_array(lower_case_text, months)


def is_sr_sra(text):
    lower_case_text = text.lower()
    return is_in_array(lower_case_text, srs)


def is_in_array(text, array):
    try:
        array.index(text)
    except ValueError:
        return False
    return True