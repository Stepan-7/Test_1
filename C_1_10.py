fruits = ['apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append ('orange')
print("Updated fruits list;",fruits)


launguage = ['French','English']
launguage1 = ['Spanish','Portuguese']
launguage.extend(launguage1)
print('LaunguageList:',launguage)


fruits = ['apple', 'pear', 'banana', 'kiwi',]
fruits.insert(2,'orange') 
print(fruits)


fruits = ['apple','pear']
fruits1 = ['kiwi','apple']
fruits.append('banana')
fruits.extend(fruits1)
fruits.insert(2,'orange')
print(fruits)