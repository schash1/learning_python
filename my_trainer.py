from random import choice

d = {}
with open("Types_and_operators.txt", encoding='utf-8') as f:
    for line in f:
        (key, val) = line.split('/')
        d[key] = val

i = len(d)
print('x - element, l - list, i - index, func - function, w - word, sym - symbol, t - tuple(tab), s - set')

while i > 0:
    explanation, method = choice(list(d.items()))
    print(explanation)
    my_method = input('Enter a method: ')
    print(method)
    del d[explanation]
    i -= 1
    print('')
