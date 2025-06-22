def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
def count(f):
    def counted(n):
        counted.call_count +=1
        return f(n)
    counted.call_count =0
    return counted