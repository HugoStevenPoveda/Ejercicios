import tkinter as tk
ventPpal=tk.Tk()
ventPpal.title("Steven Poveda")
ventPpal.geometry("500x250")


frame1=tk.Frame(ventPpal,bg="blue")
frame1.pack(expand=True,fill="both")

frame2=tk.Frame(ventPpal,bg="yellow")
frame2.pack(expand=True,fill="both")
frame2.config(cursor="heart")

redbutton=tk.Button(frame1,text="hola",fg="red")
bluebutton=tk.Button(frame1,text="blue",fg="blue")
greenbutton=tk.Button(frame1,text="green",fg="green")
blackbutton=tk.Button(frame1,text="black",fg="black")

redbutton.place(relx=.0 , rely=.05,relwidth=.25 ,relheight=.9)
bluebutton.place(relx=.25 , rely=.05,relwidth=.25 ,relheight=.9)
greenbutton.place(relx=.50 , rely=.05,relwidth=.25 ,relheight=.9)
blackbutton.place(relx=.75 , rely=.05,relwidth=.25 ,relheight=.9)

ventPpal.mainloop()

cyanbutton=tk.Button(frame2,text="red" , ig="red")
cyanbutton.pack()