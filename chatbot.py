import re, random 
from colorama import Fore, init
init(autoreset=True)
destination={
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["The Swiss alps", "The Rocky Mountains", "The Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip)
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spot (respond with -Suggest-)")
    print(Fore.GREEN + "- Offer packing tips (respond with -Tips-)")
    print(Fore.BLUE + "Type -Exit- to end program\n")
def recommend():
    print(Fore.CYAN + " What do you prefer the most: Beaches, Mountains or Cities?")
    preferance = input(Fore.YELLOW + "You:")
    preferance = normalize_input(preferance)
    if preferance in destination:
        suggestion = random.choice(destination[preferance])
        print(Fore.GREEN + f"How does a trip to {suggestion} sound like? (respond with yes/no)")
        answer = input(Fore.YELLOW + "You:")
        if answer == "yes":
            print(Fore.GREEN + f"Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "Let's try another.")
            recommend() 
        else:
            print(Fore.RED + "I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "I don't understand.")
        show_help()
def tips():
    print(Fore.CYAN + "Where to?")
    location = normalize_input(input(Fore.YELLOW + "You:"))
    print(Fore.CYAN + "How many days?")
    days = input(Fore.YELLOW + "You:")
    print(Fore.GREEN + f"Some(All) packing tips for {days} days in {location} are:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring charges/adapters")
    print(Fore.GREEN + "- Check the weather on the days you go")

# MAIN PROGRAM

print(Fore.CYAN + "Hello! I'm TravelBot.")
name = input(Fore.YELLOW + "What is your name?")
print(Fore.GREEN + f"Nice to meet you, {name}!")
show_help()

while True:
    user_input = input(Fore.YELLOW + f"{name}: ")
    user_input = normalize_input(user_input)
    if "suggest" in user_input:
        recommend()
    elif "tips" in user_input:
        tips() 
    elif "help" in user_input:
        show_help()
    elif "exit" in user_input:
        print(Fore.CYAN + "Goodbye! Safe travels!")
    else:
        print(Fore.RED + "Could you rephrase?")


