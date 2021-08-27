import random

# Magic 8-ball, based on CA assignment, no user input

name = "Tim"

question = "Will I work in the coding industry some day?"

answer = ""

random_number = random.randint(1,9)

# print(random_number)

if random_number == 1:
  answer = "Yes, definately."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error, please enter number between 1 and 9"

print(name + " asks: " + question)

print("Magic 8-Ball's answer: " + answer)
