#!/usr/bin/env python
# (c) 2016 John Strickler
#
import pyparsing as pp

samples = [
    'IP ADDRESS 234.9.15.8',
    '1.2.3.4.5.6',
    '1.2.C.5',
    '    2.3.4,5',
    '    2.3..5',
    '   542.32.93.93  ',
    'Stuff stuff 82.93.116.5 stuff stuff',
    'Stuff stuff 82.288.116.5 stuff stuff',
    'a.b.c.d',
    'IP ADDRESS 192.168.1.1',
    'This is not an IP address',
]

def main():
    ip_address = build_parser()
    for sample in samples:
        parse_result = ip_address.searchString(sample)
        print(sample, '-->', end=' ')
        if parse_result and all(0 <= i <= 255 for i in parse_result[0]):
            octets = parse_result[0]
            ip = '{}.{}.{}.{}'.format(*octets)

            print(parse_result[0], ip)
        else:
            print('INVALID')


def convert_octet_to_int(result_list):
    return int(result_list[0])


def build_parser():
    dot = pp.Suppress('.')  # match '.' and discard it

    octet = pp.Word(pp.nums)  # an octet is made of 1 or more digits

    octet.setParseAction(convert_octet_to_int)  # pass octet to this function

    ip_address = (octet + ((dot + octet) * 3))
    # ip_address = (octet + dot + octet + dot + octet + dot + octet)
    return ip_address


if __name__ == '__main__':
    main()
