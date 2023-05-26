#prompt the user to enter a text containing an emoticon
def main():
    text = convert(input("Enter (a text involving) an emoticon: "))
    print(text)

#the function "convert" converts the emoticon into an emoji
def convert(emo):
    emo = emo.replace(":)", "🙂").replace(":(", "🙁")
    return emo

main()