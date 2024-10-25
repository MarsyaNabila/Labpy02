#!/usr/bin/python3

a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if a + b == c or b + c == a or c + a == b:
    print("BENAR")
else:
    print("SALAH")