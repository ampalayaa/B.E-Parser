
# import tkinter as tk
# from tkinter import font
# from tokenizer import Lexer

# class TokenizerGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Tokenization GUI")

#         self._setup_fonts()
#         self._create_widgets()

#     def _setup_fonts(self):
#         self.text_font = font.Font(family="Helvetica", size=12)

#     def _create_widgets(self):
#         self.input_label = tk.Label(self.master, text="Enter the input text:", font=self.text_font)
#         self.input_entry = tk.Entry(self.master, width=50, font=self.text_font)
#         self.tokenize_button = tk.Button(self.master, text="Tokenize", font=self.text_font, command=self.tokenize)
#         self.output_text = tk.Text(self.master, height=10, width=70, font=self.text_font)

#         self.input_label.pack(pady=(10, 0))
#         self.input_entry.pack(pady=5)
#         self.tokenize_button.pack(pady=5)
#         self.output_text.pack(pady=10)

#     def tokenize(self):
#         input_text = self.input_entry.get()
#         lexer = Lexer()
#         lexer.input_text(input_text)
#         tokens = lexer.get_next_token()
        
#         output_tokens = []
#         for token in tokens:
#             if token.type.name == "VAR":
#                 output_tokens.append(f'"{token.type.name}"' + " | \"" + token.value + "\"")
#             else:
#                 output_tokens.append(f'"{token.type.name}"')

#         formatted_output = " | ".join(output_tokens)
#         self.output_text.delete("1.0", tk.END)
#         self.output_text.insert(tk.END, f"({formatted_output})")

# def main():
#     root = tk.Tk()
#     app = TokenizerGUI(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()



from tokenizer import Lexer
from pars3r import Parser

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
