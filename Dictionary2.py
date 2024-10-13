"""sentance=input("Enter a sentance ?")

vowels={"a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0}
for letter in sentance:
    if letter in vowels:
        vowels[letter]+=1

print (vowels)"""

sentance = "the quick brown fox jumped over the lazy dog"

import string 
b={}
for i in string.ascii_lowercase:
 b[i]=0

print(b)   
for letter in sentance:
 if letter in b:
  b[letter]+=1

print(b)
switch = True
for i in b.values():
 if i == 0 :
  switch=False

if switch == True:
 print("this is a panagram")
else:
 print("this is not a panagram")
