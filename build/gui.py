import random
import tkinter as tk

def generate_numbers():
    numbers = []
    while True:
        numbers = [random.randint(1, 25) for _ in range(4)]
        if sum(numbers) == 26:
            break
    # Select characters corresponding to numbers
    chars = ['A', 'B', 'C']
    sample_size = min(len(chars), len(numbers))
    char_indices = random.sample(range(len(chars)), sample_size)
    chars = [chars[i] for i in char_indices]
    return numbers, chars

def update_invite_numbers():
    invite1_numbers, invite1_chars = generate_numbers()
    invite2_numbers, invite2_chars = generate_numbers()
    invite3_numbers, invite3_chars = generate_numbers()

    # Update the text on the labels
    label_invite1.config(text=", ".join(map(str, invite1_chars)))
    label_invite2.config(text=", ".join(map(str, invite2_chars)))
    label_invite3.config(text=", ".join(map(str, invite3_chars)))

def create_grid(canvas):
    # Create labels for displaying invite numbers
    label_dash2 = tk.Label(canvas, text="", font=("Arial", 20))
    label_dash2.grid(row=0, column=0, padx=5, pady=5)
    label_cc1 = tk.Label(canvas, text="C", font=("Arial", 20), bg="lightblue")
    label_cc1.grid(row=0, column=1, padx=5, pady=5)
    label_cc2 = tk.Label(canvas, text="C", font=("Arial", 20), bg="lightblue")
    label_cc2.grid(row=0, column=2, padx=5, pady=5)
    label_dash1 = tk.Label(canvas, text="", font=("Arial", 20))
    label_dash1.grid(row=0, column=3, padx=5, pady=5)
    
    label_ba1 = tk.Label(canvas, text="B", font=("Arial", 20), bg="lightpink")
    label_ba1.grid(row=1, column=0, padx=5, pady=5)
    label_aa1 = tk.Label(canvas, text="A", font=("Arial", 20), bg="lightgreen")
    label_aa1.grid(row=1, column=1, padx=5, pady=5)
    label_aa2 = tk.Label(canvas, text="A", font=("Arial", 20), bg="lightgreen")
    label_aa2.grid(row=1, column=2, padx=5, pady=5)
    label_ba2 = tk.Label(canvas, text="B", font=("Arial", 20), bg="lightpink")
    label_ba2.grid(row=1, column=3, padx=5, pady=5)
    
    label_ba3 = tk.Label(canvas, text="B", font=("Arial", 20), bg="lightpink")
    label_ba3.grid(row=2, column=0, padx=5, pady=5)
    label_aa3 = tk.Label(canvas, text="A", font=("Arial", 20), bg="lightgreen")
    label_aa3.grid(row=2, column=1, padx=5, pady=5)
    label_aa4 = tk.Label(canvas, text="A", font=("Arial", 20), bg="lightgreen")
    label_aa4.grid(row=2, column=2, padx=5, pady=5)
    label_ba4 = tk.Label(canvas, text="B", font=("Arial", 20), bg="lightpink")
    label_ba4.grid(row=2, column=3, padx=5, pady=5)
    
    label_dash2 = tk.Label(canvas, text="", font=("Arial", 20))
    label_dash2.grid(row=3, column=0, padx=5, pady=5)
    label_cc3 = tk.Label(canvas, text="C", font=("Arial", 20), bg="lightblue")
    label_cc3.grid(row=3, column=1, padx=5, pady=5)
    label_cc4 = tk.Label(canvas, text="C", font=("Arial", 20), bg="lightblue")
    label_cc4.grid(row=3, column=2, padx=5, pady=5)
    label_dash3 = tk.Label(canvas, text="", font=("Arial", 20))
    label_dash3.grid(row=3, column=3, padx=5, pady=5)

def create_button(window):
    button = tk.Button(window, text="Generate Numbers", font=("Arial", 14), command=update_invite_numbers)
    button.place(relx=0.9, rely=0.9, anchor="se")

def create_gui():
    window = tk.Tk()
    window.geometry("600x480")
    window.title("Invite Numbers")

    # Create a frame to hold the content
    frame = tk.Frame(window, bg="#D9D9D9")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create labels for displaying invite numbers
    global label_invite1, label_invite2, label_invite3
    label_invite1 = tk.Label(frame, text="", font=("Arial", 14), bg="#E0DDCF")
    label_invite1.grid(row=0, column=1, padx=10, pady=5)

    label_invite2 = tk.Label(frame, text="", font=("Arial", 14), bg="#EAC9C1")
    label_invite2.grid(row=1, column=1, padx=10, pady=5)

    label_invite3 = tk.Label(frame, text="", font=("Arial", 14), bg="#E4E6C3")
    label_invite3.grid(row=2, column=1, padx=10, pady=5)

    # Create a button to generate new numbers
    create_button(frame)

    # Set initial numbers when the program starts
    update_invite_numbers()

    canvas = tk.Canvas(window, bg="white", width=300, height=200)
    canvas.place(relx=0.5, rely=0.5, anchor="center")
    
    create_grid(canvas)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
