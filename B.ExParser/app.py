# import tkinter as tk

# def simplify_and_display():
#     expression = expression_entry.get()
#     try:
#         simplified_expression = simplify_expression(expression)
#         result_label.config(text=f"Simplified Expression: {simplified_expression}")
#     except Exception as e:
#         result_label.config(text=f"Error: {e}")

# # Create the main window
# root = tk.Tk()
# root.title("Boolean Expression Simplifier")
# root.geometry("400x200")

# # Create input field
# expression_label = tk.Label(root, text="Enter a Boolean expression:")
# expression_label.pack(pady=10)
# expression_entry = tk.Entry(root, width=40)
# expression_entry.pack()

# # Create button
# simplify_button = tk.Button(root, text="Simplify", command=simplify_and_display)
# simplify_button.pack(pady=10)

# # Create label for displaying result
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Start the GUI event loop
# root.mainloop()


from pars3r import parse_expression


def main():
    expression = input("Enter a Boolean expression: ")
    simplified_expression = parse_expression(expression)
    print("Original Expression:", expression)
    print("Simplified Expression:", simplified_expression)

if __name__ == "__main__":
    main()