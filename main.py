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

list1 = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for rock' 1 for paper' 2 for scissors.\n"))
com_choice = random.randint(0, 2)

if your_choice == 0:
    if com_choice == 0:
        print("draw")

    elif com_choice == 1:
        print("Computer wins")
    else:
        print("You win")
elif your_choice == 1:
    if com_choice == 1:
        print("draw")
    elif com_choice == 0:
        print("You win")
    else:
        print("Computer wins")
elif your_choice == 2:
    if com_choice == 2:
        print("draw")
    elif com_choice == 0:
        print("Computer wins")
    else:
        print("You win")
else:
    print("You wrote wrong number.")

print(f"Your choice is {list[your_choice]}")
print(f"Computer's choice is {list[com_choice]}")