from pyrogram import Client, filters


bot = Client (
    "AN OPTIONAL NAME", 
    api_id= your api id,
    api_hash= "your api hash",
    bot_token= "your bot token from botfather"
)


@bot.on_message(filters.text & filters.group)
def caller_in_gp(client, message):
    msg = str(message.text)
    msg2 = msg.split()
    for item in msg2:
        if item == "@your username" or item == "@your another username":
            message.reply_text("sorry (your name) is not available, pls try later")

        elif item == "your name" or item == "your name with capital letters":
            message.reply_text("BEWARE, (your name) IS EVERYWHERE!")



@bot.on_message(filters.text & filters.private)
def message_response(client , message):
    message.reply_text("hello, (your name) is not available right now.pls try later.")


bot.run()
