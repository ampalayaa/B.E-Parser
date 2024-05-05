import tkinter as tk
from simplifier import simplify_expression

def simplify_and_display():
    expression = expression_entry.get()
    try:
        simplified_expression = simplify_expression(expression)
        output_field.config(state="normal")
        output_field.delete(0, tk.END)
        output_field.insert(0, simplified_expression)
        output_field.config(state="readonly")
    except Exception as e:
        output_field.config(state="normal")
        output_field.delete(0, tk.END)
        output_field.insert(0, f"Error: {e}")
        output_field.config(state="readonly")

# Create the main window
root = tk.Tk()
root.title("Boolean Expression Simplifier")
root.geometry("400x200")

# Create input field
expression_label = tk.Label(root, text="Enter a Boolean expression:")
expression_label.pack(pady=10)
expression_entry = tk.Entry(root, width=40)
expression_entry.pack()

# Create button
simplify_button = tk.Button(root, text="Simplify", command=simplify_and_display)
simplify_button.pack(pady=10)

# Create label for displaying result
result_label = tk.Label(root, text="Simplified expression:")
result_label.pack()

# Create output field
output_field = tk.Entry(root, width=40, state="readonly")
output_field.pack()

# Start the GUI event loop
root.mainloop()
