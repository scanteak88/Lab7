def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)

n = eval(input("請輸入 Fibonacci number:  "))
for i in range(n+1):
    print("n = {}, fib({}) = {}".format(i, i, fib(i)))