from tkinter import *
from tkinter import filedialog

root = Tk()


def encryption():
    file = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg')])
    if file is not None:
        file_name=file.name
        key=entry1.get(1.0,END)
        f1=open(file_name,'rb')
        image=f1.read()
        f1.close()
        image=bytearray(image)
        for i,j in enumerate(image):
            image[i]=j^int(key)
        f2=open(file_name,'wb')
        f2.write(image)
        f2.close()



# root.geometry("400*400")
entry1 = Text(root, height=2, width=10)
entry1.place(x=50, y=50)
b1 = Button(root, text="Encrypt", command=encryption)
b1.place(x=70, y=10)

root.mainloop()
