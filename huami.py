#!/usr/bin/env python2
# coding=utf8
# Huami CLI Version.
# Author: cynic (ninehills.github.com)
# Usage: huami.py PASSWORD KEY
import sys
import hmac

STR1 = "snow"
STR2 = "kise"
STR3 = "sunlovesnow1990090127xykab"

def huami(password, key):
    """计算花密密码
    """
    # 得到md5one, md5two, md5three
    # hmac.new(key, msg)
    md5one = hmac.new(key, password).hexdigest()
    md5two = hmac.new(STR1, md5one).hexdigest()
    md5three = hmac.new(STR2, md5one).hexdigest()
    # 转换大小写
    rule = list(md5three)
    source = list(md5two)
    for i in range(1, 31):
        if rule[i] in STR3:
            source[i] = source[i].upper();
    #code32 = ''.join(source)
    #保证密码首字母为字母---why?
    if source[0].isdigit():
        code16 = "K" + "".join(source[1:16])
    else:
        code16 = "".join(source[0:16])
    return code16

if __name__ == "__main__":
    if len(sys.argv) != 3:
        help_str =  "Usage: %s PASSWORD KEY\n" %(sys.argv[0])
        sys.stderr.write(help_str)
        sys.exit(1)
    print huami(sys.argv[1], sys.argv[2])