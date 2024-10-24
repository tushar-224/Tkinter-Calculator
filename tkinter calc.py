import tkinter as tk
def button_click(char):
    current = entry.get()
    if char == "C":
        entry.delete(0, tk.END)
    elif char == "=":
        try:
            entry.delete(0, tk.END)
            entry.insert(0, eval(current))
        except:
            entry.insert(0, "Error")
    elif char == "←":
        entry.delete(len(current) - 1)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/",
    "←", "C"
]
for i, button in enumerate(buttons):
    tk.Button(root, text=button, padx=10, pady=10, font=("Arial", 16),
              command=lambda b=button: button_click(b)).grid(row=(i // 4) + 1, column=i % 4)

root.mainloop()
