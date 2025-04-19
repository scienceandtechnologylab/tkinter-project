import tkinter as tk
import random

class RandomNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Generator")
        self.root.geometry("300x200")
        
        # Create a label to display the random number
        self.number_label = tk.Label(root, font=("Helvetica", 48), width=10, height=2)
        self.number_label.pack(pady=50)
        
        # Start the animation
        self.update_random_number()
    
    def update_random_number(self):
        """Update the label with a new random number"""
        random_number = random.randint(0, 100)  # Random number between 0 and 100
        self.number_label.config(text=str(random_number))
        
        # Call this function again after 500 milliseconds (0.5 second)
        self.root.after(500, self.update_random_number)

# Create the main window and pass it to the RandomNumberApp
root = tk.Tk()
app = RandomNumberApp(root)

# Run the application
root.mainloop()
