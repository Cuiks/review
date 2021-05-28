# -*- coding: utf-8 -*-
import struct

# 八个字节
bin_str = b'ABCD1234'
print(bin_str)

# '>'表示大端序。8个B表示格式化为8个整数
result = struct.unpack(">BBBBBBBB", bin_str)
print(result)

# H把相邻的两个字节看为一个整数
# bin(65) = 0b1000001
# bin(66) = 0b1000010
# int('0100000101000010', 2) = 16706
result = struct.unpack('>HHHH', bin_str)
print(result)

# L长度为4，把相邻4个字符看做一个整数
result = struct.unpack('>LL', bin_str)
print(result)

result = struct.unpack('>8s', bin_str)
print(result)

result = struct.unpack('>BBHL', bin_str)
print(result)
