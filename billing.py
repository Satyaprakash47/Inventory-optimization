from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
class BillClass:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1550x790+0+0")
    self.root.title("INVENTORY OPTIMISATION")
    self.root.config(bg="white")
    self.cart_list=[]
    self.chk_print=0
    #===TITLE===#
    self.icon_title=PhotoImage(file="images/logo1.png")
    title=Label(self.root,text="MY INVENTORY",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
       
    #===Btn_logout===#
    Btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="red").place(x=1300,y=10,height=50,width=150)
    #===clock===#
    self.lbl_clock=Label(self.root,text=" Welcome to MY INVENTORY\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white",)
    self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

#========product frame==========
    

    ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
    ProductFrame1.place(x=6,y=110,width=410,height=650)

    pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",21,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)


    self.var_search=StringVar()
    ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
    ProductFrame2.place(x=2,y=42,width=398,height=90)

    lbl_search=Label(ProductFrame2,text="Search Product | By name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
       
    lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
    txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=130,y=47,width=150,height=22)

    btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=100,height=25)
    btn_show_all=Button(ProductFrame2,text="Show All", command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=25)

    ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
    ProductFrame3.place(x=2,y=140,width=398,height=470)

    scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
    scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
      

    self.product_Table=ttk.Treeview(ProductFrame3,columns=("Pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.product_Table.xview)
    scrolly.config(command=self.product_Table.yview)

    self.product_Table.heading("Pid",text="Pid")
    self.product_Table.heading("name",text="Name")
    self.product_Table.heading("price",text="Price")
    self.product_Table.heading("qty",text="Qty")
    self.product_Table.heading("status",text="Status")
    self.product_Table["show"]="headings"

    self.product_Table.column("Pid",width=40)
    self.product_Table.column("name",width=100)
    self.product_Table.column("price",width=100)
    self.product_Table.column("qty",width=40)
    self.product_Table.column("status",width=90)
    self.product_Table.pack(fill=BOTH,expand=1)
    self.product_Table.bind("<ButtonRelease-1>",self.get_data)

    lbl_note=Label(ProductFrame1,text="Note: Enter 0 Quantity to remove from the cart",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
         
    #=====customer frame======#
    self.var_cname=StringVar()
    self.var_contact=StringVar()
    customerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
    customerFrame.place(x=420,y=110,width=530,height=70)

    cTitle=Label(customerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgrey").pack(side=TOP,fill=X)
         
    lbl_name=Label(customerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
    txt_name=Entry(customerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)
    lbl_conntact=Label(customerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
    txt_conntact=Entry(customerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

    #====cal cart frame======#
    cal_cat_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    cal_cat_Frame.place(x=420,y=190,width=530,height=460)

    #====calulator frame====#
    self.var_cal_input=StringVar()
    cal_Frame=Frame(cal_cat_Frame,bd=9,relief=RIDGE,bg="white")
    cal_Frame.place(x=5,y=10,width=268,height=440)

    txt_cal_input=Entry(cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
    txt_cal_input.grid(row=0,columnspan=4)

    btn_7=Button(cal_Frame,text="7",font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=25,cursor="hand2").grid(row=1,column=0)
    btn_8=Button(cal_Frame,text="8",font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=25,cursor="hand2").grid(row=1,column=1)
    btn_9=Button(cal_Frame,text="9",font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=25,cursor="hand2").grid(row=1,column=2)
    btn_sum=Button(cal_Frame,text="+",font=('arial',15,'bold'),command=lambda:self.get_input("+"),bd=5,width=4,pady=25,cursor="hand2").grid(row=1,column=3)
    btn_4=Button(cal_Frame,text="4",font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=25,cursor="hand2").grid(row=2,column=0)
    btn_5=Button(cal_Frame,text="5",font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=25,cursor="hand2").grid(row=2,column=1)
    btn_6=Button(cal_Frame,text="6",font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=25,cursor="hand2").grid(row=2,column=2)
    btn_sub=Button(cal_Frame,text="-",font=('arial',15,'bold'),command=lambda:self.get_input("-"),bd=5,width=4,pady=25,cursor="hand2").grid(row=2,column=3)
    btn_1=Button(cal_Frame,text="1",font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=25,cursor="hand2").grid(row=3,column=0)
    btn_2=Button(cal_Frame,text="2",font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=25,cursor="hand2").grid(row=3,column=1)
    btn_3=Button(cal_Frame,text="3",font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=25,cursor="hand2").grid(row=3,column=2)
    btn_mul=Button(cal_Frame,text="x",font=('arial',15,'bold'),command=lambda:self.get_input("*"),bd=5,width=4,pady=25,cursor="hand2").grid(row=3,column=3)
    btn_0=Button(cal_Frame,text="0",font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=21,cursor="hand2").grid(row=4,column=0)
    btn_c=Button(cal_Frame,text="c",font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=21,cursor="hand2").grid(row=4,column=1)
    btn_eq=Button(cal_Frame,text="=",font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=21,cursor="hand2").grid(row=4,column=2)
    btn_div=Button(cal_Frame,text="/",font=('arial',15,'bold'),command=lambda:self.get_input("/"),bd=5,width=4,pady=21,cursor="hand2").grid(row=4,column=3)

    #=====cart frame=====#
    cart_Frame=Frame(cal_cat_Frame,bd=3,relief=RIDGE)
    cart_Frame.place(x=280,y=8,width=245,height=442)
    self.cartTitle=Label(cart_Frame,text="Cart \t Total Product:[0]",font=("goudy old style",15),bg="lightgrey")
    self.cartTitle.pack(side=TOP,fill=X)

    scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
    scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)
      

    self.cartTable=ttk.Treeview(cart_Frame,columns=("Pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.cartTable.xview)
    scrolly.config(command=self.cartTable.yview)

    self.cartTable.heading("Pid",text="Pid")
    self.cartTable.heading("name",text="Name")
    self.cartTable.heading("price",text="Price")
    self.cartTable.heading("qty",text="Qty")
    self.cartTable["show"]="headings"

    self.cartTable.column("Pid",width=40)
    self.cartTable.column("name",width=100)
    self.cartTable.column("price",width=90)
    self.cartTable.column("qty",width=50)
    self.cartTable.pack(fill=BOTH,expand=1)
    self.cartTable.bind("<ButtonRelease-1>", self.get_data_cart)

    #=====add cart widgets frame======#
    self.var_pid=StringVar()
    self.var_pname=StringVar()
    self.var_price=StringVar()
    self.var_qty=StringVar()
    self.var_stock=StringVar()

    add_cart_widget_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    add_cart_widget_Frame.place(x=420,y=650,width=530,height=110)

    lbl_p_name=Label(add_cart_widget_Frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
    txt_p_name=Entry(add_cart_widget_Frame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

    lbl_p_price=Label(add_cart_widget_Frame,text="Price per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
    txt_p_price=Entry(add_cart_widget_Frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
         
    lbl_p_qty=Label(add_cart_widget_Frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
    txt_p_qty=Entry(add_cart_widget_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

    self.lbl_instock=Label(add_cart_widget_Frame,text="In Stock",font=("times new roman",15),bg="white")
    self.lbl_instock.place(x=5,y=70)

    btn_clear=Button(add_cart_widget_Frame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)
    btn_add=Button(add_cart_widget_Frame,text="Add | Update",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

    #==========billing area===========#
    billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    billFrame.place(x=953,y=110,width=570,height=510)

    bTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",21,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
    scrolly=Scrollbar(billFrame,orient=VERTICAL)
    scrolly.pack(side=RIGHT,fill=Y)
    self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
    self.txt_bill_area.pack(fill=BOTH,expand=1)
    scrolly.config(command=self.txt_bill_area.yview)

    #==============billing buttons===============#
    billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    billMenuFrame.place(x=953,y=620,width=570,height=140)

    self.lbl_amount=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
    self.lbl_amount.place(x=2,y=5,width=190,height=70)
    self.lbl_discount=Label(billMenuFrame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
    self.lbl_discount.place(x=194,y=5,width=190,height=70)
    self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
    self.lbl_net_pay.place(x=387,y=5,width=175,height=70)

    btn_print=Button(billMenuFrame,text="Print",command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
    btn_print.place(x=2,y=80,width=190,height=50)
    btn_clearall=Button(billMenuFrame,text="Clear All",command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="grey",fg="white")
    btn_clearall.place(x=194,y=80,width=190,height=50)
    btn_generate=Button(billMenuFrame,text="Generate Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white")
    btn_generate.place(x=387,y=80,width=175,height=50)
    

    self.show()
    #self.bill_top()
    self.update_date_time()
#============all functions==============#
  def get_input(self,num):
    xnum=self.var_cal_input.get()+str(num)
    self.var_cal_input.set(xnum)

  def clear_cal(self):
    self.var_cal_input.set('')

  def perform_cal(self):
    result=self.var_cal_input.get()
    self.var_cal_input.set(eval(result))



  def show(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root) 

  def search(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be Required",parent=self.root)
            else:    
                 cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.product_Table.delete(*self.product_Table.get_children())
                     for row in rows:
                        self.product_Table.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)            
   
  def get_data(self,ev):
      f=self.product_Table.focus()
      content=(self.product_Table.item(f))
      row=content['values']
      self.var_pid.set(row[0])
      self.var_pname.set(row[1])
      self.var_price.set(row[2])
      self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
      self.var_stock.set(row[3])
      self.var_qty.set('1')

  def get_data_cart(self,ev):
      f=self.cartTable.focus()
      content=(self.cartTable.item(f))
      row=content['values']
      self.var_pid.set(row[0])
      self.var_pname.set(row[1])
      self.var_price.set(row[2])
      self.var_qty.set(row[3])
      self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
      self.var_stock.set(row[4])
      
      
  def add_update_cart(self):
    if  self.var_pid.get()=='': 
      messagebox.showerror("Error","Please Select product from the List",parent=self.root)
    elif self.var_qty.get()=='':
      messagebox.showerror('Error','Quantity Is Required',parent=self.root)
    elif int(self.var_qty.get())>int(self.var_stock.get()):
      messagebox.showerror('Error','Invalid Quantity',parent=self.root)
    else:
      #price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
      #price_cal=float(price_cal)
      price_cal=self.var_price.get()
      cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
      #=====update cart==========#
      present='no'
      index_=0
      for row in self.cart_list:
        if self.var_pid.get()==row[0]:
          present='yes'
          break
        index_+=1
      if present=='yes':
        op=messagebox.askyesno('conform',"Product already present do you want to update| Remove from the cart list",parent=self.root)
        if op==True:
          if self.var_qty.get()=="0":
            self.cart_list.pop(index_)
          else:
            #self.cart_list[index_][2]=price_cal
            self.cart_list[index_][3]=self.var_qty.get()

      else:
        self.cart_list.append(cart_data)

      self.show_cart()
      self.bill_update()

  def bill_update(self):
    self.bill_amt=0
    self.net_pay=0
    self.discount=0
    for row in self.cart_list:
      self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
    self.discount=(self.bill_amt*5)/100
    self.net_pay=self.bill_amt-self.discount
    self.lbl_amount.config(text=f'Bill Amnt.\n{str(self.bill_amt)}')
    self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
    self.cartTitle.config(text=f"cart \t Total Products: [{str(len(self.cart_list))}]")



  def show_cart(self):
      try:
          
          self.cartTable.delete(*self.cartTable.get_children())
          for row in self.cart_list:
              self.cartTable.insert('',END,values=row)
      except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root) 

  def generate_bill(self):
    if self.var_cname.get()=='' or self.var_contact.get()=='':
      messagebox.showerror("Error",'Customet Details are required',parent=self.root)
    elif len(self.cart_list)==0:
      messagebox.showerror("Error",'Add product to the cart',parent=self.root)
    else:
      self.bill_top()
      self.bill_middle()
      self.bill_bottom()

      fp=open(f'bill/{str(self.invoice)}.txt','w')
      fp.write(self.txt_bill_area.get('1.0',END))
      fp.close()
      messagebox.showinfo('Saved','Bill has been generated',parent=self.root)
      self.chk_print=1
      

  def bill_top(self):
     self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
     bill_top_temp=f'''
\t\t\t\t MY INVENTORY
    \t\t Phone No.9867******     Gunupur-765022
{str("="*68)}
  Customer Name: {self.var_cname.get()}
  Ph no. :{self.var_contact.get()}
  Bill No. {str(self.invoice)}\t\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*68)}
   Product Name\t\t\t\tQTY\t\t Price
{str("="*68)}
     '''
     self.txt_bill_area.delete('1.0',END)
     self.txt_bill_area.insert('1.0',bill_top_temp)
  
  def bill_bottom(self):
    bill_bottom_temp=f'''
{str("="*68)}
 Bill Amount\t\t\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\t\t\tRs.{self.net_pay}
{str("="*68)}\n
    '''
    self.txt_bill_area.insert(END,bill_bottom_temp)

  def bill_middle(self):
    con=sqlite3.connect(database=r'io.db')
    cur=con.cursor()
    try:
      for row in self.cart_list:
        pid=row[0]
        name=row[1]
        qty=int(row[4])-int(row[3])
        if int(row[3])==int(row[4]):
          status="Inactive"
        if int(row[3])!=int(row[4]):
          status="Active"
        price=float(row[2])*int(row[3])
        price=str(price)
        self.txt_bill_area.insert(END,"\n  "+name+"\t\t\t\t"+row[3]+"\t\tRs."+price)
        #====update qty in product table====#
        cur.execute('Update product set qty=?,status=? where pid=?',(
          qty,
          status,
          pid
        ))
        con.commit()
      con.close()
      self.show()
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

  def clear_cart(self):
    self.var_pid.set('')
    self.var_pname.set('')
    self.var_price.set('')
    self.var_qty.set('')
    self.lbl_instock.config(text=f"In Stock")
    self.var_stock.set('')

  def clear_all(self):
    del self.cart_list[:]
    self.var_cname.set('')
    self.var_contact.set('')
    self.txt_bill_area.delete('1.0',END)
    #self.chk_print=0
    self.cartTitle.config(text=f"cart \t Total Products: [0]")
    elf.var_search.set('')
    self.clear_cart()
    self.show()
    self.show_cart()
  
  def update_date_time(self):
    time_=time.strftime("%I:%M:%S")
    date_=time.strftime("%d:%m:%Y")
    self.lbl_clock.config(text=f" Welcome to MY INVENTORY\t\t Date:{str(date_)} \t\t Time: {str(time_)}")
    self.lbl_clock.after(200,self.update_date_time)
  
  def print_bill(self):
    if self.chk_print==1:
      messagebox.showinfo('Print',"Please wait while printing",parent=self.root )
      new_file=tempfile.mktemp('.txt')
      open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
      os.startfile(new_file,'print')
    else:
      messagebox.showinfo('Print',"Please generate bill to print recipt",parent=self.root )

  def logout(self):
      self.root.destroy()
      os.system("python login.py")    
      
      
if __name__=="__main__":
  root=Tk()
  obj=BillClass(root)    
  root.mainloop()
