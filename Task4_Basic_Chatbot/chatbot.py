import random
from datetime import datetime

greetings = [
    "Hello Human!",
    "Hey there!",
    "Hi! Ready to chat?",
    "Greetings, Earthling!"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It caught a virus!",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself."
]

facts = [
    "Python was named after Monty Python, not the snake.",
    "The first computer bug was an actual bug.",
    "More than 700 programming languages exist today."
]

roasts = [
    "I'd roast you, but my developer told me to be nice.",
    "Your WiFi is probably stronger than your passwords.",
    "You have opened this chatbot more times than your textbooks."
]

print("=" * 40)
print("      CHATBOT")
print("=" * 40)

print("\nType 'help' to see commands.")
print("Type 'bye' to exit.\n")

while True:

    user = input("You : ").lower()

    if user == "hello" or user == "hi":
        print("Bot :", random.choice(greetings))

    elif user == "how are you":
        print("Bot : I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot : I am Fun ChatBot.")

    elif user == "how old are you":
        print("Bot : I was born when you ran this program.")

    elif user == "joke":
        print("Bot :", random.choice(jokes))

    elif user == "fact":
        print("Bot :", random.choice(facts))

    elif user == "roast me":
        print("Bot :", random.choice(roasts))

    elif user == "i am happy":
        print("Bot : That's great! Keep smiling.")

    elif user == "i am sad":
        print("Bot : Don't worry. Even Python throws exceptions sometimes.")

    elif user == "love advice":
        print("Bot : Talk honestly and don't send 20 messages in a row.")

    elif user == "time":
        print("Bot :", datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot :", datetime.now().strftime("%d-%m-%Y"))

    elif user == "game":

        print("Bot : Let's play Rock Paper Scissors!")
        print("Choose rock, paper or scissors")

        user_choice = input("Your Choice : ").lower()

        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)

        print("Bot Chose :", bot_choice)

        if user_choice == bot_choice:
            print("Bot : It's a Draw!")

        elif user_choice == "rock" and bot_choice == "scissors":
            print("Bot : You Win!")

        elif user_choice == "paper" and bot_choice == "rock":
            print("Bot : You Win!")

        elif user_choice == "scissors" and bot_choice == "paper":
            print("Bot : You Win!")

        else:
            print("Bot : I Win!")

    elif user == "help":

        print("\nAvailable Commands")
        print("------------------")
        print("hello")
        print("hi")
        print("how are you")
        print("what is your name")
        print("how old are you")
        print("joke")
        print("fact")
        print("roast me")
        print("i am happy")
        print("i am sad")
        print("love advice")
        print("time")
        print("date")
        print("game")
        print("help")
        print("bye")

    elif user == "bye":
        print("Bot : Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot : Sorry, I don't understand that command.")