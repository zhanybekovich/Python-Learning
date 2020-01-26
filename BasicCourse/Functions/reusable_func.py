def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "\U0001F600",
        ":(": "\U0001F615"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input('>')
print(emoji_converter(message))
