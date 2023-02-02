#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func_1(type_1='max'):
    def func_2(b):
        if type_1 == 'max':
            return max(b)
        else:
            return min(b)

    return func_2


if __name__ == "__main__":
    test_list = [1, 2, 3, 5, 0, -13, 100]
    test_tuple = [1.5, 2, 123, 5, 0, -167, 100]

    print(f'Max of entered list: {func_1()(test_list)}')
    print(f'Min of entered tuple: {func_1("min")(test_tuple)}')