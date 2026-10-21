import tkinter as tk
from tkinter import colorchooser,messagebox
root = tk.Tk()
root.title("Digital Drawing board")
root.geometry("800x600")
brush_color = "black"
brush_size = 5
last_x = None
last_y=None
title = tk.Label(root, text="Digital Drawing Board", font=("Arial", 24, "bold"))
title.pack(pady=10)
def start_drawing(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y
def draw(event):
    global last_x, last_y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=brush_color, width=brush_size)
    last_x = event.x
    last_y = event.y
def stop_drawing(event):
    global last_x, last_y
    last_x = None
    last_y = None
def choose_color():
    global brush_color
    color = colorchooser.askcolor()[1]
    if color:
        brush_color = color
def change_size(value):
    global brush_size
    brush_size = int(float(value))
def eraser():
    global brush_color
    brush_color = "white"
def clear_canvas():
    answer = messagebox.askyesno("Clear Canvas", "Are you sure you want to clear the canvas?")
    if answer:
        canvas.delete("all")
toolbar = tk.Frame(root)
toolbar.pack(pady=10)
tk.Button(toolbar, text="Choose Color", command=choose_color).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Eraser", command=eraser).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Clear Canvas", command=clear_canvas).pack(side=tk.LEFT, padx=5)
size_slider = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size", command=change_size)
size_slider.set(5)
size_slider.pack(side=tk.LEFT, padx=5)
canvas = tk.Canvas(root, bg="white", cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)
root.mainloop()