print("Hello! I am a AI friend for you")

name = input("What is your name?")
print(f"Nice to meet you,{name}!")
print("How was your day today? (good/average/bad)")
mood = input().lower()

if mood == "good":
    print("Oh! nice to hear that")
    you_happy = input("What made you happy today?")
    print(f"That's great! {you_happy} sounds like a wonderful experience.")
elif mood == "average":
    print("Haha, it's funny that nothing special happened & was a casual day.")
elif mood == "bad":
    print("I'm sorry to hear that ")
    you_sad = input("What made you sad today?")
    print(f"I'm here for you. {you_sad} can be tough, but remember, it's okay to feel sad sometimes.")
else:
    print("No problem, Sometimes it's hard to put emotions into words")
print("It was nice spending time with you, I belive we wiil meet later and Bye! :) ")