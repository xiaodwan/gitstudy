class CP(set):
    def __init__(self, values):
        l1 = []
        if values and isinstance(values, str):
            for i in values.split(','):
                l1.append(i.strip())
        print(l1)
        set.__init__(self, l1)
    def __contains__(self, item):
        if isinstance(item, set):
            return item <= self
        return set.__contains__(self, item)

c2 = CP("1,2,3")
c1 = CP([1,2])
print(1 in c1)
print(3 in c1)
print(set([1,2]) in c1)

