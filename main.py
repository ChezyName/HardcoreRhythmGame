import tkinter as tk
import tkinter.colorchooser as colorchooser
from tkinter import ttk, filedialog
import pyperclip

import json
def save_changes():
    youtube_url = youtube_url_entry.get()
    difficulty = difficulty_slider.get()
    selected_preset = db_slider.get()
    window_background_color = window_bg_entry.get()
    shape_color = shape_color_entry.get()
    warning_zone = warning_zone_entry.get()
    red_zone = red_zone_entry.get()
    #Mouse_mode = mouse_mode_entry.get()
    Mouse_mode = "True" if mouse_mode_var.get() == 1 else "False"

    print(f'youtube_url: {youtube_url}')
    print(f'difficulty: {difficulty}')
    print(f'selected_preset: {selected_preset}')
    print(f'window_background_color: {window_background_color}')
    print(f'shape_color: {shape_color}')
    print(f'warning_zone: {warning_zone}')
    print(f'red_zone: {red_zone}')
    print(f'Mouse_mode: {Mouse_mode}')

    with open('tmp.txt', 'w') as file:
        file.write(f'youtube_url: {youtube_url}\n')
        file.write(f'difficulty: {difficulty}\n')
        file.write(f'selected_preset: {selected_preset}\n')
        file.write(f'window_background_color: {window_background_color}\n')
        file.write(f'shape_color: {shape_color}\n')
        file.write(f'warning_zone: {warning_zone}\n')
        file.write(f'red_zone: {red_zone}\n')
        file.write(f'Mouse_mode: {Mouse_mode}\n')
    root.withdraw()
    import game_main
def choose_color(entry):
    color = colorchooser.askcolor(title="Choose a Color")
    if color[1]:
        hex_color = color[1]
        rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
        entry.delete(0, "end")
        entry.insert(0, str(rgb_color))

root = tk.Tk()
root.title("Text File Editor")

default_values = {
    "youtube_url": "https://youtu.be/JpwKXoIpGk4?si=pWlksUjQlLjpJlvh",
    "difficulty": "0",
    "selected_preset": "0",
    "window_background_color": "(0, 0, 0)",
    "shape_color": "(255, 0, 255)",
    "warning_zone": "(0, 255, 0)",
    "red_zone": "(255, 0, 0)",
    "Mouse_mode": "False"
}

def export_settings():
    settings = {
        "youtube_url": youtube_url_entry.get(),
        "difficulty": difficulty_slider.get(),
        "selected_preset": db_slider.get(),
        "window_background_color": window_bg_entry.get(),
        "shape_color": shape_color_entry.get(),
        "warning_zone": warning_zone_entry.get(),
        "red_zone": red_zone_entry.get(),
        "Mouse_mode": "True" if mouse_mode_var.get() == 1 else "False"
    }

    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

    if file_path:
        with open(file_path, "w") as file:
            json.dump(settings, file, indent=4)
        print("Settings exported to:", file_path)

def import_settings():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as file:
            settings = json.load(file)
            youtube_url_entry.delete(0, "end")
            youtube_url_entry.insert(0, settings.get("youtube_url", ""))
            difficulty_slider.set(settings.get("difficulty", 0))
            db_slider.set(settings.get("selected_preset", 0))
            window_bg_entry.delete(0, "end")
            window_bg_entry.insert(0, settings.get("window_background_color", ""))
            shape_color_entry.delete(0, "end")
            shape_color_entry.insert(0, settings.get("shape_color", ""))
            warning_zone_entry.delete(0, "end")
            warning_zone_entry.insert(0, settings.get("warning_zone", ""))
            red_zone_entry.delete(0, "end")
            red_zone_entry.insert(0, settings.get("red_zone", ""))
            mouse_mode_var.set(1 if settings.get("Mouse_mode", "False") == "True" else 0)
            print("Settings imported from:", file_path)

def paste_new_link():
    youtube_url_entry.delete(0, "end")
    clipboard_data = pyperclip.paste()
    youtube_url_entry.insert(0, clipboard_data)

youtube_url_label = tk.Label(root, text="youtube_url")
youtube_url_label.grid(row=0, column=0)
youtube_url_entry = tk.Entry(root, width=50)
youtube_url_entry.grid(row=0, column=1, columnspan=2)
youtube_url_entry.insert(0, default_values["youtube_url"])
clear_button = tk.Button(root, text="Clear & Paste New", command=paste_new_link)
clear_button.grid(row=1, column=1, columnspan=2)

difficulty_label = tk.Label(root, text="Select Difficulty")
difficulty_label.grid(row=2, column=0)
difficulty_slider = tk.Scale(root, from_=0, to=6, orient="horizontal", length=400)
difficulty_slider.grid(row=2, column=1, columnspan=2)
difficulty_slider.set(default_values["difficulty"])

db_label = tk.Label(root, text="Select Preset")
db_label.grid(row=3, column=0)
db_slider = tk.Scale(root, from_=0, to=9, orient="horizontal", length=400)
db_slider.grid(row=3, column=1, columnspan=2)
db_slider.set(int(default_values["selected_preset"]))

window_bg_label = tk.Label(root, text="window_background_color")
window_bg_label.grid(row=4, column=0)
window_bg_entry = tk.Entry(root)
window_bg_entry.grid(row=4, column=1)
window_bg_entry.insert(0, default_values["window_background_color"])
color_chooser_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(window_bg_entry))
color_chooser_button.grid(row=4, column=2)

shape_color_label = tk.Label(root, text="shape_color")
shape_color_label.grid(row=5, column=0)
shape_color_entry = tk.Entry(root)
shape_color_entry.grid(row=5, column=1)
shape_color_entry.insert(0, default_values["shape_color"])
color_chooser_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(shape_color_entry))
color_chooser_button.grid(row=5, column=2)

warning_zone_label = tk.Label(root, text="warning_zone")
warning_zone_label.grid(row=6, column=0)
warning_zone_entry = tk.Entry(root)
warning_zone_entry.grid(row=6, column=1)
warning_zone_entry.insert(0, default_values["warning_zone"])
color_chooser_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(warning_zone_entry))
color_chooser_button.grid(row=6, column=2)

red_zone_label = tk.Label(root, text="red_zone")
red_zone_label.grid(row=7, column=0)
red_zone_entry = tk.Entry(root)
red_zone_entry.grid(row=7, column=1)
red_zone_entry.insert(0, default_values["red_zone"])
color_chooser_button = tk.Button(root, text="Choose Color", command=lambda: choose_color(red_zone_entry))
color_chooser_button.grid(row=7, column=2)

mouse_mode_label = tk.Label(root, text="Mouse_mode")
mouse_mode_label.grid(row=8, column=0)
mouse_mode_var = tk.IntVar()
mouse_mode_checkbox = tk.Checkbutton(root, text="Mouse_mode", variable=mouse_mode_var)
mouse_mode_checkbox.grid(row=8, column=1)



save_button = tk.Button(root, text="Run game", command=save_changes)
save_button.grid(row=9, column=1)

export_button = tk.Button(root, text="Export Settings", command=export_settings)
export_button.grid(row=10, column=0)

import_button = tk.Button(root, text="Import Settings", command=import_settings)
import_button.grid(row=10, column=2)


root.mainloop()
