import time
import random
from difflib import SequenceMatcher

class TypingSpeedGame:
    def __init__(self):
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog near the riverbank.",
            "Python is a powerful programming language used for web development and data science.",
            "Practice makes perfect when learning to type faster and more accurately.",
            "Technology has revolutionized the way we communicate and work in modern society.",
            "Reading books expands your knowledge and improves your vocabulary significantly.",
            "The beautiful sunset painted the sky with vibrant colors of orange and pink.",
            "Learning new skills requires dedication, patience, and consistent practice every day.",
            "Music has the power to evoke emotions and bring people together across cultures.",
            "Healthy eating habits and regular exercise contribute to overall well-being and longevity.",
            "Innovation drives progress and helps solve complex problems facing humanity today."
        ]
    
    def get_random_text(self):
        """Get a random text sample for typing practice"""
        return random.choice(self.sample_texts)
    
    def calculate_wpm(self, text, time_taken):
        """Calculate words per minute"""
        word_count = len(text.split())
        minutes = time_taken / 60
        return round(word_count / minutes, 2) if minutes > 0 else 0
    
    def calculate_accuracy(self, original, typed):
        """Calculate typing accuracy as a percentage"""
        if not original or not typed:
            return 0
        
        # Use SequenceMatcher to calculate similarity
        similarity = SequenceMatcher(None, original, typed).ratio()
        return round(similarity * 100, 2)
    
    def display_results(self, wpm, accuracy, time_taken, errors):
        """Display the final results"""
        print("\n" + "="*50)
        print("           TYPING SPEED RESULTS")
        print("="*50)
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Words per minute (WPM): {wpm}")
        print(f"Accuracy: {accuracy}%")
        print(f"Number of errors: {errors}")
        print("="*50)
        
        # Performance feedback
        if wpm >= 60:
            print("🏆 Excellent! You're a typing master!")
        elif wpm >= 40:
            print("👍 Great job! Your typing speed is above average!")
        elif wpm >= 25:
            print("👌 Good work! Keep practicing to improve!")
        else:
            print("💪 Keep practicing! You'll get faster with time!")
    
    def count_errors(self, original, typed):
        """Count the number of character errors"""
        errors = 0
        min_length = min(len(original), len(typed))
        
        # Count character mismatches
        for i in range(min_length):
            if original[i] != typed[i]:
                errors += 1
        
        # Add errors for length differences
        errors += abs(len(original) - len(typed))
        
        return errors
    
    def play_game(self):
        """Main game loop"""
        print("🎯 Welcome to the Typing Speed Game! 🎯")
        print("Type the following text as quickly and accurately as possible.")
        print("Press Enter when you're ready to start...\n")
        
        input()  # Wait for user to press Enter
        
        # Get random text
        text_to_type = self.get_random_text()
        
        print("Get ready... 3... 2... 1... GO!\n")
        print("="*60)
        print("TEXT TO TYPE:")
        print("="*60)
        print(f"{text_to_type}")
        print("="*60)
        print("Start typing below:")
        
        # Record start time
        start_time = time.time()
        
        # Get user input
        user_input = input("> ")
        
        # Record end time
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Calculate metrics
        wpm = self.calculate_wpm(text_to_type, time_taken)
        accuracy = self.calculate_accuracy(text_to_type, user_input)
        errors = self.count_errors(text_to_type, user_input)
        
        # Display results
        self.display_results(wpm, accuracy, time_taken, errors)
        
        # Show comparison
        print("\nComparison:")
        print(f"Original:  {text_to_type}")
        print(f"Your text: {user_input}")
    
    def play_multiple_rounds(self):
        """Play multiple rounds of the game"""
        total_wpm = 0
        total_accuracy = 0
        rounds = 0
        
        while True:
            rounds += 1
            print(f"\n🎮 Round {rounds}")
            self.play_game()
            
            # Ask if player wants to continue
            play_again = input("\nDo you want to play another round? (y/n): ").lower().strip()
            
            if play_again != 'y' and play_again != 'yes':
                break
        
        print(f"\n🎊 Thanks for playing! You completed {rounds} round(s).")
        print("Come back anytime to improve your typing speed! 👋")

def main():
    """Main function to run the typing speed game"""
    game = TypingSpeedGame()
    
    print("Choose an option:")
    print("1. Play single round")
    print("2. Play multiple rounds")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        game.play_game()
    elif choice == "2":
        game.play_multiple_rounds()
    else:
        print("Invalid choice. Starting single round...")
        game.play_game()

if __name__ == "__main__":
    main()