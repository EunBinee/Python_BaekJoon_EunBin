# -*- coding: utf-8 -*-5
# 백준 25501번 재귀의 귀재  문제 - 단계별 풀어보기: 재귀
import sys


def Recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return Recursion(s, l+1, r-1)


def IsPalindrome(s):
    count = 0
    return Recursion(s, 0, len(s)-1)


loopNum = int(sys.stdin.readline())  # 한개의 정수를 받겠다는 뜻.
# sys의 사용이유 : 시간 초과를 예방하기 위함.

s = ""
str = ""
count = 0


for i in range(loopNum):
    s = sys.stdin.readline().rstrip()
    count = 0
    print(IsPalindrome(s), count)
