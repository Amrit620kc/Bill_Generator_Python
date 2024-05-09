from tkinter import *
import math, random, os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("CODEWITHAMRIT")
        bg_color="#3358ff"
        bg_colour="#000000"
        title =Label(self.root, text="ALCOHOl BILLING SOFTWARE--SANISHA CHAUDHARY",bd=12, relief=GROOVE,bg=bg_colour,fg="white",font=("times new roman",30, "bold"), pady=2).pack(fill=X)
       
       #======================Cosmetic variabel====================
        self.Barahsin=IntVar()
        self.Namaste=IntVar()
        self.Strong=IntVar()
        self.Mountain=IntVar()
        self.Arna=IntVar()
        self.Mustang=IntVar()

       #=======================Grocery variabel====================
        self.A8848=IntVar()
        self.Ruslan=IntVar()
        self.Yeti=IntVar()
        self.Highlander=IntVar()
        self.Zurick=IntVar()
        self.Smirnoff=IntVar()

       #=======================Drinks variabel====================
        self.White=IntVar()
        self.Flavoured=IntVar()
        self.Gold=IntVar()
        self.Overproof=IntVar()
        self.Smoky=IntVar()
        self.Premium=IntVar()

       #=======================Total Product price====================
        self.Beer_price=StringVar()
        self.Vodka_price=StringVar()
        self.Rum_price=StringVar()


        self.Beer_tax=StringVar()
        self.Vodka_tax=StringVar()
        self.Rum_tax=StringVar()


       #===========cumtomer===================

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x= random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



      

     
       
       
       
       #Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),fg="gold",bg=bg_colour)
        F1.place(x=0,y=80, relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",bg=bg_colour,fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20,pady=5)
        cname_txt=Entry(F1, width=15,  textvariable=self.c_name,  font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_colour,fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20,pady=5)
        cphn_txt=Entry(F1, width=15,   textvariable=self.c_phon,   font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl=Label(F1,text="Customer Number",bg=bg_colour,fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20,pady=5)
        c_bill_txt=Entry(F1, width=15, textvariable=self.search_bill,  font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1, text="Search",command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


        #====BEER===
        F2=LabelFrame(self.root,bd=10,relief=GROOVE, text="BEER", font=("times new roman", 15, "bold"),fg="gold",bg=bg_colour)
        F2.place(x=5,y=180, width=325, height=380)

        BARAHSIN=Label(F2, text="Barahsin", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=1, column=0, padx=10,pady=10, sticky="w")
        BARAHSIN=Entry(F2, width=10,  textvariable=self.Barahsin,   font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10)

        NAMASTE=Label(F2, text="Namaste", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=2, column=0, padx=10,pady=10, sticky="w")
        NAMASTE=Entry(F2, width=10,  textvariable=self.Namaste,    font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10)

        STRONG=Label(F2, text="Strong", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=3, column=0, padx=10,pady=10, sticky="w")
        STRONG=Entry(F2, width=10,   textvariable=self.Strong,   font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10)

        MOUNTAIN=Label(F2, text="Mountain", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=4, column=0, padx=10,pady=10, sticky="w")
        MOUNTAIN=Entry(F2, width=10,   textvariable=self.Mountain,       font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10)

        ARNA=Label(F2, text="Arna", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=5, column=0, padx=10,pady=10, sticky="w")
        ARNA=Entry(F2, width=10,   textvariable=self.Arna,   font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10)

        MUSTANG=Label(F2, text="Mustang", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=6, column=0, padx=10,pady=10, sticky="w")
        MUSTANG=Entry(F2, width=10,     textvariable=self.Mustang,           font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10)


         #**********************RUM*************************
        F3=LabelFrame(self.root,bd=10,relief=GROOVE, text="VODKA", font=("times new roman", 15, "bold"),fg="gold",bg=bg_colour)
        F3.place(x=340,y=180, width=325, height=380)

        A_8848=Label(F3, text="8848", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=1, column=0, padx=10,pady=10, sticky="w")
        A_8848=Entry(F3, width=10,    textvariable=self.A8848,    font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10)

        RUSLAN=Label(F3, text="Ruslan", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=2, column=0, padx=10,pady=10, sticky="w")
        RUSLAN=Entry(F3, width=10,   textvariable=self.Ruslan,  font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10)

        YETI=Label(F3, text="Yeti", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=3, column=0, padx=10,pady=10, sticky="w")
        YETI=Entry(F3, width=10,   textvariable=self.Yeti,      font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10)

        HIGHLANDER=Label(F3, text="Highlander", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=4, column=0, padx=10,pady=10, sticky="w")
        HIGHLANDER=Entry(F3, width=10,     textvariable=self.Highlander,         font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10)

        ZURICK=Label(F3, text="Zurick", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=5, column=0, padx=10,pady=10, sticky="w")
        ZURICK=Entry(F3, width=10,      textvariable=self.Zurick,  font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10)

        SMIRNOFF=Label(F3, text="Smirnoff", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=6, column=0, padx=10,pady=10, sticky="w")
        SMIRNOFF=Entry(F3, width=10,    textvariable=self.Smirnoff,   font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10)


         #**********************DRINKS*************************
        F4=LabelFrame(self.root,bd=10,relief=GROOVE, text="RUM", font=("times new roman", 15, "bold"),fg="gold",bg=bg_colour)
        F4.place(x=670,y=180, width=325, height=380)

        WHITE=Label(F4, text="White", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=1, column=0, padx=10,pady=10, sticky="w")
        WHITE=Entry(F4, width=10,    textvariable=self.White,   font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10)

        FLAVOURED=Label(F4, text="Flavoured", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=2, column=0, padx=10,pady=10, sticky="w")
        FLAVOURED=Entry(F4,        textvariable=self.Flavoured,  width=10, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10)

        GOLD=Label(F4, text="Gold", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=3, column=0, padx=10,pady=10, sticky="w")
        GOLD=Entry(F4,           textvariable=self.Gold,    width=10, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10)

        OVERPROOF=Label(F4, text="Overproof", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=4, column=0, padx=10,pady=10, sticky="w")
        OVERPROOF=Entry(F4, width=10,   textvariable=self.Overproof,      font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10)

        SMOKY=Label(F4, text="Smoky", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=5, column=0, padx=10,pady=10, sticky="w")
        SMOKY=Entry(F4, width=10,    textvariable=self.Smoky,       font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10)

        PREMIUM=Label(F4, text="Premium", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=6, column=0, padx=10,pady=10, sticky="w")
        PREMIUM=Entry(F4, width=10,      textvariable=self.Premium,  font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10)



        #***************Bill Area Frames******************
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180, width=350, height=380)
        bill_title=Label(F5,text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5, orient=VERTICAL)
        self.txtarea=Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        #*******************Button Frame************
        F6=LabelFrame(self.root,bd=10,relief=GROOVE, text="ALCOHOL VAT", font=("times new roman", 15, "bold"),fg="gold",bg=bg_colour)
        F6.place(x=0,y=560, relwidth=1, height=140)

        TOTAL_BEER=Label(F6, text="Total Beer Price", bg=bg_colour, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        TOTAL_BEER=Entry(F6, width=18,    textvariable=self.Beer_price,   font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        TOTAL_VODKA=Label(F6, text="Total Vodka Price", bg=bg_colour, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        TOTAL_VODKA=Entry(F6, width=18,    textvariable=self.Vodka_price,   font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        TOTAL_RUM=Label(F6, text="Total  Rum Price", bg=bg_colour, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        TOTAL_RUM=Entry(F6, width=18,    textvariable=self.Rum_price,       font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        # Tax of beer
        BEER_TAX=Label(F6, text="Beer Tax", bg=bg_colour, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        BEER_TAX=Entry(F6, width=18,    textvariable=self.Beer_tax,  font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)
        # Tax of vodka
        VODKA_TAX=Label(F6, text="Vodka Tax", bg=bg_colour, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        VODKA_TAX=Entry(F6, width=18,     textvariable=self.Vodka_tax,     font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)
        # Tax of rum
        RUM_TAX=Label(F6, text="Rum Tax", bg=bg_colour, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        RUM_TAX=Entry(F6, width=18,    textvariable=self.Rum_tax,  font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)


        btn_F=Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)


        total_btn=Button(btn_F,  command=self.total, text="Total", bg="cadetblue", fg="white", bd=2, pady=11, width=10, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        Gbill_btn=Button(btn_F, text="Generate Bill",   command=self.bill_area, bg="cadetblue", fg="white", bd=2, pady=10, width=11, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn=Button(btn_F, text="Clear", bg="cadetblue", command=self.clear_data, fg="white", bd=2, pady=11, width=10, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn=Button(btn_F, text="Exit", bg="cadetblue", command=self.Exit_app, fg="white", bd=2, pady=11, width=10, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):

        self.brhsin=self.Barahsin.get()*300
        self.nmst=self.Namaste.get()*330
        self.strg=self.Strong.get()*320
        self.mount=self.Mountain.get()*350
        self.arna=self.Arna.get()*320
        self.mustg=self.Mustang.get()*175
         
        # Total beer price===================================
        self.total_beer_price=float(
               self.brhsin+
               self.nmst+
               self.strg+
               self.mount+
               self.arna+
               self.mustg  
        ) 
        self.Beer_price.set("Rs. "+str(self.total_beer_price))  
        self.b_tax= round((self.total_beer_price*00.36),2)
        #tax of cosmetic
        self.Beer_tax.set("Rs. "+str(self.b_tax))  # Tax of beer

        self.a48=self.A8848.get()*2055
        self.rsln=self.Ruslan.get()*1900
        self.yeti=self.Yeti.get()*2200
        self.hgld=self.Highlander.get()*1005
        self.zurk=self.Zurick.get()*1920
        self.smrf=self.Smirnoff.get()*5950
        # Total vodka price=====================================
        self.total_vodka_price=float(

            self.a48+
            self.rsln+
            self.yeti+
            self.hgld+
            self.zurk+
            self.smrf
        ) 
        self.Vodka_price.set("Rs. "+str(self.total_vodka_price)) 
        self.v_tax= round((self.total_vodka_price*00.36),2)
        #tax of vodka
        self.Vodka_tax.set("Rs. "+str(self.v_tax)) # Tax of vodka

        self.white=self.White.get()*2110
        self.flvrd=self.Flavoured.get()*1800
        self.gold=self.Gold.get()*1940
        self.ovrpf=self.Overproof.get()*1800
        self.smoky=self.Smoky.get()*1650
        self.prmm=self.Premium.get()*2600
        # Total Drinks price================================================
        self.total_rum_price=float(
            self.white+
            self.flvrd+
            self.gold+
            self.ovrpf+
            self.smoky+
            self.prmm
        ) 
        self.Rum_price.set("Rs. "+str(self.total_rum_price)) 
        self.r_tax= round((self.total_rum_price*00.36),2)
        #tax of drinks
        self.Rum_tax.set("Rs. "+str(self.r_tax))


        # For Total Bill
        self.Total_bill=float(self.total_beer_price+
                              self.total_vodka_price+
                              self.total_rum_price+
                              self.b_tax+
                              self.v_tax+
                              self.r_tax
                            )



        #Generate
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Amrit Retail\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n......................................")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n......................................")


#Bill Area
    def bill_area(self):
        #validation
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error", "Please Add Customer details")
        elif self.Beer_price.get()=="Rs. 0.0" and self.Vodka_price.get()=="Rs. 0.0" and self.Rum_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product purchase")

        else: 


        #end validation
            
            self.welcome_bill()
            #====cosmetics
            if self.Barahsin.get()!=0:
                self.txtarea.insert(END, f"\n Barahsin Beer\t\t{self.Barahsin.get()}\t\t{self.brhsin}")
            
            if self.Namaste.get()!=0:
                self.txtarea.insert(END, f"\n Namaste Beer\t\t{self.Namaste.get()}\t\t{self.nmst}")

            if self.Strong.get()!=0:
                self.txtarea.insert(END, f"\n Strong Beer\t\t{self.Strong.get()}\t\t{self.strg}")
            
            if self.Mountain.get()!=0:
                self.txtarea.insert(END, f"\n Mountain Beer\t\t{self.Mountain.get()}\t\t{self.mount}")
            
            if self.Arna.get()!=0:
                self.txtarea.insert(END, f"\n Arna Beer\t\t{self.Arna.get()}\t\t{self.arna}")

            if self.Mustang.get()!=0:
                self.txtarea.insert(END, f"\n Mustang Beer\t\t{self.Mustang.get()}\t\t{self.mustg}")

        

            #====Vodka===
            if self.A8848.get()!=0:
                self.txtarea.insert(END, f"\n 8848 Vodka\t\t{self.A8848.get()}\t\t{self.a48}")
            
            if self.Ruslan.get()!=0:
                self.txtarea.insert(END, f"\n Ruslan Vodka\t\t{self.Ruslan.get()}\t\t{self.rsln}")

            if self.Yeti.get()!=0:
                self.txtarea.insert(END, f"\n Yeti Vodka\t\t{self.Yeti.get()}\t\t{self.yeti}")
            
            if self.Highlander.get()!=0:
                self.txtarea.insert(END, f"\n Highlander\t\t{self.Wheat.get()}\t\t{self.hgld}")
            
            if self.Zurick.get()!=0:
                self.txtarea.insert(END, f"\n Zurick Vodka\t\t{self.Zurick.get()}\t\t{self.zurk}")

            if self.Smirnoff.get()!=0:
                self.txtarea.insert(END, f"\n Smirnoff Vodka\t\t{self.Smirnoff.get()}\t\t{self.smrf}")



            #====Drink
            if self.White.get()!=0:
                self.txtarea.insert(END, f"\n White Rum\t\t{self.White.get()}\t\t{self.white}")
            
            if self.Flavoured.get()!=0:
                self.txtarea.insert(END, f"\n Flavoured Rum\t\t{self.Flavoured.get()}\t\t{self.flvrd}")

            if self.Gold.get()!=0:
                self.txtarea.insert(END, f"\n Gold Rum\t\t{self.Gold.get()}\t\t{self.gold}")
            
            if self.Overproof.get()!=0:
                self.txtarea.insert(END, f"\n OverProof Rum\t\t{self.Overproof.get()}\t\t{self.ovrpf}")
            
            if self.Smoky.get()!=0:
                self.txtarea.insert(END, f"\n Smoky Rum\t\t{self.Smoky.get()}\t\t{self.smoky}")

            if self.Premium.get()!=0:
                self.txtarea.insert(END, f"\n Premium Rum\t\t{self.Premium.get()}\t\t{self.prmm}")


            
            self.txtarea.insert(END, f"\n--------------------------------------")
            # beer tax
            if self.Beer_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END, f"\n Beer Tax\t\t\t{self.Beer_tax.get()}")
            # vodka tax
            if self.Vodka_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Vodka Tax\t\t\t{self.Vodka_tax.get()}")
            #  rum tax
            if self.Rum_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Rum Tax\t\t\t{self.Rum_tax.get()}")

            #For Total all Bill + Tax
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.txtarea.insert(END, f"\n Your Total Bill is :\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            #bill save txt
            self.save_bill()
            
    
           

    def save_bill(self):
        op= messagebox.askyesno("Save Bill","Do you want to save Bill?")
        if op>0:

            self.bill_data=self.txtarea.get('1.0', END)
            f1=open("CustomerBills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close
            messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} Bill saved Successfully!")
        else:
            return
    #find bill
    def find_bill(self):
        present="no"
        for i in os.listdir("CustomerBills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"CustomerBills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:    
                    self.txtarea.insert(END, d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error", "Invalid Bill No.")

    #end find bill
    #start clear button=======
    def clear_data(self):

        op= messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:


            #======================Beer variable====================
            self.Barahsin.set(0)
            self.Namaste.set(0)
            self.Strong.set(0)
            self.Mountain.set(0)
            self.Arna.set(0)
            self.Mustang.set(0)

           #=======================Vodka variable====================
            self.A8848.set(0)
            self.Ruslan_oil.set(0)
            self.Yeti.set(0)
            self.Highlander.set(0)
            self.Zurick.set(0)
            self.Smirnoff.set(0)

        #======================= ===Rum variable====================
            self.White.set(0)
            self.Flavoured.set(0)
            self.Gold.set(0)
            self.Overproof.set(0)
            self.Smoky.set(0)
            self.Premium.set(0)

        #=======================Total Product price====================
            self.Beer_price.set("")
            self.Vodka_price.set("")
            self.Rum_price.set("")


            self.Beer_tax.set("")
            self.Vodka_tax.set("")
            self.Rum_tax.set("")


        #===========cumtomer===================

            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x= random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # for exit button
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit?")
        if op>0:
          self.root.destroy()
        
          




            

root=Tk()
obj = Bill_App(root)
root.mainloop()