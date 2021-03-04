print('Hi Ishaan here, this calculator is the best lmao')
#numbers and variables
n = int(input())
m = int(input())

#defining functions
def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def divion(a,b):
    return a/b

#what to do?
operation = str(input())

#convert what to do in strings of code
operations = {
    'addition':'addition(n, m)', 
    'subtraction':'subtraction(n, m)', 
    'multiplication':'multiplication(n, m)', 
    'division':'divion(n,m)'
}

#do it while converting string of code into real code lmao using eval()
#here 'operation' is a key that will call the appropriate function as a string from the dictionary
print(eval(operations[operation]))
print('I won lmao')



n = int(input())
m = int(input())
def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def divion(a,b):
    return a/b
operation = str(input())
operations = {
    'addition':'addition(n, m)', 
    'subtraction':'subtraction(n, m)', 
    'multiplication':'multiplication(n, m)', 
    'division':'divion(n,m)'
}
print(eval(operations[operation]))
