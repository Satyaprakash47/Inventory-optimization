from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from billing import BillClass
import sqlite3
import os
class salesclass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1270x610+250+130")
       self.root.title("INVENTORY OPTIMISATION")
       self.root.config(bg="white")
       self.root.focus_force()

       self.var_invoice=StringVar()
       self.bill_list=[]
       #title==============================
       lbl_title=Label(self.root,text="View Customer Bills",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
       
       lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="white",).place(x=50,y=100)
       txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow",).place(x=160,y=100,width=180,height=30)
       
       btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=30)
       btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=490,y=100,width=120,height=30)
       btn_generate_bill=Button(self.root,text="Generate bill",command=self.billing,font=("times new roman",15,"bold"),bg="aqua",fg="black",cursor="hand2").place(x=1000,y=530,width=150,height=40)
      
        #=====bill list=======
       sales_frame=Frame(self.root,bd=3,relief=RIDGE)
       sales_frame.place(x=50,y=140,width=250,height=430)

       scrolly=Scrollbar(sales_frame,orient=VERTICAL)
       self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly)
       scrolly.pack(side=RIGHT,fill=Y)
       scrolly.config(command=self.sales_list.yview)
       self.sales_list.pack(fill=BOTH,expand=1)
       
       self.sales_list.bind("<ButtonRelease-1>",self.get_data)

       #======billarea========
       bill_frame=Frame(self.root,bd=3,relief=RIDGE)
       bill_frame.place(x=320,y=140,width=500,height=430)
       
       lbl_title=Label(bill_frame,text="Customer Bills Area",font=("goudy old style",20),bg="orange",).pack(side=TOP,fill=X)

       scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
       self.bill_area=Text(bill_frame,bg="lightyellow",yscrollcommand=scrolly2)
       scrolly2.pack(side=RIGHT,fill=Y)
       scrolly2.config(command=self.bill_area.yview)
       self.bill_area.pack(fill=BOTH,expand=1)

       #=====image========
       self.bill_photo=Image.open("images\cat2.jpg")
       self.bill_photo=self.bill_photo.resize((450,300),Image.ANTIALIAS)
       self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

       lbl_image=Label(self.root,image=self.bill_photo,bd=0)
       lbl_image.place(x=850,y=160)

       self.show() 
 #============================================================
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                 fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                 self.bill_area.delete('1.0',END)
                 for i in fp:
                     self.bill_area.insert(END,i)
                 fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
    
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)

if __name__=="__main__":
     root=Tk()
     obj=salesclass(root)    
     root.mainloop()