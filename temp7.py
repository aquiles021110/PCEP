my_dict = {'Name':'Tara','RollNo':130046,'Mark':458,'Age':16}
print(my_dict)
my_dict.pop('Mark')
my_dict.pop('RollNo')
my_dict.update({'Mark10':458})
my_dict.update({'RegNo':130046})
print(my_dict)
###sort
dict={'hey':12,'bye':4,'cya':100,'tkt':321}
list=[]
for i in dict.keys():
    list.append(dict[i])
list.sort()
#list.reverse()
print(list)