import tkinter

box = tkinter.Tk()
box.geometry("200x200")


text = tkinter.Label(box, text="a")
text.pack(padx=1, pady=1)

text1 = tkinter.Label(box, text="b")
text1.pack(padx=2, pady=1)

botao = tkinter.Button(box, text="1")
botao.pack(padx=3, pady=1)

botao1 = tkinter.Button(box, text="2")
botao1.pack(padx=4, pady=1)

box.mainloop()