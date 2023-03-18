import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
data = [
    {
        'name': 'Trump',
        'follower_count': 314,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 322,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Atif Aslam',
        'follower_count': 220,
        'description': 'Musician and actor',
        'country': 'Pakistan'
    },
    {
        'name': 'Ali Zafar',
        'follower_count': 201,
        'description': 'Actor and singer',
        'country': 'Pakistan'
    },
    {
        'name': 'Aima Baig',
        'follower_count': 145,
        'description': 'Musician and actress',
        'country': 'Pakistan'
    },
    {
        'name': 'Aftab Iqbal',
        'follower_count': 180,
        'description': 'Reality TV personality and businessman and Self-Made Billionaire',
        'country': 'Pakistan'
    },
    {
        'name': 'Tabish Hashmi',
        'follower_count': 185,
        'description': 'Reality TV personality',
        'country': 'Pakistan'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 300,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Abida Parveen',
        'follower_count': 195,
        'description': 'Musician',
        'country': 'Pakistan'
    },
    {
        'name': 'Neymar',
        'follower_count': 298,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Hamid Mir',
        'follower_count': 116,
        'description': 'Reality TV personality and Model',
        'country': 'Pakistan'
    },
    {
        'name': 'Arshad Iqbal',
        'follower_count': 119,
        'description': 'Reporter',
        'country': 'Pakistan'
    },
    {
        'name': 'Imran Khan',
        'follower_count': 333,
        'description': 'Cricketer',
        'country': 'Pakistan'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Zardari',
        'follower_count': 178,
        'description': 'Politician',
        'country': 'Pakistan'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 194,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 268,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 289,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 187,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 186,
        'description': 'Footballer',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 185,
        'description': 'Footballer',
        'country': 'Spain'
    }
]
import os
clear = lambda: os.system('cls') #on Windows System

print(logo)
choice1 = random.choice(data)
choice2 = random.choice(data)
if choice1 == choice2:
    choice1 = random.choice(data)
    namecampareA = choice1["name"]
    descriptionA = choice1["description"]
    countryA = choice1["country"]
    followersA = choice1["follower_count"]
    print(f"CompareA: {namecampareA}, a {descriptionA}, from {countryA}.")
    print(vs)
    choice2 = random.choice(data)
    namecampareB = choice2["name"]
    descriptionB = choice2["description"]
    countryB = choice2["country"]
    followersB = choice2["follower_count"]
    print(f"Against B: {namecampareB}, a {descriptionB}, from {countryB}.")
else:
    namecampareA = choice1["name"]
    descriptionA = choice1["description"]
    countryA = choice1["country"]
    followersA = choice1["follower_count"]
    print(f"Compare A: {namecampareA}, a {descriptionA}, from {countryA}.")

    print (vs)

    namecampareB = choice2["name"]
    descriptionB = choice2["description"]
    countryB = choice2["country"]
    followersB = choice2["follower_count"]
    print(f"Against B: {namecampareB}, a {descriptionB}, from {countryB}.")

looo = True
count = 0
while looo:
    more_followers = input("Which one has more followers. Type 'A' or 'B': \n").capitalize()
    if more_followers == 'A':
        if followersA > followersB:
            count += 1
            print(f"Hence! you are right and your final score is: {count}")
            clear()
            choice1 = choice2
            namecampareB = namecampareA
            descriptionB = descriptionA
            countryB = countryA
            followersB = followersA
            print(f"Compare A: {namecampareB}, a {descriptionB}, from {countryB}.")
            print(vs)
        else:
            print(f"Sorry! that's wrong. Final score is {count}")
            break
    elif more_followers == 'B':
        if followersB > followersA:
            count += 1
            print(f"Hence! you are right and your final score is: {count}")
            clear()
            choice2 = choice1
            namecampareA = namecampareB
            descriptionA = descriptionB
            countryA = countryB
            followersA = followersB
            print(f"Compare A: {namecampareA}, a {descriptionA}, from {countryA}.")
            print(vs)
        else:
            print(f"Sorry! that's wrong. Final score is {count}")
            break
    else:
        print("You have not entered 'A' or 'B' correctly. ")
    choice2 = random.choice(data)
    namecampareB = choice2["name"]
    descriptionB = choice2["description"]
    countryB = choice2["country"]
    followersB = choice2["follower_count"]
    print(f"Against B: {namecampareB}, a {descriptionB}, from {countryB}.")



