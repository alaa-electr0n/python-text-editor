import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_box.get("1.0", tk.END)
            file.write(content)

def make_text_bold():
    current_tags = text_box.tag_names("sel.first")
    if "bold" in current_tags:
        text_box.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_box.tag_add("bold", "sel.first", "sel.last")
        text_box.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))

def make_text_italic():
    current_tags = text_box.tag_names("sel.first")
    if "italic" in current_tags:
        text_box.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_box.tag_add("italic", "sel.first", "sel.last")
        text_box.tag_configure("italic", font=("TkDefaultFont", 12, "italic"))

root = tk.Tk()
root.title("Text Editor")

text_box = tk.Text(root, wrap="word")
text_box.pack(fill="both", expand=True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Bold", command=make_text_bold)
edit_menu.add_command(label="Italic", command=make_text_italic)

root.mainloop()
