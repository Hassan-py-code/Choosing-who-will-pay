

import random
print('Welcom to wallet?')
print('You will give me a list of names and I will pick a person to pay')
name_string=input("If you're ready, enter the names seprated by a comma:")

ran=name_string.split(",")

choice_list=random.choice(ran)

print(f"Please aske {choice_list} to take his wallet out.Dinner is on him")




