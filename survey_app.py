#Here we are asking the user for their name then assigning it to the "name" variable.
name = input('What is your name?')
print(f'Hello {name}!') 
#printed using f string so that we may run the variable within a string.

'''
I found out that depending on how the user inputs the response "yes", the incorrect statement would run.
For example, if I typed "Yes", the else statement would run, NOT the if statement (although the if statement is applied as equal to "yes").
Because of this error, I called the lower function to the allergy variable (which was assigned with the user's input), so essentially it turned anything the user inputed, to all lower cases. 
Now, by calling the lower function, the user can input any variation of "yes" (ie. Yes, YeS, yEs, yeS, YEs, etc.) and the correct statement will run (the if statement == yes).
Same also applies for "no".
'''
allergy = input('Are you allergic to cats or dogs?')
allergy_lower = allergy.lower()
if allergy_lower == "yes":
    print('Aw thats too bad!')
else:
    print('Fantastic!')

like_dogs = input('Do you like dogs?')
like_dogs_lower = like_dogs.lower()
if like_dogs_lower == "yes":
    print('Woof woof! Dogs rock!')
else:
    print('Thats totally understandable!') 

#if, elif and else statements. There are specific print statements that will run when the user inputs "small" or "big", but I wanted a more general print statement for the input "medium" so that it could also be applied when the user decides to input anything ELSE other then "small", "medium", or "big". 

dog_small_big = input('If you could have a dog, would it be small, medium or big?')
dog_small_big_lower = dog_small_big.lower()
if dog_small_big_lower == "small":
    print('Thats adorable!')
elif dog_small_big_lower == "big":
    print('I love big dogs!')
else:
    print('Sweet!')

'''
Here I asked if the user had a dog. 
If they did, I asked the gender of their dog. 
Depending on the gender, the code will run different statements. 
To achieve this, I created nested if statements. 
Finally, if the user DID NOT have a dog, it would just run the outer ELSE statement. 
'''
have_dog = input('So, do you have a dog?')
have_dog_lower = have_dog.lower()
if have_dog_lower == "yes":
    dog_gender = input('Aw! Boy or girl?')
    dog_gender_lower = dog_gender.lower()
    if dog_gender == "boy":
        pet_name = input("What's his name?")
    else:
        pet_name = input("What's her name?")        
    print(f'Aw, I would love to meet {pet_name}!')
else:
    print('Having a dog would make a great companion!')

'''
Here, I asked a question that would return the user input as a string. 
I called the int function to turn the string into an integer. 
I did this because my if statements had integers assigned to the varible, and python will not read a string equal to an integer (ie. "1" != 1). 
'''
how_many_dogs = input('If you could, how many dogs would you like to have? (ex: 1, 2, etc.)')
how_many_dogs_int = int(how_many_dogs)
if how_many_dogs_int == 1:
    print('1 would be awesome!')
elif how_many_dogs_int > 1:
    print('The more the merrier!')
else:
    print('Thats ok! Nothing wrong with that!')

'''
More nested if statements depending on the user input. 
Called the lower function so that it converts the user input into all lower cases, so that python can run the correct if/elif/else statements.
There is an f string for calling a variable into a string statement.
'''
prefer_cat = input('Would you prefer a cat?')
prefer_cat_lower = prefer_cat.lower()
if prefer_cat_lower == "yes":
    tabby = input('Like a tabby?')
    tabby_lower = tabby.lower()
    if tabby_lower == "yes":
        print('Tabbies are awesome!')
    else:
        fav_breed_cat = input('Hm... What is your favorite breed of cats?')
        print(f'Oh, I love {fav_breed_cat}s!')
else:
    print('I like dogs better too!') 

have_cat = input('Do you have a cat?')
have_cat_lower = have_cat.lower()
if have_cat_lower == "yes":
    print('Cats are great!')
else:
    print('Maybe you can consider adopting one in the future!')

how_many_cats = input('If you could, how many cats would you like to have? (ex: 1, 2, 3, etc.)')
how_many_cats_int = int(how_many_cats)
if how_many_cats_int == 1:
    print('Aw thats cute!')
elif how_many_cats_int > 1:
    print('Wow! That would be so much fun!')
else:
    print("No problem! Cats aren't for everyone!")

#Last print statement, thanking the user for partaking in this survey.
print('Thank you for taking this survey!')