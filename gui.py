import tkinter as tk
from tkinter import ttk
import sys
from soccer_display import fetch_data, display_results

root = tk.Tk()
root.title("Sports Results Display")

results_frame = ttk.Frame(root, padding="10")
results_frame.pack()

fetch_button = ttk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack()

results_label = ttk.Label(results_frame, text="Results will be displayed here")
results_label.pack()

root.mainloop()

