import random

choice = input("please enter a choice(rock/paper/scissors) ")

if choice == "rock":
  print("you chose rock")
elif choice == "paper":
    print("you chose paper")
elif choice == "scissors":
    print("you chose scissors")
else:
    print("invalid choice")

 #აქ წერია ამაში ანუ ინ ამით აქედან რამე თუ არ იყო დაწერს რა არჩეული ქონდა და რომ რაღაცა სხვა თუ დაწერე ამოაგდებს რომ არ არის ეგეთი არჩევანი
if choice in ["rock", "paper", "scissors"]:
    computer = random.choice(["rock", "paper", "scissors"])
    print("computer chose:", computer)