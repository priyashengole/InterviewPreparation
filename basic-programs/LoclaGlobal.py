#Program 1

'''f = 100
print(str(f) +'Local')

def fun():
    f = 'Python'
    print(str(f) +'Global')


fun()
print(str(f) +'Local')'''

#Program 2

f = 100
print(f)

def fun():
    global f
    print(f)
    f = 'Python'

fun()
print(f)
