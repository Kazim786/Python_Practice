#Day1 Brand name project

#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end


# print("Welcome to the brand name generator. \n")

# city = input("What city did you grow up in? \n")

# pet = input("What is the name of your pet? \n")

# brand_name = city + " " + pet
# print(brand_name)


#Day 2 Random Password Generator

#Password Generator Project


# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# #I added this bit of code not Angela. 
# random.shuffle(letters)
# random.shuffle(numbers)
# random.shuffle(symbols)



# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


# random_letters = []
# random_symbols = []
# random_numbers = []
# #concatenate values from above 3 to the PW list by using + 
# pw = []

# # random.shuffle(letters)

# # print(letters)

# for i in range(nr_letters):
#     random_letters.append(letters.pop())


# for i in range(nr_symbols):
#     random_symbols.append(symbols.pop())


# for i in range(nr_numbers):
#     random_numbers.append(numbers.pop())

# pw += random_numbers + random_letters + random_symbols

# random.shuffle(pw)

# pw_str = str(pw)

# print(str(pw_str))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#I did the hard version. 
#The whole thing I did by myself 



#Day 7 hangman game 

#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




lives = 6


chosen_word = random.choice(word_list)

print(chosen_word)

display = []

idx = 0

end_of_game = False


for letter in chosen_word:
    display.append("_")

while not end_of_game:

    user_guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if user_guess == letter:
            print("Right")
        else:
            print("Wrong") 
    
    #using enumerate
    for index, letter in enumerate(chosen_word): 
            if letter == user_guess:
                display[index] = letter
                
        #remember that in the list basics. To assign a value to a certain part of a list you can do it in this way
        #example_list = ["A", "C", "E"]
        #example_list[0] = "B"
        #print(example_list) -> ["B", "C", "E"]

            else:
                 lives -= 1
                 if lives == 0:
                      print("You lose")
                      end_of_game = True
    

    print(display)

    if "_" not in display:
         end_of_game = True
         print("You win")




#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' 
# has no more blanks ("_"). Then you can tell the user they've won.
