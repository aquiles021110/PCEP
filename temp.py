'''v = 1E-3
print(v)
v=v*2
print(v)

print("Hello \t World")'''

a=int(input('Choose number 1\n'))
b=int(input('Choose number 2\n'))
if a>b:
    print(a,'+',b,f'= {a+b}')
elif a<b:
    print(a,'-',b,f'= {a-b}')
elif a==b:
    print(a,'X',b,f'= {a*b}')
