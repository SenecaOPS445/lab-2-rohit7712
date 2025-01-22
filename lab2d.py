#!/usr/bin/env python3

import sys

error = sys.argv[0]

if len(sys.argv) != 3:
    print('Usage: ' + error + ' name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + age + ' years old.')

