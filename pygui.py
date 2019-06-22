import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text="Extract Images from Presentation")
label.grid(row=0, column=0)

label = tk.Label(frame, text="Presentation")
label.grid(row=1, column=0)

entry = tk.Entry(frame, bg='green')
entry.grid(row=1, column=1)

button = tk.Button(frame, text="Extract Images", bg='gray', fg='red')
button.grid(row=2, column=1)

root.mainloop()
