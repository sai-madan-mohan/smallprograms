import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x300")  # Set window size
root.configure(bg="black")  # Background color

# Create a frame for the clock with padding
frame = tk.Frame(root, bg="black", padx=20, pady=20, bd=5, relief="ridge")
frame.pack(pady=20)

# Time Label
time_label = tk.Label(frame, font=("Arial", 50, "bold"), background="black", foreground="cyan")
time_label.pack()

# Date Label
date_label = tk.Label(frame, font=("Arial", 20, "bold"), background="black", foreground="white")
date_label.pack()

# Function to update time and date
def update_time():
    current_time = strftime("%H:%M:%S %p")  # Get time in HH:MM:SS AM/PM format
    current_date = strftime("%A, %d %B %Y")  # Get date in full format (e.g., Friday, 08 March 2025)
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  # Update every second

# Start the clock
update_time()
root.mainloop()
