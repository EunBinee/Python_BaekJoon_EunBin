# -*- coding: utf-8 -*-5
# ���� 10870�� �Ǻ���ġ �� ���� - �ܰ躰 Ǯ���: ���

def Fibonacci(num):
    if num == 0:
        return 0
    elif num <= 1:
        return 1
    return Fibonacci(num-1)+Fibonacci(num-2)


num = int(input())
print(Fibonacci(num))
