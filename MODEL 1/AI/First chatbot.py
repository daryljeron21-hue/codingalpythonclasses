print("Hello! I am a AI Bot. What's your question?")

name = "Jeron"
print(f"Nice to meet you,{name}!")
print("How are you feeling Today? (good/bad)")
mood = "good".lower()

if mood == "good":
    print("I'm glad to hear that")
elif mood == "bad":
    print("I'm sorry to her that.")
else:
    print("Sometimes its hard to put emotion into word")

print(f"It was nice chatting with you {name}")