n = int(input('number of elements: '))
dic = {}
for i in range(n):
	a = input('roll number: ')
	b = input('name: ')
	dic[a] = b
key = dic.keys()
for z in key:
	print(z, '\t', dic[z])