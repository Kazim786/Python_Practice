# # # # mood = 'happy'

# # # # if mood == 'happy':
# # # #     print("Im happy you are happy")
# # # #     print(':)' * 10)

# # # # else:

# # # #     print("Hope you feel better")

# # # # unit = input("What unit are you using? ")
# # # # temp = int(input("What temperature is the water? "))

# # # # if unit == "f":
# # # #     if temp >= 60 and temp <= 77:
# # # #         print("Its nice and cool")
# # # #     else:
# # # #         print("Temperature isnt nice")

# # # # else:
# # # #     print("I dont know celcius")


# # # height = float(input("Please enter your height in inches "))
# # # weight = float(input("Please enter your weight in pounds "))

# # # bmi = (weight * 703)/(height * height)

# # # bmi = round(bmi, 1)

# # # print(bmi)

# # # if bmi < 16.0:
# # #     print("Severly Underweight")
# # # elif bmi >= 16.0 and bmi <= 18.4:
# # #     print(f"Underweight your BMI is {bmi}")

# # # elif bmi >= 18.5 and bmi <= 24.9:
# # #     print(f"Normal")

# # # elif bmi >= 25.0 and bmi <= 29.9:
# # #     print("Overweight")

# # # elif bmi >= 30.0 and bmi <= 34.9:
# # #     print("Moderately Obese")

# # # elif bmi >= 35.0 and bmi <= 39.9:
# # #     print("Severely Obese")

# # # else:
# # #     print("Morbidly Obese")

# # # age = input("What is your age?")

# # # if not age.isnumeric():
# # #     input("Enter a valid number!")

# # # answer = input("Please say hi ")

# # # while answer != "hi":
# # #     answer = input("Rude, Please say hi ")

# # # print("Hi to you too")


# # #odd or even number
# # # odd_or_even = int(input("Enter your number. No decimal points "))

# # # if odd_or_even % 2 == 1:
# # #     print("Number is odd")
# # # else:
# # #     print("Number is even")

# # # num = 10

# # # while num > 0:
# # #     print(f"NUMBER IS: {num}")
# # #     num -= 1

# # # count = 7

# # # while count > 0:
# # #     print("*" * count)
# # #     count -= 1

# # # from random import randint




# # # dice_1 = randint(1, 6)

# # # dice_2 = randint(1, 6)

# # # while dice_1 != 1 or dice_2 != 1:

# # #     print(f"Dice 1 {dice_1} and Dice 2 is {dice_2}")
# # #     dice_1 = randint(1, 6)

# # #     dice_2 = randint(1, 6)

# # # print(f"Dice 1:  {dice_1} and Dice 2: is {dice_2} We got Snake Eyes finally {dice_1} {dice_2}")

# # # name = "Kazim"

# # # for x in name:
# # #     print("Hi")

# # # total = 0
# # # for ltr in "euphoria":
# # #     if ltr in "aeiou":
# # #         total += 1

# # # print(total)



# # # for x in range(1, 10):
# # #     print(x)


# # # beer_bottles = 99

# # # while beer_bottles > 0:
# # #     print(f"{beer_bottles} bottles of beer on the wall.")
# # #     print(f"{beer_bottles} bottles of beer")
# # #     beer_bottles -= 1
# # #     print(f"take one down, pass it around, {beer_bottles} bottles of beer on the wall")


# # # for x in range(99, 0, -1):
# # #     print(f"{x} bottles of beer on the wall.")
# # #     print(f"{x} bottles of beer")
# # #     if x == 1:
# # #         print("take one down, pass it around, No more bottles of beer")
# # #     else:
# # #         print(f"take one down, pass it around, {x - 1} bottles of beer on the wall")


# # # for x in range(1,5):
# # #     print(x)
# # #     for y in range(1,5):
# # #         print(y)


# # # import random

# # # # print(random.randint(1, 5))

# # # num_dice = int(input("How many dice are we rolling? "))

# # # sides = int(input("How many sides on each dice? ")) #this will have the randint()

# # # for x in range(1, num_dice + 1):
# # #     print("|" * x)
# # #     # for side in range(1, sides + 1):
# # #     #     print(random.randint(1, side)) #1, 6
# # #     for y in range(1, num_dice + 1):
# # #         print(random.randint(1, sides))



# # #TOOTHPICK EXERCISE, ITLL USE WHILE LOOP WHILE TOOTHPICK NUMBER IS > 0

