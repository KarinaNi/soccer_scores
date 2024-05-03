import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from soccer_display import fetch_data, display_results

def fetch_data_and_display():
    results_text.config(state=tk.NORMAL)
    results_text.delete('1.0', tk.END)
    try:
        matches = fetch_data()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
    else:
        display_results(matches, results_text)
    results_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Sports Results Display")

root.configure(bg="#f0f0f0")
root.option_add("*TCombobox*Listbox*Background", "#ffffff")
root.option_add("*TCombobox*Listbox*Foreground", "#333333")
root.option_add("*TCombobox*Listbox*selectBackground", "#0078d4")
root.option_add("*TCombobox*Listbox*selectForeground", "#ffffff")
root.option_add("*TCombobox*Foreground", "#333333")
root.option_add("*TCombobox*Background", "#ffffff")

results_frame = ttk.Frame(root, padding="10", relief=tk.RIDGE)
results_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

fetch_button = ttk.Button(root, text="Fetch Data", command=fetch_data_and_display)
fetch_button.pack(padx=20, pady=10)

results_text = tk.Text(results_frame, height=20, width=50, wrap=tk.WORD, state=tk.DISABLED)
results_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
