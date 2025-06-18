
sign='@'
text=''
word=input('Enter email:  ').lower()
i=0
while i<len(word):
    if word[i] not in sign:
        text+=word[i]
    else:
        break
    i+=1
print(text)