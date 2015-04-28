# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
    print(__name__)

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def main():
    #main function when fibo run independently 
    
    #import sys
    #fib(int(sys.argv[1]))
    print('Fibo is main')
    import collections
    queue = collections.deque([1,2,3])
    print(queue.popleft())


if __name__ == "__main__":
    main()


    
