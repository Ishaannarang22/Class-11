str1 = input('enter a string: ')
count = 0
work = str1.casefold().split()
for i in work:
    if i[0] in 'aeiou':
        count += 1
print(count)
