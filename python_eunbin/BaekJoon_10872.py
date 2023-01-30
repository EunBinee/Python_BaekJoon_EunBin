# -*- coding: utf-8 -*-5
# 백준 10872번 팩토리얼 문제 - 단계별 풀어보기: 재귀

def Factorial(num):
    if num <= 1:
        return 1
    else:
        return num * Factorial(num-1)


num = int(input())
print(Factorial(num))