# # toothpick = "|" * 13
# # print(len(toothpick))

# # print(toothpick)


# # #toothpick = toothpick.replace(toothpick[len(toothpick) - 1], "", 1) #this just replaces every occurrence of |
# # print(toothpick)
# # print(len(toothpick))
# # player_1 = input("Enter player 1's name ")
# # player_2 = input("Enter player 2's name ")
# # while len(toothpick) > 0:
# #     print(f"There are {len(toothpick)} toothpicks left" )
# #     player_1_count = int(input(f"How many do you take {player_1}? Choose 1, 2, or 3"))
# #     if player_1_count == 1 or player_1_count == 2 or player_1_count == 3:
# #         toothpick = toothpick.replace(toothpick[len(toothpick) - 1], "", player_1_count) 
# #     else:
# #         player_1_count = int(input(f"How many do you take {player_1}? You need to choose numbers 1, 2, or 3 "))   
# #     if len(toothpick) == 0:
# #         print(f"{player_1} wins!")
# #     print(f"There are {len(toothpick)} toothpicks left" )
# #     player_2_count = int(input(f"How many do you take {player_2}? Choose 1, 2, or 3"))
# #     if player_2_count == 1 or player_2_count == 2 or player_2_count == 3:
# #         toothpick = toothpick.replace(toothpick[len(toothpick) - 1], "", player_2_count)
# #     else:
# #         player_1_count = int(input(f"How many do you take {player_2}? You need to choose numbers 1, 2, or 3 ")) 

# #     if len(toothpick) == 0:
# #         print(f"{player_2} wins!")
# #     break


# # # def multiply(x):
# # #     print(f"ha" * x)

# # # multiply(10)

# # # def is_even(x):
# # #     return x % 2 == 0
        
    
# # # print(is_even(9))

# # #spaces replaced with dashes, leading/trailing spaces are removed, lowercase everything
# # # def slugify(x):
# # #     x = x.strip().replace(" ", "-").lower()
# # #     # x = x.replace(" ", "-")
# # #     # x = x.lower()
    
# # #     return x


# # # print(slugify(" KAZIM RAZA SHABBIR "))






# # # def vowel_count(word):
# # #     count = 0
# # #     index = len(word) - 1
# # #     while word[index] == "a" or "e" or "i" or "o" or "u":
# # #         count += 1
# # #         index -= 1
# # #         if index < 0:
# # #             break
# # #     return count


# # # def vowel_count(word):
# # #     #might have to use and statement
# # #     count = 0
# # #     for vowel in word:
# # #         vowel = vowel.lower()
# # #         if vowel in "aeiou":
# # #             count += 1

# # #     return count
        

# # # print(vowel_count("Prophet Muhammad (saw) I love you and peace be upon you and your family. I love your brother Mola Ali (as)"))


# # def laugh(strength=2):
# #     print("ha" * strength)
    

# #spaces replaced with dashes, leading/trailing spaces are removed, lowercase everything
# # def slugify(phrase, sep="-"):
# #     phrase = phrase.strip().replace(" ", sep).lower()
# #     phrase = phrase.replace(" ", sep)
# #     phrase = phrase.lower()
    
# #     return phrase

# # slugify(" KAZIM RAZA SHABBIR ")



# # using_return_to_our_advtg = slugify(" KAZIM RAZA SHABBIR ")
# # print(using_return_to_our_advtg)

# # names = ["Kazim", "Mohiba"]

# # print(names[1][0])

# # names[1] = "Mrs. Mohiba Kazim"

# # print(names)

# # waitlist = ["Kazim", "Raza", "Shabbir"]

# # waitlist.append("Mohiba")

# # print(waitlist)

# # nums = [1, 2, 3, 4]

# # nums[1:3] = ["a", "b", "c"]


# # print(nums[1:4])

# # nums[1:4] = [5]

# # #output will be nums = [1, 5, 4]
# # print(nums)
# # print(nums)

# # waitlist = ["Kazim", "Ali", "Hasan"]

# # last_guy = waitlist.pop()

# # print(waitlist)
# # print(last_guy)


# # new_students = ["Kazim", "Oscar", "Hamza", "Fred", "Reinhard", "John"]

# # lucky_student = new_students.pop(2)

# # print(new_students)
# # print(lucky_student)

# lang = ["Java", "SQL", "HTML", "C", "Javascript", "Python"]

