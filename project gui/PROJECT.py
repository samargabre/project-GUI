from tkinter import *
import webbrowser

def function1():
    
    link=ent1.get()
    webbrowser.open(link)

fram = Tk()

fram.title("Task - 1")
fram.geometry("400x300")

lab1 = Label(fram , text = "past link here",font = "Tahoma 30 bold" )
lab1.pack(pady=30) 


ent1 = Entry( fram,width=50)
ent1.pack(pady=10)


mybutton1=Button(fram,text="high resulotion",fg="black",bg="gray",font="Helvatica 10 bold",padx=10,pady=3,command=function1)

mybutton1.pack()


mybutton2=Button(fram,text="low resulotion",fg="black",bg="gray",font="Helvatica 10 bold",padx=10,pady=3,command=function1)
mybutton2.pack()

mybutton3=Button(fram,text="Audio only",fg="black",bg="gray",font="Helvatica 10 bold",padx=10,pady=3,command=function1)
mybutton3.pack()

function1()
fram.mainloop()