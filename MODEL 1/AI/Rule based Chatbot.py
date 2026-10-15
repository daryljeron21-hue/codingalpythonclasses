import re, random 
from colorama import Fore, init

init(autoresrt=True)

destinations = {
    "beaches": ["Bali","Maldives","Phuket"],
    "mountains": ["Swiss Alps","Rocky mountains ","Himalayas"],
    "cities": ["Tokyo","Paris","New york"]
}
jokes = [
    "Why don't programers like nature? Too many Bugs!",
    "Why did the computer go to the doctor? Because it had virus",
    "Why do travellers always fell warm? Because of all their hot spots"
]
def normalize_input(text):
    return re.sub(r"\s+", "",text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travel_Bot: Beaches, Mountains, or Cities")
    preference = "Mountains"
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travel_Bot How about {suggestion}?")
        print(Fore.CYAN + "Travel_Bot: do you like it? (yes/no)")
        answer = "yes"

        if answer == "yes":
            print(Fore.BLACK + f"Travel_Bot: Awesome! Enjoy {suggestion}!")
        elif answer =="no":
            print(Fore.RED + "Travel_Bot: Let's try another")
            recommend()
        else:
            print(Fore.RED + "Travel_Bot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "Travel_Bot: Sorry, I dont have that type of destination")
        recommend()
def packing_tips():
    print(Fore.CYAN + "Travel_Bot: Where to?")
    location = "Mountains"
    print(Fore.CYAN + "Travel_Bot:How many days?")
    days = 3

    print(Fore.GREEN + f"Travel_Bot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adaptars.")
    print(Fore.GREEN + "- Check the weather forecast.")
def tell_joke():
    print(Fore.YELLOW + f"Travel_Bot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips(say 'packing')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm Travel_Bot.")
    name = "Jeron"
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = "joke"
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "Travel_Bot safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "Travel_Bot: Could you rephrase?")
if __name__ == "__main__":
    chat()