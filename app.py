import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as fileRef:
        tempApps = fileRef.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


def updateList():
    for widget in frame.winfo_children():
        widget.destroy()

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def addApp():
    updateList()
    fileName = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    updateList()


def runApp():
    for app in apps:
        os.startfile(app)


def delApp():
    apps = []
    if os.path.isfile("save.txt"):
        with open("save.txt", "w") as fileRef:
            fileRef.write("")
    updateList()


root = tk.Tk()

canvas = tk.Canvas(root, height="600", width="600", bg="#000")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth="0.8", relheight="0.8", relx="0.1", rely="0.1")

updateList()

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="red", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="lightblue", command=runApp)
runApps.pack()

delApps = tk.Button(root, text="Clear saved list", padx=10,
                    pady=5, fg="white", bg="lightblue", command=delApp)
delApps.pack()

root.mainloop()

with open("save.txt", "w") as fileRef:
    for app in apps:
        fileRef.write(app + ",")
