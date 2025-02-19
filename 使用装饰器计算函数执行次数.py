#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def count_calls(func):
    n=0
    def inner():
        nonlocal n
        n = n+1
        print(f"函数{func.__name__}目前被调用了{n}次")
        return func()
    return inner
@count_calls
def fun1():
    print("111111")
def main():
    fun1()
    fun1()

if __name__ == '__main__':
    main()
