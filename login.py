from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x760+0+0")
        self.root.config(bg="#fafafa")
        #===images========
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png",)
        self.lbl_Phone_images=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)


        #===Login_frame====
        self.employee_id=StringVar()
        self.password=StringVar()

        Login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(Login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
         
        lbl_user=Label(Login_frame,text="Employee ID",font=("Analus",15),bg="white",fg="#767171").place(x=50,y=120)
        
        txt_employee_id=Entry(Login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=160,width=250,height=30)


        lbl_pass=Label(Login_frame,text="Password",font=("Analus",15),bg="white",fg="#767171").place(x=50,y=220)
        txt_pass=Entry(Login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=260,width=250,height=30)

        btn_login=Button(Login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=320,width=250,height=35)

        hr=Label(Login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        #or_=Label(Login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        #btn_forget=Button(Login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #===frame2========
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Welcome To My Inventory",font=("times new roman",15,"bold"),bg="white").place(x=63,y=15)
        

        #=====Animation Images=======
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()

  #============All functions========

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(3000,self.animate)    

    def login(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error',"All fields are required",parent=self.root)
            else:    
              cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
              user=cur.fetchone() 
              if user==None:
                  messagebox.showerror('Error',"Invalid USERNAME/PASSWORD",parent=self.root)
              else:
                  if user[0]=="Admin":
                      self.root.destroy()
                      os.system("python Dashboard.py")
                  else:
                    self.root.destroy()
                    os.system("python billing.py")    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)      

    


root=Tk()
obj=Login_system(root) 
root.mainloop()  
