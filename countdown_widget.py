import tkinter as tk
from datetime import datetime

# Target date - February 5th of the upcoming year
target_date = datetime(datetime.now().year, 2, 5, 0, 0, 0)
if datetime.now() > target_date:
    target_date = target_date.replace(year=target_date.year + 1)

def update_clock():
    now = datetime.now()
    remaining = target_date - now

    total_seconds = int(remaining.total_seconds())
    if total_seconds < 0:
        countdown_str = "00d 00h 00m 00s"
    else:
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_str = f"{days}d {hours:02}h {minutes:02}m {seconds:02}s"

    label.config(text=countdown_str)
    root.after(1000, update_clock)

# GUI setup
root = tk.Tk()
root.title("Countdown to February 5th")
root.configure(bg="black")

# Remove window decorations (makes it more "widget-like")
root.overrideredirect(True)

# Make window always on top
root.attributes("-topmost", True)

# Allow dragging by clicking and moving the window
def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")

# Bind mouse events for dragging
root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

# Create the countdown label
label = tk.Label(
    root,
    text="Loading...",
    font=("Arial", 20, "bold"),
    fg="lime",
    bg="black",
    padx=10,
    pady=5
)
label.pack()

# Bind drag events to the label as well
label.bind("<Button-1>", start_move)
label.bind("<B1-Motion>", do_move)

# Start the countdown update loop
update_clock()

# Center the window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# Start the GUI event loop
root.mainloop()