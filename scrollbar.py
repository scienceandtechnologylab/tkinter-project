import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Scrolling App Example")
    root.geometry("400x300")

    # Create a frame to hold the Text and Scrollbar
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Add a Text widget with the scrollbar
    text_area = tk.Text(frame, yscrollcommand=scrollbar.set, wrap=tk.WORD)
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Connect scrollbar to the text widget
    scrollbar.config(command=text_area.yview)

    # Insert some sample text
    for i in range(100):
        text_area.insert(tk.END, f"Line {i + 1}\n")

    root.mainloop()

if __name__ == "__main__":
    main()
