
import tkinter as tk
import os
from tkinter import messagebox
from fs_parser import parse, ParseError

def create_files(structure, base_path='.'):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            with open(path, 'w') as f:
                pass
        else:
            os.makedirs(path, exist_ok=True)
            create_files(content, path)

def on_submit():
    input_script = text_box.get("1.0", "end").strip()
    try:
        structure = parse(input_script)
        create_files(structure)
        output_label.config(text="✅ File structure created.")
    except ParseError as e:
        output_label.config(text=f"❌ Parse Error: {e}")

root = tk.Tk()
root.title("File Structure Creator")

text_box = tk.Text(root, height=10, width=60)
text_box.pack()

submit_btn = tk.Button(root, text="Create", command=on_submit)
submit_btn.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
