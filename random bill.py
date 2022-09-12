import random
print ("Welcome to the bill payment selector")
names_string = input("Give me every body's name , Spearated by comma. ")
names = names_string.split(",")
alpha = random.randint(0,len(names)-1)
print(names_string[alpha])
 



