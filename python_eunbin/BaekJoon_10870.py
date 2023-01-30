# -*- coding: utf-8 -*-5
# 백준 10870번 피보나치 수 문제 - 단계별 풀어보기: 재귀

def Fibonacci(num):
    if num == 0:
        return 0
    elif num <= 1:
        return 1
    return Fibonacci(num-1)+Fibonacci(num-2)


num = int(input())
print(Fibonacci(num))
