#with class version
class DreamLife:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.happiness = 50
        self.skills = 0

    def study(self):
        self.money -= 10
        self.happiness -= 3
        self.skills += 20

    def work(self):
        self.money += 75
        self.happiness += 7 
        self.skills += 6

    def gym(self):
        self.money -= 5
        self.happiness += 10
        self.skills += 5

    def travel(self):
        self.money -= 30
        self.happiness += 20
        self.skills += 0

    def hobbies(self):
        self.money -= 5
        self.happiness += 15
        self.skills += 2
    
    def is_successful(self):
        print(f"""Congratulations {self.name}, you've done pretty good, you were able to raise £{self.money}.
Your happiness rating started on 50 and you were able to change it to {self.happiness}.
Finally, you were able to increase your skill level to {self.skills}.
It's been a pleaseure, bye {self.name}!!!!""")
    
    def is_unsuccessful(self):
        print(f"""Unfortunately {self.name}, you've not done as well as you could've, you were able to raise £{self.money}/75.
Your happiness rating started on 50 and you changed it to {self.happiness}/60.
Finally, your skill level was {self.skills}/20.
You could try again if you really want to improve your scores {self.name}""")
    def show_info(self):
        print(f"Here is your current information:\n Your money rating: {self.money} \n Your Happiness rating is: {self.happiness}\n Finally, your skills level is: {self.skills}")
        i = input("Submit any key to continue: ")

valid_choices = ["study", "work", "gym", "travel", "hobbies"]

print("Welcome to your dream life simulator!!!")
name = input("What's your name? ")
age = int(input(f"Hey, {name} what's your age? "))
print(f"Hey {name}, im guessing your {age}, I know, I know Im craaazy smart")

player = DreamLife(name, age)
for day in range(1,6):
    print(f"Welcome to day {day} of your dream life simulator {name}")
    for i in valid_choices:
        print(f"-{i}")
    
    choice = input("Above are your optional activies, what would you like to do? ").strip().lower()

    while choice not in valid_choices:
        for i in valid_choices:
            print(f"-{i}!!!!!!!")
        choice = input("DONT WASTE MY TIME, WHAAAT DO YOOOOOOOUUUUUUUU WANT TOO DOOOO!?!?!?!?!?!? ").strip().lower()
    
    print(f"Great choice picking {choice} lets see how it effects your life↓↓↓↓↓↓↓")
    if choice == "study":
        player.study()
    elif choice == "work":
        player.work()
    elif choice == "gym":
        player.gym()
    elif choice == "travel":
        player.travel()
    elif choice == "hobbies":
        player.hobbies()
    player.show_info()

answer = input(f"You've finally completed all {day} days in the simulator, are you ready for your results? ")
while answer != "no" and answer != "yes":
    answer = input("Please answer yes or no: ")
if answer == "no":
   print("I didn't actually care, here are your results↓↓↓↓↓↓")
   print()
   print()

if player.money >= 75 and player.happiness  >=60 and player.skills >=20:
    player.is_successful()
else:
    player.is_unsuccessful()

