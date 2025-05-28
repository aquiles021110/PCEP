'''v = 1E-3
print(v)
v=v*2
print(v)

print("Hello \t World")'''


'''if a>b:
    print(a,'+',b,f'= {a+b}')
elif a<b:
    print(a,'-',b,f'= {a-b}')
elif a==b:
    print(a,'X',b,f'= {a*b}')'''

a=int(input('Choose number 1\n'))
b=int(input('Choose number 2\n'))
num=a if a < b else b
#or
'''res=a | b'''
#and
'''res=a & b'''
#negation
'''res=~a'''
#left shift
'''res=a << 2'''
#right shift
'''res=a >>2'''
print(res)
