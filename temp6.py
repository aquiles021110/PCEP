d1={'Adam.S':'A','Judy.P':'B+'}
d2={'Mary.L':'A','Patrick.W':'C'}
d3={}
for i in (d1,d2):
    d3.update(i)
print(d3)

A={'Tamil':92,'English':56,'Maths':88,'Science':97,'Social Studies':89}
B={'Tamil':78,'English':68,'Maths':88,'Science':97,'Social Studies':56}
print('Matching pairs are:')
for i in A:
    if i in B and A[i] == B[i]:
        print(i,A[i])