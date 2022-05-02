import random 


numbers = ['0','1','2','3','4','5','6','7','8','9']
special_char = ['!','@','#','£','%','&','+','*','$']
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number_n = int(input("How many number you want in your password? "))

special_char_n = int(input("How many special char you want in your password? "))

letter_n = int(input("How many letter you want in your password? "))

OurPass = []

for char in range(1,number_n+1):
	OurPass += random.choice(numbers)
	
for char in range(1,special_char_n+1):
	OurPass += random.choice(special_char)
	
for char in range(1,letter_n+1):
	OurPass += random.choice(letter)
	
random.shuffle(OurPass)
password = ""

for char in OurPass:
	password +=char

print(f"Your generated Password is {password}")