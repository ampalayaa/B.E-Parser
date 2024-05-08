import customtkinter as ctk
#from tkinter import PhotoImage
from simplifier import simplify_expression

def simplify_and_display():
    expression = expression_entry.get()
    try:
        simplified_expression = simplify_expression(expression)
        output_field.configure(state="normal")
        output_field.delete(0, ctk.END)
        output_field.insert(0, simplified_expression)
        output_field.configure(state="disabled")
    except Exception as e:
        output_field.configure(state="normal")
        output_field.delete(0, ctk.END)
        output_field.insert(0, f"Error: {e}")
        output_field.configure(state="disabled")

def switch_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

root = ctk.CTk() # -> main window
root.title("Boolean Expression Simplifier")
root.geometry("600x400")
root.minsize(500, 500)

# logo_image = PhotoImage("Users\Frances Bea Magdayao\Downloads\moon.png") 

ctk.set_appearance_mode("Dark") # -> apperance mode

expression_label = ctk.CTkLabel(root, text="Enter a Boolean expression:") #input entry
expression_label.pack(pady=10)

expression_entry = ctk.CTkEntry(root, width=400, placeholder_text="Enter your expression here")
expression_entry.pack()

simplify_button = ctk.CTkButton(root, text="Simplify", command=simplify_and_display, bg_color="pink")  # -> simplify button command
simplify_button.pack(padx=20, pady=10)

result_label = ctk.CTkLabel(root, text="Simplified expression:") 
result_label.pack()

output_field = ctk.CTkTextbox(root, width=500, height=200, state="disabled") # -> output field
output_field.pack(padx=20, pady=10)

theme_switcher_frame = ctk.CTkFrame(root)
theme_switcher_frame.pack(side="left", padx=15)

theme_switcher = ctk.CTkButton(theme_switcher_frame, text="Switch Theme", command=switch_theme, bg_color="pink") # --> switch theme command
theme_switcher.pack(pady=10)

root.mainloop() # -> main/gui loop