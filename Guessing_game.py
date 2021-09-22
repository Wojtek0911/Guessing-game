import random

candies_number = random.randint(1,100)

answer_limit = 3
answers = 0 

while answers <= answer_limit:
	guess = int(input("Guess how many candies are in the jar: "))
	print(guess)
	if guess == candies_number:
		print("You are correct!")
		break
	elif  guess < candies_number:
		print("Sorry, that's not correct. Your number is lower than the answer.")
		answers += 1
	elif guess > candies_number:
		print("Sorry, that's not correct. Your number is higher than the answer.'")
		answers +=1
	else:
		print("No, that's not right.'")
		continue
print(f"The correct answer was {candies_number}")