# # for language in lang:
# #     print(language)
# #     if language == "Python":
# #         print("Python is the best")

# # x = 0

# # while x < len(lang):
# #     print(lang[x])
# #     x += 1


# # lando_2021_results = [4, 3, 5, 8, 10, 9, 2, 3, 4, 6, 20, 14, 29]
# # minimum = lando_2021_results[0]


# # for nums in lando_2021_results:
# #     if nums < minimum:
# #         minimum = nums
# # print(minimum)


# # total = 0

# # for nums in lando_2021_results:

# #     total += nums 
# #     average = total/len(lando_2021_results)


# # print(average)


# # def average(list):
# #     total = 0
# #     for num in list:
# #         total += num

# #     the_average = total/len(list)

# #     return the_average
    
# # print(average(lando_2021_results))


# #*************************************



# # # It's race day and our starting grid is set! Charles sits on pole and Lando brings up the rear.
# # drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]

# # # Oh dear, we've misspelled "Valtteri" as "Valterri".  Update the drivers list to include the correct spelling!

# # drivers[2] = "Valtteri"

# # # print(drivers)

# # # Esteban makes it out of the pits and joins the pack just in time.  Add "Esteban" to the end of the drivers list!

# # drivers.append("Esteban")

# # # What's this? There's another group of drivers that comes out of nowhere to join the race! Add each element from the others list to the end of the drivers list.
# # others = ["Blue", "Elton", "Colt"]

# # drivers.extend(others)
# # # print(drivers)

# # # Colt looks lost out there! He has a horrible fiery crash.  Remove the last element from the drivers list ("Colt")

# # drivers.pop()
# # # print(drivers)

# # # Oh dear, there's a huge crash at the front! Remove the first element from the driver's list

# # drivers.pop(0)
# # # print(drivers)
# # # And again the leader of the pack runs into trouble! He's not out of the race, but he's now moved to last place.  Remove the first driver in the list, store it in variable, and then add it to the end of the list.

# # leader = drivers.pop(0)

# # drivers.append(leader)

# # # print(drivers)


# # # My idiotic cat, Blue, is in the middle of the pack.  Delete "Blue" from the drivers list using the remove method!

# # drivers.remove("Blue")

# # # print(drivers)

# # # My dog, Elton, is making a remarkable charge up the leadboard! Remove Elton from his current position in the list and insert him at index 2.

# # dog = drivers.pop(5)

# # drivers.insert(2, dog)

# # # print(drivers)

# # # The race is over! It's time for the podium ceremony.  Create a new list called podium that contains the first 3 elements from the drivers list. (use a slice!)

# # podium = drivers[0:3]

# # print(podium)


# # # Loop over the drivers list and print out a leadboard that includes a driver's finishing position and their name, like this:
# # # 1. Valtteri
# # # 2. Lewis
# # # 3. Elton
# # # 4. George
# # # 5. Lando
# # # 6. Esteban
# # # 7. Pierre

# # finishing_position = 1
# # for driver in drivers:
# #     print(f"{finishing_position}. {driver}")
# #     finishing_position += 1


# # flavors = ["chocolate", "coffee", "vanilla", "strawberry"]

# # response = input("What flavor would you like? ")


# # while response.lower() not in flavors:
# #     response = input("That flavor is not available in list. Try again. ").lower()
# # print(f"{response} is available in the flavors")


# # if response in flavors:
# #     print("nice choice")
# # else:
# #     print("flavor not available")


# # nums1 = [1, 2, 3]

# # nums2 = nums1

# # print(nums2)

# # nums2.append(4)

# # print(nums2)

# # full_name = ["Kazim", "Raza", "Shabbir"]

# # print("-".join(full_name))

# race_results = ["Kazim", "John", "Edward", "Tyrone", "Umair", "Razi"]

# # gold, silver, bronze, *losers = race_results

# # print(gold)
# # print(losers)

# print(race_results.index("Kazim") + 1)

# movie = {"title": "The Message",
#           "imbd": 8.3,
#           "Director": "Mustafa Akkad"
#           }

# print(movie["title"])

# movie["imbd"] = 10

# movie["Number_1_fan"] = "Kazim"

# print(movie)

# produce = {
#     "arugala": {
#         "price": 1.10,
#         "qty": 61,
#         "organic": True,
#         "producer": "Blue Kitty Farms"
#     },
#     "coconut": {
#         "price": 7.15,
#         "qty": 12,
#         "organic": False,
#         "producer": "Tropical Dream Farm"
#     }
# }

