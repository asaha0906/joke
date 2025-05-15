import random

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call fake spaghetti? An impasta!"
    ]
    return random.choice(jokes)

def main():
    print("Welcome to the Joke Generator!")
    while True:
        input("Press Enter to get a joke, or type 'q' to quit: ")
        if input().lower() == 'q':
            print("Goodbye! Hope you had a laugh.")
            break
        print("\n" + get_joke() + "\n")

if __name__ == "__main__":
    main()
