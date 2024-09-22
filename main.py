from tkinter import *
import os
import shutil
root = Tk()
root.title("WinRAR Activator")
root.minsize(100, 100)  # width, height
root.geometry("300x100")
root.eval('tk::PlaceWindow . center')
# Create Label in our window
text = Label(root, text="Welcome To WinRAR Activator")
text.pack()
def activate():
    current_dir = os.getcwd()
    file_to_copy = 'rarreg.key'
    dest_dir = 'C:\\Program Files\\WinRAR'
    file_path = os.path.join(current_dir, file_to_copy)
    dest_file_path = os.path.join(dest_dir, file_to_copy)
    try:
        shutil.copy(file_path, dest_file_path)
    except  Exception as e:
        print(e)
    text2 = Label(root, text="Activated", bg="green")
    text2.pack()
btn = Button(root, text="Activate", bg="red",  command=activate)
btn.pack()
root.mainloop()