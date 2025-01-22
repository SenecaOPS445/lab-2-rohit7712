#!/usr/bin/env python3

#Author:  - Rohit
#Author ID: 145339222
#Date Created: 2025/01/22

import sys

if len(sys.argv) != 2:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')

