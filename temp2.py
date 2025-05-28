'''
inp=int(input('Put ONE number\n'))
eve=True if inp%2==0 else False
pos=True if inp>0 else False
eve='That is an even number' if eve==True else 'That is an odd number'
pos='That is a positive number' if pos==True else 'That is a negative number'
print(eve,pos,sep='\n')
'''
age=int(input('Enter age of traveller\n'))
dist=int(input('Enter distance of trip in mi\n'))
less=True if dist<1000 else False
price=200 if age<12 else 250
price=300 if age>65 and age<12 else 250
price+=200 if less==False else 0
print(f'The price is {price}')
