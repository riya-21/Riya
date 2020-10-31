from random import choice

responses = ["As I see it, yes", "Ask again later", "It is certain", "Don't count on it", "My sources say no",
             "Better not tell you now", "Signs point to yes", "Reply hazy try again", "Very doubtful"]

question = input("What is your question?").strip()

next_question = ""
while next_question != "Q" :
    print("in progress...")
    print(choice(responses))
    next_question = input("please enter your question or type q to quit the game").strip().upper()