# print(produce["coconut"]["producer"])


# test_scores = {
#     "Marsha": [78, 80, 89],
#     "Baker": [69, 65, 52]
# }


# print(test_scores["Marsha"][0])

# waitlist = [
#     {
#         "email": "tiff@gmail.com",
#         "location": 'USA',
#         "first_name": "Tiffany"
#     },
#     {
#         "email": "tiff@gmail.com",
#         "location": 'USA',
#         "first_name": "Tiffany"
#     }
# ]
# print(waitlist[0]["email"])





#********

# even = {2, 4, 6, 8}

# even.add(12)


# even.clear()
# print(even)


#*********** Tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# # total_bill = float(input("What was the total bill? "))

# # tip = float(input("How much tip would you like to pay? "))

# # tip = tip/100

# # tip = total_bill * tip 


# # split = int(input("How many people to split the bill? "))
# # if split != 0:
# #     paying = (total_bill + tip) / split
# #     paying = round(paying, 2)
# #     print(f"Each Person is Paying ${paying}")

# # else:

# #     paying = total_bill + tip
# #     paying = round(paying, 2)
# #     print(f"The total you are paying is ${paying}")


# #***** Treasure Island

# #print('''
# #*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# direction = input("Where do you want to go? Left or Right?")

# if direction == "Left" or direction == "Right":
#     if direction == "Left":
#         choice = input("You came to a lake, There is an island in the middle. Type 'wait' to wait for a boat or type  'swim' to swim accross?")
#         if choice == "wait":
#             arrival = input("You have arrived on the island. There is a house with 3 doors. Red, Green, Yellow. Which color do you choose? ")
#             if arrival == "Red":
#                 print("You burned yourself")
#             elif arrival == "Blue":
#                 print("Eaten by BEASTS. GAME OVER")
#             elif arrival == "Green":
#                 print("You win!! You found the treasure")
#             elif arrival == "Yellow":
#                 print("Game over")

                
#         else:
#             print("Attacked by Trout. GAME OVER")


#     else:
#         print("Fall into hole. GAME OVER")

# num1 = {1, 2, 3, 4, 5}

# num2 = {3, 7, 12, 8, 1}

# print(num1 & num2)


#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for image in picture:
#     for num in image:
#         if num == 0:
#             print(" ", end="")
            
#         else:
#             print("*", end="")
#     print("")


# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# total = 0
# for items in my_list:
#     total += items

# print(total)


# def checkDriverAge (age = 0):
#     #age = input("What is your age?: ")

#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")


# print(checkDriverAge(27))
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

#*************

#def highest_even(li):
    #approach 1
    # for num in li:
    #     if num % 2 == 0 and num == max(li):
    #         print(num)


#max(li) - automatically turns into 11

    
        # if max(li) % 2 == 0:
        #     print(max(li))
        # elif max(li) - 1:
        #       print(max(li) - 1)


# #approach 2
#     # the_index = 0
#     # while li[the_index] > len(li):
#     #     if li[the_index] % 2 == 0 and li[the_index] == max(li):
#     #         print(li[the_index])
#     #     the_index += 1


# #approach 3
#     #if max(li) % 2 == 0:
#         #print(max(li))





# highest_even([10, 2, 4, 3, 5, 7, 8, 11, 13, 14, 22, 15, 25, 28, 30, 33])


#********Object oriented programming

# class Puppy:
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []
# #self refers to the current instance of Puppy

# #Instatiating a puppy

# elton = Puppy("Elton")
# #Everytime we call Puppy() we're creating a new Puppy instance with its own name and tricks list.
# elton.name
# elton.tricks



# class Dog:

#     species = "canine"
#     num_dogs = 0

#     def __init__(self, name, breed, location):
#         self.name = name
#         self.breed = breed
#         self.tricks = []
#         self.location = location
#         Dog.num_dogs += 1
    

#     @classmethod
#     def register_stray(cls):
#         return cls('coming soon', 'unknown', 'unknown')
#     #This method is being used to generate an instance. cls stands for the Dog class. Hence any method used for Dog can be used for cls

#     def add_trick(self, new_trick):
#         self.tricks.append(new_trick)
    
#     def bark(self):
#         print(f"{self.name} says 'WOOOF!'")

