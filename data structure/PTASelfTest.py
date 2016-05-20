# -*- coding: utf-8 -*-
# PTASelfTest.py
# https://pta.patest.cn/pta/test/17/exam/4

import math


# 1. 打印沙漏
def shalou(num, mark):
    n = int(math.sqrt((num+1)/2)) - 1
    for i in range(n, -1, -1):
        print(' '*(n-i)+mark*(2*i+1))
    for i in range(1, n+1):
        print(' '*(n-i)+mark*(2*i+1))
    print(num-(n+1)**2*2+1)


# 2. 素数对猜想1
def sushudui1(num):
    # get prime list
    s = [x for x in range(3, num+1, 2) if x % 6 == 1 or x % 6 == 5]
    n = num**0.5
    for i, v in enumerate(s):
        if v <= n:
            s = s[:i+1]+[x for x in s[i+1:] if x % v != 0 and x != v]
        else:
            break
    s = [3]+s
    for i in range(0, len(s)-1):
        s[i] = s[i+1]-s[i]
    print(s.count(2))


# 2. 素数对猜想2
def primes(n):
    '''
    To Get Prime List

    code from www.iplaypython.com
    modified to omit 2
    '''
    # if n < 2:    return []
    # if n == 2: return [2]
    s = [x for x in range(3, n, 2)]
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)//2
            # print('i = %d\t m = %d\tj = %d' % (i,m,j))
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
            # print(s)
            # print('+++++++++')
        i = i + 1
        m = 2 * i + 3
    # return [2]+[x for x in s if x]
    return [x for x in s if x]


def sushudui2(num):        # really fast!
    # get prime list
    s = primes(num+1)
    for i in range(0, len(s)-1):
        s[i] = s[i+1]-s[i]
    print(s.count(2))


# 3. 数组右移
def shiftright(n, m, s):
    m = m % n
    if m == 0:
        return s
    for i in range(-m, 0):
        s.insert(0, s.pop())
    return s


# 4. Have Fun with Numbers
def DoubleNum(num):
    s = sorted(str(num))
    n = num*2
    if num >= (10**(len(s)))//2:
        return 'No', n
    d = sorted(str(n))
    for i in range(len(s)):
        if s[i] != d[i]:
            return 'No', n
    return 'Yes', n


# 5. Shuffling Machine
def shuffle(deck, n, order):
    for i in range(n):
        deck = [x[1] for x in sorted(list(zip(order, deck)))]
    return deck


def main():
    print("Please select a function to test:\n--------------")
    print("1. Shalou\n2. SuShuDui\n3. ShiftRight\n4. DoubleNum\n5. Shuffle")
    print("--------------")
    f = input("Your choice(1-5,0 to quit): ")
    if f == '0':
        return
    if f == '1':
        s = input().split(' ')
        shalou(int(s[0]), s[1])
    elif f == '2':
        sushudui2(100000)
    elif f == '3':
        l1 = ['10', '3']
        l2 = ['1', '3', '5', '7', '9', '11', '14', '16', '20', '22']
        l1 = input().split(' ')
        l2 = input().split(' ')
        print(' '.join(shiftright(int(l1[0]), int(l1[1]), l2)))
    elif f == '4':
        s = eval(input())
        s = 123456789
        d = DoubleNum(s)
        print(d[0])
        print(d[1])
    elif f == '5':
        a = ('S', 'H', 'C', 'D')
        deck = [i+str(j) for i in a for j in range(1, 14)] + ['J1', 'J2']
        n = int(input())
        order = [int(x) for x in input().split(' ')]
        print(' '.join(shuffle(deck, n, order)))
    else:
        return

if __name__ == '__main__':
    main()
