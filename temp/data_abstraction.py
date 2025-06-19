


def multiply_rational(x,y):
    return (numer(x)*numer(y),denom(x)*denom(y))


def print_rational(x):
    print(numer(x),'/',denom(x))




def rational(n,d):
    def selector(name):
        if name=='n':
            return n
        elif name=='d':
            return d

    return selector

def numer(x):
    return x('n')

def denom(x):
    return x('d')