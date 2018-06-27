birthdays = {'Albert Einstein': '03/14/1879', 'Benjamin Franklin': '01/17/1706', 'Ada Lovelace': '12/10/1815'}
 
print ('Welcome to the birthday dictionary.')
print ('We know the birthdays of: Albert Einstein Benjamin Franklin Ada Lovelace')
print ("Who's birthday do you want to look up?")

query = input()
print (birthdays[query])
