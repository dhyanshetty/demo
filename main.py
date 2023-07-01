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

#Write your code below this line 👇
import random
ch=True
while ch:
  c = random.randint(1, 3)
  choic=input("what do you choose? 1-rock 2-paper 3-scissors")
  choice=int(choic)
  if choice==1:
    print(rock)
  elif choice==2:
    print(paper)
  elif choice==3:
    print(scissors)
  else:
    print("invalid choice")
  print("computer chose\n")

  if c==1:
    print(rock)
  elif c==2:
    print(paper)
  else:
    print(scissors)
  if choice==1 and c==2:
    print("computer wins")
  elif choice==2 and c==1:
    print("you win")
  if choice==3 and c==1:
    print("computer wins")
  elif choice==1 and c==3:
    print("you win")
  if choice==2 and c==3:
    print("computer wins")
  elif choice==3 and c==2:
    print("you win")
  elif choice==c:
    print("play again")
  cho=input("do u want to play again? 'y'or 'n'")
  if cho=='y':
    ch=True
  else:
    ch=False