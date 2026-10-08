import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN}🐣Welcome to sentiment Spy! 🐣{Style.RESET_ALL}")
user_name = "Daryl"
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.YELLOW}Hello Agent{user_name}!")
print(f"Type a sentence and i will analyze your sentences and show yo the sentiment!")
print(f"Type {Fore.BLUE},reset{Fore.BLACK}, {Fore.LIGHTMAGENTA_EX},history{Fore.LIGHTGREEN_EX},"f"or {Fore.LIGHTRED_EX},exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:
    user_input="Hello, today there was a science expo in my school"

    if not user_input:
        print(f"{Fore.RED}Please enter some text or valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"\n{Fore.CYAN}Exiting Sentiment Spy. Farewell, Agent {user_name}!😄{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.RED}All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() =="history":
        if not conversation_history:
            print(f"{Fore.Yellow}No converstation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYan}Converstation History:{Style.RESET_ALL}")
            for idx, (text,polarity, sentiment_type) in enumerate(conversation_history,start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😄"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"
                print(f"{idx}. {color}{emoji} {text} "f"Polarity: {polarity:2f}, {sentiment_type}{Style.RESET_ALL}")
            continue
        polarity= TextBlob(user_input).sentiment.polarity          
        if polarity > 0.25:
            sentiment_type = "Positive"
            color = Fore.GREEN
            emoji = "😄"
        elif polarity < -0.25:
            sentiment_type = "Negative"
            color = Fore.RED
            emoji = "😞"
        else:
            sentiment_type = "Neutral"
            color = Fore.Yellow
            emoji = "😞"
        conversation_history.append((user_input, polarity, sentiment_type))

        print(f"{color}{emoji} {sentiment_type} sentiment detected!"f"Polarity: {polarity:.2f}")