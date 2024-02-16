from tkinter import*
from PIL import Image,ImageTk
from employee import emploeeclass
from supplier import supplierclass
from category import categoryclass
from product  import productclass
from sales import salesclass
import time
import sqlite3
from tkinter import messagebox
import os
class IO:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1550x790+0+0")
       self.root.title("INVENTORY OPTIMISATION")
       self.root.config(bg="white")

       #===TITLE===#
       self.icon_title=PhotoImage(file="images/logo1.png")
       title=Label(self.root,text="MY INVENTORY",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
       
      #===Btn_logout===#
       Btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="red").place(x=1300,y=10,height=50,width=150)
       #===clock===#
       self.lbl_clock=Label(self.root,text=" Welcome to MY INVENTORY\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white",)
       self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

       #===left menu===#
       self.MenuLogo=Image.open("images\menu_im.png")
       self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
       self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

       LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       LeftMenu.place(x=0,y=102,width=250,height=660)

       lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
       lbl_MenuLogo.pack(side=TOP,fill=X)

       self.icon_side=PhotoImage(file="images/side.png")
       lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",30),bg="#009688").pack(side=TOP,fill=X)


       Btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       Btn_Suplier=Button(LeftMenu,text="Suplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       Btn_category=Button(LeftMenu,text="category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       Btn_Product=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       Btn_Sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       Btn_Exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

       
       #===content===#
       self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_employee.place(x=350,y=120,height=150,width=300)
       
       self.lbl_Supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_Supplier.place(x=750,y=120,height=150,width=300)
       
       self.lbl_Category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_Category.place(x=1150,y=120,height=150,width=300)

       self.lbl_Product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_Product.place(x=350,y=300,height=150,width=300)

       self.lbl_Sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
       self.lbl_Sales.place(x=750,y=300,height=150,width=300)
       
      
       self.update_content()
     #===footer===
       lbl_footer=Label(self.root,text="Inventory Optimization | Developed by Satya prakash samal |\n ",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)#=================================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=emploeeclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)


    def update_content(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Product.config(text=f'Total Product\n[ {str(len(product))} ]')

            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_Supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')

            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_Category.config(text=f'Total Category\n[ {str(len(category))} ]')
             
            bill=len(os.listdir('bill'))
            self.lbl_Sales.config(text=f'Total Sales\n[ {str(bill)} ]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d:%m:%Y")
            self.lbl_clock.config(text=f" Welcome to MY INVENTORY\t\t Date:{str(date_)} \t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")





if __name__=="__main__":
  root=Tk()
  obj=IO(root)    
  root.mainloop()
