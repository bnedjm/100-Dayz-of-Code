import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.sample_text = ("The quick brown fox jumps over the lazy dog. "
                            "This sentence contains every letter of the alphabet. "
                            "Typing speed tests are a great way to improve your keyboard skills.")
        
        self.start_time = None
        self.end_time = None

        self.create_widgets()
        
    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="Type the following text as quickly and accurately as you can:")
        self.text_label.pack(pady=10)

        self.sample_text_label = tk.Label(self.root, text=self.sample_text, wraplength=400, justify='left')
        self.sample_text_label.pack(pady=10)

        self.entry = tk.Text(self.root, height=10, width=50)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.end_test)
        self.submit_button.pack(pady=5)
        self.submit_button.config(state=tk.DISABLED)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def start_test(self):
        self.entry.delete(1.0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL)
        
    def end_test(self):
        self.end_time = time.time()
        input_text = self.entry.get(1.0, tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("No Input", "Please type the text before submitting.")
            return
        
        time_taken = self.end_time - self.start_time # type: ignore
        word_count = len(input_text.split())
        wpm = (word_count / time_taken) * 60
        
        self.result_label.config(text=f"Time taken: {time_taken:.2f} seconds\nWords per minute: {wpm:.2f} WPM")
        
        self.start_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
