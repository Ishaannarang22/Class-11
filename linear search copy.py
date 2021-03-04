def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False
list = [1, 2, 'qwerty', 4, 'abs', 6]

n = 'qwerty'

if search(list, n):
    print("successful")
else:
    print("unsuccessful")