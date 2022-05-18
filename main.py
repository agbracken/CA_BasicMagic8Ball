import random
response_list = {
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
}
select = 1
response = random.sample(response_list, select)

name = input("What is your name?:")
question = input("What is your question?:")

print(name, "asks:", question)
print("Magic 8-Ball's answer:", response[0])
