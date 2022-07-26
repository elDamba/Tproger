import operator
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
a = sorted(my_dict.items(), key=operator.itemgetter(1))
print(a[-3:])
