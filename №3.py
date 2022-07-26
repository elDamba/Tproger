import operator
a = {6: 4, 7: 2, 3: 0, 2: 1, 9: 3, 10: 5}
b = dict(sorted(a.items(), key=operator.itemgetter(1)))
c = dict(sorted(a.items(), key=operator.itemgetter(1), reverse=True))
print(b, c, sep='\n')
