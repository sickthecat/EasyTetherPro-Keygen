#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys

def calculate_registration_key(imei):
    x = -1
    key = 0

    for i in range(10):
        if x < 4:
            x = x + 1
        else:
            x = len(imei) + i - 10
        n = ord(imei[x]) & 0xFF
        key += (((49635 * n & 0xFFFF) >> 1) - n & 0xFFFF) & 0xFFFF

    return 0xFFFF & key

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <imei>".format(sys.argv[0]))
        print("Written by _SiCk - https://afflicted.sh\n")
        sys.exit(1)

    imei = sys.argv[1]
    registration_key = calculate_registration_key(imei)
    print("Your registration key: %05d" % registration_key)

if __name__ == "__main__":
    main()
