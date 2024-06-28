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

# #Step 1 

# import random

# word_list = ["aardvark", "baboon", "camel"]


# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']




# lives = 6


# chosen_word = random.choice(word_list)

# print(chosen_word)

# display = []

# idx = 0

# end_of_game = False


# for letter in chosen_word:
#     display.append("_")

# while not end_of_game:

#     user_guess = input("Guess a letter: ").lower()

#     for letter in chosen_word:
#         if user_guess == letter:
#             print("Right")
#         else:
#             print("Wrong") 
    
#     #using enumerate
#     for index, letter in enumerate(chosen_word): 
#             if letter == user_guess:
#                 display[index] = letter
                
#         #remember that in the list basics. To assign a value to a certain part of a list you can do it in this way
#         #example_list = ["A", "C", "E"]
#         #example_list[0] = "B"
#         #print(example_list) -> ["B", "C", "E"]

#             else:
#                  lives -= 1
#                  if lives == 0:
#                       print("You lose")
#                       end_of_game = True
    

#     print(display)

#     if "_" not in display:
#          end_of_game = True
#          print("You win")




# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' 
# # has no more blanks ("_"). Then you can tell the user they've won.


#Day 8 - Caesar Cipher (main exercise)


#Paint calculator

# import math

# test_h = int(input("What is the height of the wall? "))

# test_w = int(input("What is the width of the wall? "))

# coverage = 5

# def paint_calc(height = test_h, width = test_w, cover = coverage):
#     number_cans = math.ceil((height * width) / cover)
#     # number_cans = round(number_cans, 2)
#     return number_cans

# print(paint_calc(test_h, test_w, coverage))


#Exercise 2
#Primal number checker 

# n = int(input("Enter a number "))

# def prime_checker(number):
  
#   if number <= 1:
#     print(f"{number} is not a Prime number")
#     return False 
#   elif number == 2:
#     print(f"{number} is a Prime Number") 
#     return True
#   elif number > 2 and number % 2 != 0:
#     print(f"{number} is prime")
#     return True
#   elif number % 2 == 0:
#     print(f"{number}, any even number greater than 2 is also not prime. ")
#     return False


# prime_checker(n)



#Caesar Cipher

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(the_text=text, the_shift=shift):
    
#     encrypted = []
#     encrypted_message = []
#     for letter in the_text:
#        encrypted.append(alphabets.index(letter) + the_shift)
    
#     for numbers in encrypted:
#         encrypted_message.append(alphabets[numbers])

#     return "".join(encrypted_message) 


# secret_message = encrypt(text,shift)

# #issue happens with the letter z. 

# #I just ended up copying the entire list of the alphabet and adding it back to the end so it circles around. Angela did the same thing 

# #Did the whole thing by myself

# #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# #Done

# #part 2 decrypt


# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(the_text = secret_message, the_shift = shift):
#     decoded_index = []
#     decoded = []
#     for letters in the_text:
#         decoded_index.append(alphabets.index(letters) - the_shift)
#     for numbers in decoded_index:
#         decoded.append(alphabets[numbers])

#     return "".join(decoded)






#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"



# def caesar_cipher():
#     if direction == "encode":
#         return encrypt()
#     else:
#         return decrypt()
    
# print(caesar_cipher())

# #Did all by myself




#Day 9

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])

# programming_dictionary["Bug"] = 'Random change'
# print(programming_dictionary["Bug"])



#Create Grading Program - dictionaries


# student_scores = {"Harry": 81,
#                   "Ron": 78,
#                   "Hermione": 99,
#                   "Draco": 74,
#                   "Neville": 62,                  
#                   }

# student_grades = {}


# for student, score in student_scores.items():
#   if score in range(91, 101):
#     student_grades[student] = "Outstanding"
#   elif score in range(81, 91):
#     student_grades[student] = "Exceeds Expectations"
#   elif score in range(71, 81):
#     student_grades[student] = "Acceptable"
#   elif score in range(0, 71):
#     student_grades[student] = "Fail"


# print(student_grades)

#Did all by myself

#Travel Log 


# country = input("Add a country name ") # Add country name
# visits = int(input("How many times have you visited? ")) # Number of visits
# list_of_cities = list(input("List the cities you visited ").lower().split(",")) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 

# # print(travel_log[0]["country"])

# # travel_log.append({"country": "Pakistan", "Visits": 12, "cities": ["Karachi", "Lahore", "Murree"] })

# # print(travel_log)

# # def add_new_country(a_country=country, the_visits=visits, city_list=list_of_cities):
    
# #   travel_log.append({"country": a_country, "visits": the_visits, "cities": city_list})
# #   #print(travel_log)
# #   return travel_log

# # # Do not change the code below 👇
# # add_new_country(country, visits, list_of_cities)
# # print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# # print(f"My favourite city was {travel_log[2]['cities'][0]}.")



#Silent auction

# from replit import clear
#HINT: You can call clear() to clear the output in the console.

name = input("What is your name? ")
bid = int(input("How much do you want to bid? "))
more_bidders = input("Any more bidders? Say yes or no ").lower()

def silent_auction(the_name=name, the_bid=bid, additional_bidders=more_bidders):
    auction = []
    record_of_bid = {the_name:the_bid}
    auction.append(record_of_bid)
    print(auction)
    while additional_bidders == "yes":
        # auction.append(record_of_bid)
        # print(auction)
        #have to find a position to insert clear()

        the_name = input("What is your name? ")
        the_bid = int(input("How much do you want to bid? "))
        record_of_bid = {the_name:the_bid}
        auction.append(record_of_bid)
        additional_bidders = input("Any more bidders? Say yes or no ").lower()
         
    
    return auction
    

print(silent_auction())
