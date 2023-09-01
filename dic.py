from tkinter import*
from PIL import *
root=Tk()
def dict():
 word=n1.get()
 if word in di:
   mean=di[word]

   res.config(text=mean)
 else:
   res.config(text="not present")
root.title("Dictionary")
root.geometry("400x400")
root.resizeable(false,false)
frame=Frame(root,bg="pink",height="400",width="250")
frame.place(x=0,y=0)
frame1=Frame(root,bg="yellow",height="400",width="250")
frame1.place(x=250,y=0)

label=Label(root,text="dictinory",font=("Arial 20 bold"))
label.place(x=100,y=10)
n1=Entry(root,font=("Arial 15"))
n1.place(x=150,y=80)
btn=Button(root,text="search",font=("Arial 15"),bg="light pink",command=dict)
btn.place(x=150,y=150)
di={"apple": "fruit", "dog":"animal","mahima": "a person","warsha": "a person","juhi":"a person","advice":"salah dena","sparrow":"a bird"}
res=Label(root,text="",font=("Arial 20"),bg="green")
res.place(x=150,y=200)
root.mainloop()