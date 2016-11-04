# -*- coding: utf-8 -*-
# @Date    : 2016-11-03 15:22:41
# @Author  : fancy (fancy@thecover.cn)

import time
import hashlib

# 今日头条接口加密算法
def main():
    i = int((time.time() * 1000) / 1e3)
    t = hex(i).replace('0x', '').upper()
    e = hashlib.md5(str(i)).hexdigest().upper()
    if len(t) != 8:
        return {
            'as': '479BB4B7254C150',
            'cp': '7E0AC8874BB0985'
        }
    def get_o():
        o = ''; s = e[:5]
        for i in range(5):
            o += s[i] + t[i]
        return o
    def get_c():
        c = '';  a = e[-5:]
        for i in range(5):
            c += t[i + 3] + a[i]
        return c
    o = get_o()
    c = get_c()
    return {
        'as': 'A1%s%s' % (o, t[-3:]),
        'cp': '%s%sE1' % (t[:3], c),
    }

if __name__ == '__main__':
    print main()
