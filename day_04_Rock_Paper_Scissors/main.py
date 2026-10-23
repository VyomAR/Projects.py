import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rock_paper_scissors = input("What do you choose? For Rock use 0, Paper use 1 & Scissors use 2:\n")
if rock_paper_scissors == "0":
    print(rock)
elif rock_paper_scissors == "1":
    print(paper)
elif rock_paper_scissors == "2":
    print(scissors)

random_comp = random.randint(0,2)
game_images = ["Rock","Paper","Scissors"]

print(f"Computer Chose: {game_images[random_comp]}")

if random_comp == 0:
    print(rock)
elif random_comp == 1:
    print(paper)
elif random_comp == 2:
    print(scissors)

if (rock_paper_scissors == "0" and random_comp == 0) or (rock_paper_scissors == "1" and random_comp == 1) or (rock_paper_scissors == "2" and random_comp == 2):
    print("Its a Draw!")
elif (rock_paper_scissors == "0" and random_comp == 2) or (rock_paper_scissors == "1" and random_comp == 0) or (rock_paper_scissors == "2" and random_comp == 1):
    print("You Won!")
elif (rock_paper_scissors == "0" and random_comp == 1) or (rock_paper_scissors == "2" and random_comp == 0) or (rock_paper_scissors == "1" and random_comp == 2):
    print("You Lost!")
else:
    print("You typed an invalid number!")
