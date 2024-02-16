from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productclass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1270x610+250+130")
       self.root.title("INVENTORY OPTIMISATION")
       self.root.config(bg="white")
       self.root.focus_force()
       #=============================
       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()
       self.var_cat=StringVar()
       self.var_pid=StringVar()

       self.var_sup=StringVar()
       self.cat_list=[]
       self.sup_list=[]
       self.fetch_cat_sup()

       self.var_name=StringVar()
       self.var_price=StringVar()
       self.var_qty=StringVar()
       self.var_status=StringVar()
       product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       product_Frame.place(x=10,y=10,width=450,height=580)

      #===title===#
       title=Label(product_Frame,text=" Manage Products Details",font=("goudy old style",19),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
       
       #===column1===#
       lbl_Category=Label(product_Frame,text="Category",font=("goudy old style",19),bg="white").place(x=30,y=90)
       lbl_Supplier=Label(product_Frame,text="Supplier",font=("goudy old style",19),bg="white").place(x=30,y=160)
       lbl_Product_Name=Label(product_Frame,text="Name",font=("goudy old style",19),bg="white").place(x=30,y=240)
       lbl_Price=Label(product_Frame,text="Price",font=("goudy old style",19),bg="white").place(x=30,y=300)
       lbl_Quantity=Label(product_Frame,text="Quantity",font=("goudy old style",19),bg="white").place(x=30,y=350)
       lbl_Status=Label(product_Frame,text="Status",font=("goudy old style",19),bg="white").place(x=30,y=405)


     
    #===column2===#
       cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_cat.place(x=150,y=90,width=220)
       cmb_cat.current(0) 
       
       cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_sup.place(x=150,y=160,width=220)
       cmb_sup.current(0) 

       txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=240,width=220)
       txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=300,width=220)
       txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=350,width=220)
       
       cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_status.place(x=150,y=410,width=220)
       cmb_status.current(0) 


       #===buttons===#
       btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=500,width=100,height=40)
       btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=500,width=100,height=40)
       btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=500,width=100,height=40)
       btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=500,width=100,height=40)

       #====search box====#
       searchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12), bg="white")
       searchFrame.place(x=510,y=10,width=730,height=80)
       #==options===#
       cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("select","Supplier","Category","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_search.place(x=10,y=10,width=200)
       cmb_search.current(0)


       txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=230,y=10,width=280)
       btn_search=Button(searchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=530,y=8,width=160,height=30)
       
       #===product details========

       p_frame=Frame(self.root,bd=3,relief=RIDGE)
       p_frame.place(x=508,y=100,width=730,height=490)

       scrolly=Scrollbar(p_frame,orient=VERTICAL)
       scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
      

       self.product_table=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.product_table.xview)
       scrolly.config(command=self.product_table.yview)

       self.product_table.heading("pid",text="P_ID")
       self.product_table.heading("Category",text="CATEGORY")
       self.product_table.heading("Supplier",text="SUPPLIER")
       self.product_table.heading("name",text="NAME")
       self.product_table.heading("price",text="PRICE")
       self.product_table.heading("qty",text="QUANTITY")
       self.product_table.heading("status",text="STATUS")
       self.product_table["show"]="headings"

       self.product_table.column("pid",width=90)
       self.product_table.column("Category",width=100)
       self.product_table.column("Supplier",width=100)
       self.product_table.column("name",width=100)
       self.product_table.column("price",width=100)
       self.product_table.column("qty",width=100)
       self.product_table.column("status",width=100)
    
       self.product_table.pack(fill=BOTH,expand=1)
       self.product_table.bind("<ButtonRelease-1>",self.get_data)

       self.show()
       
#===================================================================================================================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            cur.execute("select  name from category")
            cat=cur.fetchall()
            if len(cat)>0:
               del self.cat_list[:]
               self.cat_list.append("Select")  
               for i in cat:
                  self.cat_list.append(i[0])
            

            cur.execute("select  name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
              del self.sup_list[:]
              self.sup_list.append("Select")  
              for i in sup:
                  self.sup_list.append(i[0])
           
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    def add(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                 cur.execute("select * from product where name=?",(self.var_name.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error", "Product already present,try different",parent=self.root)
                 else:
                     cur.execute("Insert into product (Category,Supplier,name,price,qty,status)  values(?,?,?,?,?,?)",(         
                                              self.var_cat.get(),
                                              self.var_sup.get(),
                                              self.var_name.get(),
                                              self.var_price.get(),
                                              self.var_qty.get(),
                                              self.var_status.get(),
                                             
            ))
            con.commit()
            messagebox.showinfo("Sucess","Product Added sucessfully", parent=self.root)
            self.show()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root) 


    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_sup.set(row[2]),
        self.var_cat.set(row[1]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
                                             


    def update(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from the list",parent=self.root)
            else:
                 cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error", "Invalid product ID",parent=self.root)
                 else:
                     cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(         
                                              self.var_cat.get(),
                                              self.var_sup.get(),
                                              self.var_name.get(),
                                              self.var_price.get(),
                                              self.var_qty.get(),
                                              self.var_status.get(),
                                              self.var_pid.get()
            ))
                     con.commit()
                     messagebox.showinfo("Sucess","Product Updated sucessfully", parent=self.root)
                     self.show()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    

    def delete(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
           if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from list",parent=self.root)
           else:
                 cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error", "Invalid product",parent=self.root)
                 else: 
                      op=messagebox.askyesno("Conform","Do you really want to delete?",parent=self.root)
                      if op==True:
                         cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                         self.clear()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    
    def clear(self):
       self.var_cat.set("Select"),
       self.var_sup.set("Select"),
       self.var_name.set(""),
       self.var_price.set(""),
       self.var_qty.set(""),
       self.var_status.set("Active"),
       self.var_pid.set("")
       self.var_searchtxt.set("")
       self.var_searchby.set("Select")
       self.show()
    
    def search(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be Required",parent=self.root)
            else:    
                 cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.product_table.delete(*self.product_table.get_children())
                     for row in rows:
                        self.product_table.insert('',END,values=row)
                 else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root) 






if __name__=="__main__":
     root=Tk()
     obj=productclass(root)    
     root.mainloop()