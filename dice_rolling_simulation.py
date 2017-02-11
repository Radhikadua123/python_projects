import random

def main():
	sides=6
	roll=True
	counts=[0]*6
	while roll:
		roll_again = raw_input("DO YOU WANT TO ROLL ? Q=Quit ENTER=Roll")
		if roll_again=="q":
			roll = False
		else:
			num=random.randint(1,sides)
			print("YOU ROLLED ",num)
			counts[num-1]+=1
	print("Thanks for playing!!!!")
	i=0
	while i < 6:
		print("Number of times ",i+1,"appeared is",counts[i])
		i+=1

main()


