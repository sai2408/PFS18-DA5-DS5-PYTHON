#Yield
'''
def abc(n):
    for i in range(n):
        yield i**2
res = abc(3)
print(res)
for i in res:
    print(i)
'''
#next
'''
def abc(n):
    for i in range(n):
        yield i**2
res = abc(3)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
'''

