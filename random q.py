import tkinter as tk
import random

def generate_numbers():
    numbers = [str(random.randint(0, 1000)) for _ in range(100)]
    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, ' '.join(numbers))
    text_area.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Random Numbers")

text_area = tk.Text(root, height=10, width=50)
text_area.pack()

button = tk.Button(root, text="Generate Numbers", command=generate_numbers)
button.pack()

root.mainloop()
