import time
import random
import string

def get_random_sentence(length=10):
    """Generate a random sentence for typing test"""
    word_list = [
        "python", "programming", "keyboard", "speed", "test", 
        "computer", "algorithm", "function", "variable", "string",
        "integer", "float", "boolean", "dictionary", "list",
        "tuple", "set", "loop", "conditional", "module",
        "library", "developer", "software", "hardware", "network",
        "internet", "database", "application", "interface", "system"
    ]
    return ' '.join(random.choice(word_list) for _ in range(length))

def calculate_wpm(start_time, end_time, typed_words):
    """Calculate words per minute"""
    time_elapsed = end_time - start_time
    minutes = time_elapsed / 60
    return len(typed_words) / minutes

def calculate_accuracy(original, typed):
    """Calculate typing accuracy percentage"""
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    return (correct / len(original)) * 100 if original else 0

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    print("Type the following sentence as fast as you can. Press Enter when done.\n")
    
    test_sentence = get_random_sentence()
    print(test_sentence + "\n")
    
    input("Press Enter when you're ready to start typing...")
    start_time = time.time()
    
    user_input = input("Start typing: ")
    end_time = time.time()
    
    # Calculate results
    original_words = test_sentence.split()
    typed_words = user_input.split()
    
    wpm = calculate_wpm(start_time, end_time, typed_words)
    accuracy = calculate_accuracy(test_sentence, user_input)
    
    # Display results
    print("\n===== Results =====")
    print(f"Original text: {test_sentence}")
    print(f"You typed:     {user_input}")
    print(f"Time taken:    {end_time - start_time:.2f} seconds")
    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

def main():
    while True:
        typing_speed_test()
        play_again = input("\nWould you like to try again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()