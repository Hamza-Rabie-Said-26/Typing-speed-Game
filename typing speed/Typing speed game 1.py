import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        # Sample texts for typing
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
            "Python is a high-level programming language with dynamic semantics.",
            "Machine learning is a method of data analysis that automates analytical model building.",
            "Artificial intelligence is the simulation of human intelligence processes by machines.",
            "Data science is an interdisciplinary field that uses scientific methods to extract knowledge from data.",
            "Web development is the work involved in developing a website for the Internet.",
            "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks.",
            "Cloud computing is the delivery of computing services over the Internet.",
            "Blockchain is a system of recording information in a way that makes it difficult to change."
        ]
        
        self.current_text = ""
        self.start_time = 0
        self.end_time = 0
        self.user_input = ""
        
        self.create_widgets()
        self.new_game()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Typing Speed Test", 
            font=("Helvetica", 24, "bold"), 
            bg="#2c3e50", 
            fg="#ecf0f1"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Type the text below as quickly and accurately as you can:",
            font=("Helvetica", 14),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        instructions.pack(pady=5)
        
        # Sample text display
        self.text_display = tk.Label(
            self.root,
            text="",
            font=("Courier", 16),
            wraplength=700,
            justify="left",
            bg="#34495e",
            fg="#ecf0f1",
            relief="solid",
            borderwidth=2,
            padx=20,
            pady=20
        )
        self.text_display.pack(pady=20, padx=50)
        
        # User input area
        input_label = tk.Label(
            self.root,
            text="Start typing here:",
            font=("Helvetica", 14),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        input_label.pack(pady=(30, 5))
        
        self.input_text = tk.Text(
            self.root,
            height=5,
            width=70,
            font=("Courier", 14),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="solid",
            borderwidth=2
        )
        self.input_text.pack(pady=10)
        self.input_text.bind("<KeyRelease>", self.check_input)
        
        # Stats display
        self.stats_frame = tk.Frame(self.root, bg="#2c3e50")
        self.stats_frame.pack(pady=20)
        
        self.wpm_label = tk.Label(
            self.stats_frame,
            text="WPM: 0",
            font=("Helvetica", 16, "bold"),
            bg="#2c3e50",
            fg="#f1c40f"
        )
        self.wpm_label.pack(side=tk.LEFT, padx=20)
        
        self.accuracy_label = tk.Label(
            self.stats_frame,
            text="Accuracy: 0%",
            font=("Helvetica", 16, "bold"),
            bg="#2c3e50",
            fg="#f1c40f"
        )
        self.accuracy_label.pack(side=tk.LEFT, padx=20)
        
        self.time_label = tk.Label(
            self.stats_frame,
            text="Time: 0s",
            font=("Helvetica", 16, "bold"),
            bg="#2c3e50",
            fg="#f1c40f"
        )
        self.time_label.pack(side=tk.LEFT, padx=20)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=20)
        
        self.restart_button = tk.Button(
            button_frame,
            text="New Text",
            command=self.new_game,
            font=("Helvetica", 14, "bold"),
            bg="#3498db",
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        )
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_game,
            font=("Helvetica", 14, "bold"),
            bg="#e74c3c",
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Results display
        self.results_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 16, "bold"),
            bg="#2c3e50",
            fg="#2ecc71"
        )
        self.results_label.pack(pady=20)
        
    def new_game(self):
        self.current_text = random.choice(self.sample_texts)
        self.text_display.config(text=self.current_text)
        self.input_text.delete(1.0, tk.END)
        self.input_text.config(state=tk.NORMAL)
        self.results_label.config(text="")
        self.start_time = 0
        self.end_time = 0
        self.update_stats(0, 0, 0)
        self.input_text.focus_set()
        
    def reset_game(self):
        self.new_game()
        
    def check_input(self, event=None):
        if self.start_time == 0:
            self.start_time = time.time()
            
        self.user_input = self.input_text.get(1.0, tk.END).strip()
        elapsed_time = time.time() - self.start_time
        
        # Calculate accuracy
        correct_chars = 0
        for i in range(min(len(self.current_text), len(self.user_input))):
            if self.current_text[i] == self.user_input[i]:
                correct_chars += 1
        
        accuracy = (correct_chars / len(self.current_text)) * 100 if len(self.current_text) > 0 else 0
        
        # Calculate WPM (words per minute)
        # Assuming an average word length of 5 characters
        words_typed = len(self.user_input) / 5
        wpm = (words_typed / elapsed_time) * 60 if elapsed_time > 0 else 0
        
        self.update_stats(wpm, accuracy, elapsed_time)
        
        # Check if user has finished typing
        if len(self.user_input) >= len(self.current_text):
            self.end_time = time.time()
            self.input_text.config(state=tk.DISABLED)
            self.show_results(wpm, accuracy, elapsed_time)
    
    def update_stats(self, wpm, accuracy, elapsed_time):
        self.wpm_label.config(text=f"WPM: {wpm:.1f}")
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
        self.time_label.config(text=f"Time: {elapsed_time:.1f}s")
        
    def show_results(self, wpm, accuracy, elapsed_time):
        # Determine performance message
        if wpm < 30:
            performance = "Keep practicing!"
        elif wpm < 50:
            performance = "Good job!"
        elif wpm < 70:
            performance = "Great typing!"
        else:
            performance = "Excellent! You're a typing master!"
            
        result_text = f"Completed in {elapsed_time:.1f} seconds\n"
        result_text += f"Words per minute: {wpm:.1f}\n"
        result_text += f"Accuracy: {accuracy:.1f}%\n"
        result_text += performance
        
        self.results_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingSpeedGame(root)
    root.mainloop()