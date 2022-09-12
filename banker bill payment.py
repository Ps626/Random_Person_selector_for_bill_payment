import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size = len(names)
 
the_person = random.randint(0, size - 1)

lucky_person = names[the_person]


print(lucky_person + "IS GOINI TO PAY THE BILL.") 