#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 学习使用按位与&
# 程序分析: 0 & 0 = 0;
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

if __name__ == '__main__':
    a = 0o77
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b= %d' % b)
