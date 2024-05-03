# import tkinter as tk
# from tkinter import font
# from tokenizer_1 import Lexer

# class TokenizerApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("Expression Tokenizer")
#         master.geometry("400x300")
#         master.minsize(500, 500)

#         # Set up fonts
#         self.title_font = font.Font(family="Arial", size=20, weight="bold")
#         self.text_font = font.Font(family="Helvetica", size=12)

#         # Set up frames
#         self.title_frame = tk.Frame(master)
#         self.entry_frame = tk.Frame(master)
#         self.button_frame = tk.Frame(master)
#         self.result_frame = tk.Frame(master)

#         # Set up widgets for first screen
#         self.title_label = tk.Label(self.title_frame, text="Expression Tokenizer", font=self.title_font)
#         self.entry_label = tk.Label(self.entry_frame, text="Enter expression:", font=self.text_font)
#         self.entry = tk.Entry(self.entry_frame, width=70, font=self.text_font)
#         self.tokenize_button = tk.Button(self.button_frame, text="Tokenize", font=self.text_font, command=self.display_result)

#         # Set up widgets for second screen
#         self.token_label = tk.Label(self.result_frame, text="Tokenization result:", font=self.text_font)
#         self.token_text = tk.Text(self.result_frame, height=8, width=45, font=self.text_font)

#         # Pack widgets for first screen
#         self.title_frame.pack(side="top", pady=(30, 10))
#         self.entry_frame.pack(side="top", pady=10)
#         self.button_frame.pack(side="top", pady=10)

#         self.title_label.pack()
#         self.entry_label.pack(side="left")
#         self.entry.pack(side="left", padx=(0, 10))
#         self.tokenize_button.pack()

#     def display_result(self):
#         expression = self.entry.get()
#         lexer = Lexer()
#         lexer.input_text(expression)
#         lexer.get_next_token()
#         tokens = "\n".join(f"{token.type}: {token.value}" for token in lexer.tokens)

#         # Clear existing content on the result text widget
#         self.token_text.delete(1.0, tk.END)
        
#         # Insert new tokens
#         self.token_text.insert(tk.END, tokens)
        
#         # Pack widgets for second screen
#         self.result_frame.pack(side="top", pady=10)
#         self.token_label.pack(pady=(10, 5))
#         self.token_text.pack(fill="both", expand=True)

# def main():
#     root = tk.Tk()
#     app = TokenizerApp(root)
#     # Center the window on the screen
#     window_width = root.winfo_reqwidth()
#     window_height = root.winfo_reqheight()
#     position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
#     position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
#     root.geometry("+{}+{}".format(position_right, position_down))
#     root.mainloop()

# if __name__ == "__main__":
#     main()


from tokenizer import Lexer

lexer = Lexer()
input_text = input("Enter the input text: ")
lexer.input_text(input_text)
tokens = lexer.get_next_token()
output_tokens = []

for token in tokens:
    if token.type.name == "VAR":
        output_tokens.append(" | \"" + token.value + "\"" if token.value else " | \"" + token.type.name + "\"")
    else:
        output_tokens.append(" | \"" + token.type.name + "\"" if token.value is None else " | \"" + token.type.name + " | " + token.value + "\"")

grouped_tokens = ["(" + " | ".join(output_tokens[:5]) + ")" + " | " + " | ".join(output_tokens[5:])]

print(" | ".join(grouped_tokens))