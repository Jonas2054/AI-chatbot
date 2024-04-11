bot_template = "BOT : {0}"
user_template = "USER : {0}"
def respond(message):
    bot_msg = "I can hear, you said " + message
    bot_msg = "how are you, you said" + message
    bot_msg = "how was your day you said. my day is going good" + message
    bot_msg = "what are you doing you said" + message
    return bot_msg
def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))
while True:
    a=input()
    send_message(message) 
