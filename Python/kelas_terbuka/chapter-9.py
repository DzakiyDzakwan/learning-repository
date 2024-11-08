import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()

# Configure Window
window.configure(bg='white')

# Window frame Size
window.geometry("800x500")

# Disabled window resizable
window.resizable(False, False)

# Window Title
window.title('Test Application')

# Adding Frame
frame_1 = ttk.Frame(window)

## Grid Pack Placement
frame_1.pack(padx=24, pady=24, fill="x")

# Other Component
FIRST_NAME = tk.StringVar()

label_fname = ttk.Label(frame_1, text="First Name")
label_fname.pack()

input_fname = ttk.Entry(frame_1, textvariable=FIRST_NAME)
input_fname.pack()

LAST_NAME = tk.StringVar()
label_lname = ttk.Label(frame_1, text="Last Name")
label_lname.pack()

input_lname = ttk.Entry(frame_1, textvariable=LAST_NAME)
input_lname.pack()

def handleSubmit():
    """
    This function will called after the button got clicked by User
    """
    message = f"Congrats {FIRST_NAME.get()} {LAST_NAME.get()} you have clicked the button"
    messagebox.showinfo("New Message", message)

button_submit = ttk.Button(frame_1, text='Submit', command=handleSubmit)
button_submit.pack(pady=12)

# Window lopp so it doesn't close
window.mainloop()