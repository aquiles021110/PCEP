'''odd=0
even=0
while True:
    val=int(input('Enter number:    '))
    if val%2==0:
        even+=1
    elif val==0:
        break
    else:
        odd+=1
    print(f'Odd numbers:{odd}\nEven numbers:{even}')'''

vowels='aeiou'
text=''
word=input('Enter word/phrase:  ').lower()
i=0
while i<len(word):
    if word[i] not in vowels:
        text+=word[i]
    i+=1
print(text)