#without class version
print("Welcome to your dream life simulator!!!")
name = input("What's your name? ")
age = int(input(f"Hey, {name} what's your age? "))
print(f"Hey {name}, im guessing your {age}, I know, I know Im craaazy smart")
money = 0
happiness = 0
skills = 0

char_info = {
    "name": name,
    "age": age,
    "money": money,
    "happiness": happiness,
    "skills": skills
}
activities = {
    "study": {"money": -10, "happiness": -3, "skills": 20},
    "work": {"money": 50, "happiness": 7, "skills": 6},
    "gym": {"money": -5, "happiness": 10, "skills": 5},
    "travel": {"money": -30, "happiness": 20, "skills": 0},
    "hobbies": {"money": -5, "happiness": 15, "skills": 2}
}
for day in range(1,6):
    print(f"Welcome to day {day} of your dream life simulator {name}")
    for i in activities:
        print(f"-{i}")

    choice = input("Above are your optional activies, what would you like to do? ")

    while choice not in activities:
        for i in activities:
            print(f"-{i}!!!!!!!")
        choice = input("DONT WASTE MY TIME, WHAAAT DO YOOOOOOOUUUUUUUU WANT TOO DOOOO!?!?!?!?!?!? ")

    print(f"Great choice picking {choice} lets see how it effects your life↓↓↓↓↓↓↓")

    for i in activities[choice]:
        for j in char_info:
            if i == j:
                char_info[j] += activities[choice][i]
    print(char_info)
    
answer = input(f"You've finally completed all {day} days in the simulator, are you ready for your results? ")
while answer != "no" or answer != "yes":
    answer = input("Please answer yes or no: ")
    if answer == "no":
        print("I didn't actually care, here are your results↓↓↓↓↓↓")

if char_info["money"] >= 100 and char_info["happiness"] >=60 and char_info["skills"] >= 20:
    print(f"""Congratulations {name}, you've done pretty good, you were able to raise £{char_info["money"]}. \n 
    Your happiness rating started on 50 and you were able to change it to {char_info["happiness"]}. \n
    Finally, you were able to increase your skill level to {char_info["skills"]}. \n 
    It's been a pleaseure, bye {name}!!!!""")
else:
    print(f"""Unfortunately {name}, you've not done as well as you could've, you were able to raise £{char_info["money"]}. \n 
    Your happiness rating started on 50 and you changeed it to {char_info["happiness"]}. \n
    Finally, your skill level was {char_info["skills"]}. \n 
    You could try again if you really want to improve your scores {name}""")
