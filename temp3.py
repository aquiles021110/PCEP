age=int(input('Enter Age\n'))
condition=int(input('Input your condition(1,Stable;2,Serious;3,Critical)\n'))
prio=('High' if condition==3 and (age<12 or age>=65) else
'Low' if (age>=18 and age<65) and condition==1 else
'Med' if (age>=12 and age<=64) else 'Error')
print(f"This patient's priority is {prio}")

#tax
dedu=0
dedu1=0
dedu2=0
finalres=0
totaltax=0
income=int(input('Enter annual income\n'))
hins=input('Have you paid your health insurance?(Y/N)\n')
cdo=input('Have you made any charitable donations?(Y/N)\n')
if hins=='Y':
    dedu+=0.05
if cdo=='Y':
    dedu+=0.1
finalres=income*(1-dedu)
tax=(
0 if finalres<10_000 else 
0.1*(finalres-10_000) if income<50_000 else 
0.1*(40_000)+0.2*(finalres-50_000))
print(f'Taxable income: {finalres}\nTax to be paid: {tax}')