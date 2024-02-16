from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class emploeeclass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1270x610+250+130")
       self.root.title("INVENTORY OPTIMISATION")
       self.root.config(bg="white")
       self.root.focus_force()
        #=============================
         #all variables
       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()


       self.var_emp_id=StringVar()
       self.var_emp_gender=StringVar()
       self.var_emp_contact=StringVar()
       self.var_emp_name=StringVar()
       self.var_emp_doj=StringVar()
       self.var_emp_email=StringVar()
       self.var_emp_pass=StringVar()
       self.var_emp_utype=StringVar()
       self.var_emp_dob=StringVar()
       self.var_emp_salary=StringVar()

       
      #====search box====#
       searchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12), bg="white")
       searchFrame.place(x=280,y=20,width=600,height=70)
       #==options===#
       cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_search.place(x=10,y=10,width=180)
       cmb_search.current(0)


       txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
       btn_search=Button(searchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=420,y=8,width=150,height=30)
       

       #===title===#
       title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1180)
       

       #===content===#
       lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
       lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
       lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

       txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
       #txt_gender=Entry(self.root,textvariable=self.var_emp_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
       cmb_gender=ttk.Combobox(self.root,textvariable=self.var_emp_gender,values=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_gender.place(x=500,y=150,width=180)
       cmb_gender.current(0)
       txt_contact=Entry(self.root,textvariable=self.var_emp_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
       

       lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=195)
       lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=195)
       lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=195)

       txt_name=Entry(self.root,textvariable=self.var_emp_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=195,width=180)
       txt_dob=Entry(self.root,textvariable=self.var_emp_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=195,width=180)
       txt_doj=Entry(self.root,textvariable=self.var_emp_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=195,width=180)
       

       lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=235)
       lbl_password=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=235)
       lbl_usertype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=235)

       txt_name=Entry(self.root,textvariable=self.var_emp_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=235,width=180)
       txt_dob=Entry(self.root,textvariable=self.var_emp_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=235,width=180)
       cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_emp_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_usertype.place(x=850,y=230,width=180)
       cmb_usertype.current(0)
       
       lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=280)
       lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=280)
       
       self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
       self.txt_address.place(x=150,y=280,width=300,height=60)
       txt_salary=Entry(self.root,textvariable=self.var_emp_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=280,width=180)
       

       #===buttons===#
       btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=320,width=110,height=28)
       btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=320,width=110,height=28)
       btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=320,width=110,height=28)
       btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=320,width=110,height=28)


       #===employee details===#
       emp_frame=Frame(self.root,bd=3,relief=RIDGE)
       emp_frame.place(x=0,y=380,relwidth=1,height=190)

       scrolly=Scrollbar(emp_frame,orient=VERTICAL)
       scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
      

       self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.EmployeeTable.xview)
       scrolly.config(command=self.EmployeeTable.yview)

       self.EmployeeTable.heading("eid",text="EMP ID")
       self.EmployeeTable.heading("name",text="NAME")
       self.EmployeeTable.heading("email",text="EMAIL")
       self.EmployeeTable.heading("gender",text="GENDER")
       self.EmployeeTable.heading("contact",text="CONTACT")
       self.EmployeeTable.heading("dob",text="DOB")
       self.EmployeeTable.heading("doj",text="DOJ")
       self.EmployeeTable.heading("pass",text="PASS")
       self.EmployeeTable.heading("utype",text="UTYPE")
       self.EmployeeTable.heading("address",text="ADDRESS")
       self.EmployeeTable.heading("salary",text="SALARY")
       self.EmployeeTable["show"]="headings"

       self.EmployeeTable.column("eid",width=90)
       self.EmployeeTable.column("name",width=100)
       self.EmployeeTable.column("email",width=100)
       self.EmployeeTable.column("gender",width=100)
       self.EmployeeTable.column("contact",width=100)
       self.EmployeeTable.column("dob",width=100)
       self.EmployeeTable.column("doj",width=100)
       self.EmployeeTable.column("pass",width=100)
       self.EmployeeTable.column("utype",width=100)
       self.EmployeeTable.column("address",width=100)
       self.EmployeeTable.column("salary",width=200)
       self.EmployeeTable.pack(fill=BOTH,expand=1)
       self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

       self.show()
#======================================================================================================================
    def add(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be  required",parent=self.root)
            elif self.var_emp_pass.get()=="":
                messagebox.showerror("Error","Password must be  required",parent=self.root)
            else:
                 cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error", "This Employee ID already assigned,try different",parent=self.root)
                 else:
                     cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)  values(?,?,?,?,?,?,?,?,?,?,?)",(         
                                              self.var_emp_id.get(),
                                              self.var_emp_name.get(),
                                              self.var_emp_email.get(),
                                              self.var_emp_gender.get(),
                                              self.var_emp_contact.get(),
                                              self.var_emp_dob.get(),
                                              self.var_emp_doj.get(),
                                              self.var_emp_pass.get(),
                                              self.var_emp_utype.get(),
                                              self.txt_address.get('1.0',END),
                                              self.var_emp_salary.get(),
            ))
                     con.commit()
                     messagebox.showinfo("Sucess","EMPLOYEE Added sucessfully", parent=self.root)
            self.show()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root) 


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_emp_email.set(row[2])
        self.var_emp_gender.set(row[3])
        self.var_emp_contact.set(row[4])
        self.var_emp_dob.set(row[5])
        self.var_emp_doj.set(row[6])
        self.var_emp_pass.set(row[7])
        self.var_emp_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_emp_salary.set(row[10])


    def update(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be  required",parent=self.root)
            else:
                 cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error", "Invalid Employee ID",parent=self.root)
                 else:
                     cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(         
                                              self.var_emp_name.get(),
                                              self.var_emp_email.get(),
                                              self.var_emp_gender.get(),
                                              self.var_emp_contact.get(),
                                              self.var_emp_dob.get(),
                                              self.var_emp_doj.get(),
                                              self.var_emp_pass.get(),
                                              self.var_emp_utype.get(),
                                              self.txt_address.get('1.0',END),
                                              self.var_emp_salary.get(),
                                              self.var_emp_id.get(),
            ))
            con.commit()
            messagebox.showinfo("Sucess","EMPLOYEE Updated sucessfully", parent=self.root)
            self.show()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    

    def delete(self):
        con=sqlite3.connect(database=r'io.db')
        cur=con.cursor()
        try:
           if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be  required",parent=self.root)
           else:
                 cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error", "Invalid Employee ID",parent=self.root)
                 else: 
                      op=messagebox.askyesno("Conform","Do you really want to delete?",parent=self.root)
                      if op==True:
                         cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                         self.clear()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root)
    
    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_email.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_contact.set("")
        self.var_emp_dob.set("")
        self.var_emp_doj.set("")
        self.var_emp_pass.set("")
        self.var_emp_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_emp_salary.set("")
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
                 cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                     for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                 else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}", parent=self.root) 

if __name__=="__main__":
     root=Tk()
     obj=emploeeclass(root)    
     root.mainloop()
 
