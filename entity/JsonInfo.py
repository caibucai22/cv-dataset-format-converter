# -*- coding: UTF-8 -*-
"""
@File    ：JsonInfo.py
@Author  ：Csy
@Date    ：2023-07-26 22:40 
@Bref    :
"""


def parseKeyValue():
    keys = []
    values = []

    return keys, values


def parseValues(values):
    if len(values) > 0 and isinstance(values[0], tuple):
        pass
    else:
        print("len of values equals 0, or value is not a tuple")
