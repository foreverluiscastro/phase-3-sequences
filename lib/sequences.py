#!/usr/bin/env python3

import ipdb

def print_fibonacci(length):
    pass
    if length == 0:
        return []
    else:
        sequenced_list = []
        for n in range(length):
            if n == 0 or n == 1:
                sequenced_list.append(n)
                print(n)
            else:
                next_squence = sequenced_list[n-2] + sequenced_list[n-1]
                sequenced_list.append(next_squence)
                print(next_squence)