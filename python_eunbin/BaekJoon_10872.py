# -*- coding: utf-8 -*-5
# ���� 10872�� ���丮�� ���� - �ܰ躰 Ǯ���: ���

def Factorial(num):
    if num <= 1:
        return 1
    else:
        return num * Factorial(num-1)


num = int(input())
print(Factorial(num))