#     def learn_trick(self, new_trick):
#         if new_trick not in self.tricks:
#             self.tricks.append(new_trick)
#         else:
#             print(f"{self.name} already knows this")

#     def perform_trick(self, trick):
#         if trick in self.tricks:
#             print(f"{self.name} can {trick}")
#         else:
#             print(f"{self.name} doesnt know this {trick}")
 

# stray1 = Dog.register_stray()

# # print(stray1.name)

# class Human:
#     def __init__(self, name):
#         self.name = name
 
#     def breathes(self):
#         print(f"{self.name} is breathing")

# class Child(Human):
#     def growing(self):
#         print(f"{self.name} is growing to become an adult")



# shayan = Child("Shayan")

# print(shayan.name)

# print(shayan.growing()) #This class exists in child class

# print(shayan.breathes()) #This class exists in main class

# print(type(shayan)) #outputs Child class





# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def meow(self):
#         print(f"{self.name} meows!!")


# class Lion(Cat):
#     def __init__(self, name, pride_name):
#         super().__init__(name)
#         self.pride_name = pride_name
#     def roar(self):
#         print(f"{self.name} ROARS")

# ali = Lion("Ali", "Bani Hashim")

# print(ali.name)

# print(ali.pride_name)


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def meow(self):
#         print(f"{self.name} meows!!")


# class Lion(Cat):
     
#     def roar(self):
#         print(f"{self.name} ROARS")

# ali = Lion("Ali")

# print(ali.name)


#***** Chat gpt exercises

# Strings:
# Anagram Check: Write a function that checks if two strings are anagrams of each other (contain the same characters in a different order).


# def anagram(str1, str2):
#     #this might need nested loops
#     #Anagram would be for example Kazim and Mizak or Silent and Listen. Since these 2 have the same letters but in different order
#     letter_box = []
#     if len(str1) == len(str2):
#         for i in str1:
#             if i in str2 and str1.count(i) == str2.count(i) :
#                 letter_box.append(i)
#         if len(letter_box) == len(str2):
#             print("This is an anagram")
#         else:
#             print("No its not an anagram")
        
# anagram("silent", "listen") 

#Did by myself and it works 



# String Compression: Write a function that performs basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3".

def compression(string):

    
    idx = 0
    compressed_str = ""
    while idx < len(string):
        string.count(string[idx])
        compressed_str += string[idx] + "" + str(string.count(string[idx]))
        idx += 1
    return compressed_str
    

print(compression("aabcccccaaa"))

# String Rotation Check: Write a function that checks if one string is a rotation of another. For example, "abcd" is a rotation of "cdab".


# txt = "Hello World" [::-1]
# print(txt)

# #outputs dlroW olleH

def rotation(string1, string2):

    if string1[::-1].lower() == string2.lower():
        print("These strings are rotations of each other")

rotation("dlroW olleh", "hello world")


#Did this by myself


# Lists:
# List Rotation: Write a function that rotates a list by a specified number of steps. For example, if you rotate [1, 2, 3, 4, 5] by 2 steps, you get [4, 5, 1, 2, 3].

# List Intersection: Write a function that takes two lists and returns a new list containing only the elements that are common between the two lists, without duplicates.

# List Flattening: Write a function to flatten a nested list structure. For example, [[1,2,3], [4,5], [6,7,8]] should become [1, 2, 3, 4, 5, 6, 7, 8].

# Sets:
# Power Set: Write a function that returns the power set of a given set (all possible subsets, including the empty set and itself).

# Set Symmetric Difference: Write a function that computes the symmetric difference between two sets (elements that are in either of the sets but not in both).

# Set Partition: Write a function that partitions a set into two subsets such that the difference of their sums is minimized.

# Tuples:
# Tuple Sorting: Write a function that sorts a list of tuples based on the second element of each tuple.

# Tuple Merge: Write a function that merges two sorted tuples into a single sorted tuple.

# Tuple Uniqueness Check: Write a function that checks if all elements in a tuple are unique.

# Dictionaries:
# Dictionary Inversion: Write a function that inverts a dictionary, where the values become keys and the keys become values (assuming the values are unique).

# Dictionary Intersection: Write a function that takes two dictionaries and returns a new dictionary containing only the key-value pairs that are common to both dictionaries.

# Dictionary Key Mapping: Write a function that maps keys of a dictionary according to a specified mapping function.