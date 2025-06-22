class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    "如果没有自己写__repr__ 和__str__ 输出都只会是 类名加地址"
    def __repr__(self):
        if self.rest:
            rest_repr = ',' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr +')' 

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string +=str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def ordered(s,key=lambda x:x):
    """
    >>> ordered(Link(1,Link(3,Link(4))))
    True
    >>> ordered(Link(1,Link(4,Link(3))))
    False
    >>> ordered(Link(1,Link(-3,Link(4))))
    False
    >>> ordered(Link(1,Link(-3,Link(4))),key=abs)
    True
    >>> ordered(Link(1,Link(4,Link(3))),key=abs)
    False

    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)


def merge(s,t):
    """ 将s和t从大到小排
    >>> a=Link(1,Link(5))
    >>> b=Link(1,Link(4))
    >>> merge(a,b)
    Link(1,Link(1,Link(4,Link(5))))
    >>> a
    Link(1,Link(5))
    >>> b
    Link(1,Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first,merge(s.rest,t))
    else:
        return Link(t.first,merge(s,t.rest))








