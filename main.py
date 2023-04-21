from random import choice

d = {}
with open("List.txt", encoding='utf-8') as f:
    for line in f:
        (key, val) = line.split('/')
        d[key] = val

i = len(d)
print('List is a collection which is ordered and changeable. Allows duplicate members.')
print('x - element, l - list, i - index, func - function')

while i > 0:
    explanation, method = choice(list(d.items()))
    print(explanation)
    my_method = input('Enter a method: ')
    print(method)
    del d[explanation]
    i -= 1
    print('')
