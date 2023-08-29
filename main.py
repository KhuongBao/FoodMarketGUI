from tkinter import*
from tkinter import messagebox
import random
from app import chat
import json

total_listing=0
total_bought=0
log=''
disc=0
check=False
def boot():
    global window, bg, img
    window = Tk()
    window.overrideredirect(False)
    window.geometry("1440x900")
    window.title('GUI')

    img = [
        PhotoImage(file='resources/default.png'),
        PhotoImage(file='resources/main.png'),
        PhotoImage(file='resources/login.png'),
        PhotoImage(file='resources/register.png'),
        PhotoImage(file='resources/menu.png'),
        PhotoImage(file='resources/settings.png'),
        PhotoImage(file='resources/sell.png'),
        PhotoImage(file='resources/sell2.png'),
        PhotoImage(file='resources/mail.png'),
        PhotoImage(file='resources/info.png'),
        PhotoImage(file='resources/log.png'),
        PhotoImage(file='resources/buy.png'),
        PhotoImage(file='resources/gethelp.png'),
        PhotoImage(file='resources/map.png'),
        PhotoImage(file='resources/sellmenu2.png'),
        PhotoImage(file='resources/admin_register.png')
    ]

    bg = Canvas(window, width=1440, height=900, highlightthickness=0)
    bg.pack(fill="both", expand=True)

    startmenu()
    window.mainloop()

def remove():
    for widget in window.place_slaves():
        widget.destroy()


def startmenu():

    def store_login():
        remove()

        bg.create_image(720, 450, image=img[15], anchor=CENTER)

        market_entry = Entry(window)
        market_entry.place(relx=0.352, rely=0.19, height=30, width=500)

        pass_entry = Entry(window)
        pass_entry.place(relx=0.352, rely=0.28, height=30, width=500)

        address_entry = Entry(window)
        address_entry.place(relx=0.352, rely=0.38, height=30, width=500)

        email_entry = Entry(window)
        email_entry.place(relx=0.352, rely=0.475, height=30, width=500)

        phone_entry = Entry(window)
        phone_entry.place(relx=0.352, rely=0.565, height=30, width=500)




        def login_get():
            global store_name
            store_name = market_entry.get()
            password = pass_entry.get()
            address = address_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()

            if len(store_name) != 0 and len(password) != 0 and len(address) != 0 and len(email) != 0 and len(phone) != 0:
                messagebox.showinfo("Success", "Logged-in successfully")
                remove()
                bg.create_image(720, 450, image=img[0], anchor=CENTER)

                def get_disc(amount):
                    global disc, check
                    disc=amount
                    check=False
                    messagebox.showinfo("Success", "Discount applied!")
                    startmenu()

                disc1=Button(window, text="10%", font=("Times New Roman", 50), command= lambda : get_disc(10))
                disc1.place(relx=0.22, rely=0.2)
                disc2 = Button(window, text="25%", font=("Times New Roman", 50), command= lambda : get_disc(25))
                disc2.place(relx=0.65, rely=0.2)
                disc3 = Button(window, text="30%", font=("Times New Roman", 50), command= lambda : get_disc(30))
                disc3.place(relx=0.22, rely=0.65)
                disc4 = Button(window, text="50%", font=("Times New Roman", 50), command= lambda : get_disc(50))
                disc4.place(relx=0.65, rely=0.65)

            else:
                messagebox.showwarning("Error", "Missing credentials")

        lg_button = Button(window, text="ログイン", font=("Times New Roman", 18), command=login_get)
        lg_button.place(relx=0.48, rely=0.705)
        changeOnHover(lg_button, "spring green", "white")

        back_button_menu = Button(window, text='戻る', font=("Times New Roman", 20), command=startmenu, fg='red')
        back_button_menu.place(relx=0.9, rely=0.03)
        changeOnHover(back_button_menu, "pink", "white")

    remove()

    bg.create_image(720, 450, image=img[1], anchor=CENTER)

    login_button = Button(window, text="ログイン", font=("Times New Roman", 18), command=login, height=2, width=20,borderwidth=0)
    login_button.place(relx=0.4, rely=0.5)
    changeOnHover(login_button, "spring green", "white")

    register_button = Button(window, text="アカウント登録", font=("Times New Roman", 18), command=register, height=2,width=20, borderwidth=0)
    register_button.place(relx=0.4, rely=0.6)
    changeOnHover(register_button, "spring green", "white")

    store_login=Button(window, text="Store login", font=("Times New Roman", 18), command=store_login, height=2, width=20,borderwidth=0)
    store_login.place(relx=0.4, rely=0.7)
    changeOnHover(store_login, "spring green", "white")


def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def mainmenu():
    global check, store_name
    remove()
    bg.create_image(720, 450, image=img[4])

    settings_button=Button(window,text="設定",font=(10), width=25, height=3, command=settings)
    settings_button.place(relx=0.83, rely=0.5)
    changeOnHover(settings_button, "pink", "white")

    info_button=Button(window,text="プライバシーポリシー",font=(10), width=25, height=3, command=info)
    info_button.place(relx=0.83, rely=0.75)
    changeOnHover(info_button, "pink", "white")

    cart_button=Button(window,text="注文履歴",font=(10), width=25, height=3, command=cart)
    cart_button.place(relx=0.02, rely=0.5)
    changeOnHover(cart_button, "pink", "white")

    mail_button=Button(window,text="メール",font=(10), width=25, height=3, command=mail)
    mail_button.place(relx=0.02, rely=0.75)
    changeOnHover(mail_button, "pink", "white")

    shop_button=Button(window,text="カート",font=(10), width=30, height=3, command=buy)
    shop_button.place(relx=0.28, rely=0.265)
    changeOnHover(shop_button, "pink", "white")

    donate_button=Button(window,text="商品",font=(10), width=30, height=3, command=sell)
    donate_button.place(relx=0.56, rely=0.265)
    changeOnHover(donate_button, "pink", "white")

    map_button=Button(window,text="マップ",font=(10), width=30, height=3, command=map)
    map_button.place(relx=0.42, rely=0.9)
    changeOnHover(donate_button, "pink", "white")

    back_button_menu=Button(window, text='戻る', font=(30), command=startmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

    if disc!=0 and check!=True:
        messagebox.showinfo("Discount", store_name+" item are "+str(disc)+"% off")
        check=True

def map():
    remove()

    bg.create_image(720, 450, image=img[13])

    names=["Tsuro Kamiyo", "Kyara Iwahori", "Enishi Ichioka", "Chuugou Ishimura", "Keigaku Nakagawa", "Uraru Yawata", "Sayou Hosoda", "Hiyuto Ono", "Tameemon Goto", "Uoka Yogi", "Sakuhi Yuki", "Mauka Hasegawa"]
    random_names=random.sample(names, 4)
    name1 = random_names[0]
    name2 = random_names[1]
    name3 = random_names[2]
    name4 = random_names[3]

    with open('food.json', 'rb') as f:
        file=json.load(f)["food"]
    food=[]
    for f in file:
        for product in f["product"]:
            food.append(product)
    random_food=random.sample(food, 4)
    product1 = random_food[0]
    product2 = random_food[1]
    product3 = random_food[2]
    product4 = random_food[3]

    def add_product(product):
        global log
        log+=product+" x 1\n"
        messagebox.showinfo("Success", "Item added to cart!")


    def button_hover1(e):
        pin1["bg"]='white'
        status_label1.config(text=name1+'\n'+product1, bd=1)

    def button_leave1(e):
        pin1["bg"]="SystemButtonFace"
        status_label1.config(text='', bd=0)

    status_label1=Label(window, text='', font=("Times New Roman", 15) ,bd=0, relief=SUNKEN, anchor=E)
    status_label1.place(relx=0.237, rely=0.56)
    pin1=Button(window, text="      ", font=("Times New Roman", 15), command=lambda : add_product(product1))
    pin1.place(relx=0.237, rely=0.52)
    pin1.bind("<Enter>", button_hover1)
    pin1.bind("<Leave>", button_leave1)

    def button_hover2(e):
        pin2["bg"]='white'
        status_label2.config(text=name2+'\n'+product2, bd=1)

    def button_leave2(e):
        pin2["bg"]="SystemButtonFace"
        status_label2.config(text='', bd=0)

    status_label2=Label(window, text='', font=("Times New Roman", 15) ,bd=0, relief=SUNKEN, anchor=E)
    status_label2.place(relx=0.375, rely=0.67)
    pin2=Button(window, text="      ", font=("Times New Roman", 15), command=lambda : add_product(product2))
    pin2.place(relx=0.375, rely=0.63)
    pin2.bind("<Enter>", button_hover2)
    pin2.bind("<Leave>", button_leave2)

    def button_hover3(e):
        pin3["bg"]='white'
        status_label3.config(text=name3+'\n'+product3, bd=1)

    def button_leave3(e):
        pin3["bg"]="SystemButtonFace"
        status_label3.config(text='', bd=0)

    status_label3=Label(window, text='', font=("Times New Roman", 15) ,bd=0, relief=SUNKEN, anchor=E)
    status_label3.place(relx=0.57, rely=0.39)
    pin3=Button(window, text="      ", font=("Times New Roman", 15), command=lambda : add_product(product3))
    pin3.place(relx=0.57, rely=0.35)
    pin3.bind("<Enter>", button_hover3)
    pin3.bind("<Leave>", button_leave3)

    def button_hover4(e):
        pin4["bg"]='white'
        status_label4.config(text=name4+'\n'+product4, bd=1)

    def button_leave4(e):
        pin4["bg"]="SystemButtonFace"
        status_label4.config(text='', bd=0)

    status_label4=Label(window, text='', font=("Times New Roman", 15) ,bd=0, relief=SUNKEN, anchor=E)
    status_label4.place(relx=0.715, rely=0.72)
    pin4=Button(window, text="      ", font=("Times New Roman", 15), command=lambda : add_product(product4))
    pin4.place(relx=0.715, rely=0.68)
    pin4.bind("<Enter>", button_hover4)
    pin4.bind("<Leave>", button_leave4)


    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

def cart():
    remove()

    bg.create_image(720, 450, image=img[10])

    box=Text(window, height=19, width=113, font=('Times New Roman', 18))
    box.config(state="normal")
    box.insert(INSERT, log)
    box.config(state="disabled")
    box.place(relx=0.03, rely=0.3)

    def clear_cart():
        global log
        log=""
        messagebox.showinfo("Success", "Items bought successfully")
        cart()

    buy_button=Button(window, text="BUY", font=("Times New Roman", 20), command=clear_cart)
    buy_button.place(relx=0.5, rely=0.9)
    changeOnHover(buy_button, "pink", "white")

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

def buy():

    def buy2(type):
        remove()
        bg.create_image(720, 450, image=img[11])

        with open("food.json", 'rb') as f:
            file=json.load(f)["food"]

        random_listing=[product for fl in file if fl["type"]==type for product in fl["product"]]

        listings=random.sample(random_listing, 4)
        listing1 = listings[0]
        listing2 = listings[1]
        listing3 = listings[2]
        listing4 = listings[3]

        quantity1 = str(random.randint(1, 10))
        quantity2 = str(random.randint(1, 10))
        quantity3 = str(random.randint(1, 10))
        quantity4 = str(random.randint(1, 10))

        buy_label1=Label(window, text='食品名: '+listing1, font=('Times New Roman', 20), bg='#647d23')
        buy_label1.place(relx=0.15, rely=0.25)
        quantity_label1=Label(window, text='数: '+quantity1, font=('Times New Roman', 20), bg='#647d23')
        quantity_label1.place(relx=0.15, rely=0.35)

        buy_label2=Label(window, text='食品名: '+listing2, font=('Times New Roman', 20), bg='#647d23')
        buy_label2.place(relx=0.58, rely=0.25)
        quantity_label2=Label(window, text='数: '+quantity2, font=('Times New Roman', 20), bg='#647d23')
        quantity_label2.place(relx=0.58, rely=0.35)


        buy_label3=Label(window, text='食品名: '+listing3, font=('Times New Roman', 20), bg='#647d23')
        buy_label3.place(relx=0.15, rely=0.65)
        quantity_label3=Label(window, text='数: '+quantity3, font=('Times New Roman', 20), bg='#647d23')
        quantity_label3.place(relx=0.15, rely=0.75)

        buy_label4=Label(window, text='食品名: '+listing4, font=('Times New Roman', 20), bg='#647d23')
        buy_label4.place(relx=0.58, rely=0.65)
        quantity_label4=Label(window, text='数: '+quantity4, font=('Times New Roman', 20), bg='#647d23')
        quantity_label4.place(relx=0.58, rely=0.75)



        def confirm_buy(item):
            global total_bought, log
            if messagebox.askquestion("", "Are you sure?") == 'yes':
                total_bought+=1
                messagebox.showinfo("Success", "Item added to cart!")
                log+=item+' x 1\n'
                mainmenu()
            else:
                pass

        buy_button1=Button(window, text='BUY', font=('Times New Roman', 20), width=25, command=lambda: confirm_buy(listing1))
        buy_button1.place(relx=0.15, rely=0.5)

        buy_button2=Button(window, text='BUY', font=('Times New Roman', 20), width=25, command=lambda: confirm_buy(listing2))
        buy_button2.place(relx=0.15, rely=0.9)

        buy_button3 = Button(window, text='BUY', font=('Times New Roman', 20), width=25, command=lambda: confirm_buy(listing3))
        buy_button3.place(relx=0.58, rely=0.5)

        buy_button4 = Button(window, text='BUY', font=('Times New Roman', 20), width=25, command=lambda: confirm_buy(listing4))
        buy_button4.place(relx=0.58, rely=0.9)

        back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=buy, fg='red')
        back_button_menu.place(relx=0.9, rely=0.03)
        changeOnHover(back_button_menu, "pink", "white")

    remove()

    bg.create_image(720, 450, image=img[14])

    veggies_button = Button(window, width=15, height=2, text="野菜", font=('Times New Roman', 18), command=lambda: buy2("fresh"))
    veggies_button.place(relx=0.05, rely=0.8)
    changeOnHover(veggies_button, "pink", "white")

    canned_button = Button(window, width=15, height=2, text="缶詰食品", font=('Times New Roman', 18), command=lambda: buy2("canned"))
    canned_button.place(relx=0.327, rely=0.8)
    changeOnHover(canned_button, "pink", "white")

    frozen_button = Button(window, width=15, height=2, text="冷凍食品", font=('Times New Roman', 18), command=lambda: buy2("frozen"))
    frozen_button.place(relx=0.605, rely=0.8)
    changeOnHover(frozen_button, "pink", "white")

    others_button = Button(window, width=15, height=15, text="他の\n種類の\n食品", font=('Times New Roman', 18), command=lambda: buy2("other"))
    others_button.place(relx=0.805, rely=0.43)
    changeOnHover(others_button, "pink", "white")

    back_button_menu = Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")


def sell():
    remove()

    bg.create_image(720, 450, image=img[14])

    def product_info():
        global productname_entry, quantity_entry
        remove()

        bg.create_image(720, 450, image=img[7])
        productname_label=Label(window, text='食品名', font=('Times New Roman', 28), bg='#66CC66')
        productname_label.place(relx=0.13, rely=0.3)

        quantity_label=Label(window, text='数', font=('Times New Roman', 28), bg='#66CC66')
        quantity_label.place(relx=0.13, rely=0.5)

        productname_entry=Entry(window)
        productname_entry.place(relx=0.33, rely=0.31, height=40, width=600)

        quantity_entry=Entry(window)
        quantity_entry.place(relx=0.33, rely=0.51, height=40, width=600)

        back_button_menu = Button(window, text='戻る', font=("Times New Roman", 20), command=sell, fg='red')
        back_button_menu.place(relx=0.9, rely=0.03)
        changeOnHover(back_button_menu, "pink", "white")

        def logs_2():
            global total_listing_temp, total_listing, time
            total_listing_temp = 0
            productname = productname_entry.get()
            quantity = quantity_entry.get()
            if len(productname) != 0 and len(quantity) != 0:
                total_listing_temp = int(quantity)
                total_listing += total_listing_temp
                messagebox.showinfo("Success", "Your item has been listed")
                mainmenu()
            else:
                messagebox.showwarning("Error", "Missing product information")

        confirm_button = Button(window, text="CONFIRM", font=("Times New Roman", 18), command=logs_2)
        confirm_button.place(relx=0.48, rely=0.905)
        changeOnHover(confirm_button, "spring green", "white")


    veggies_button=Button(window, width=15, height=2, text="野菜", font=('Times New Roman', 18), command=product_info)
    veggies_button.place(relx=0.05, rely=0.8)
    changeOnHover(veggies_button, "pink", "white")

    canned_button=Button(window, width=15, height=2, text="缶詰食品", font=('Times New Roman', 18), command=product_info)
    canned_button.place(relx=0.327, rely=0.8)
    changeOnHover(canned_button, "pink", "white")

    frozen_button=Button(window, width=15, height=2, text="冷凍食品", font=('Times New Roman', 18), command=product_info)
    frozen_button.place(relx=0.605, rely=0.8)
    changeOnHover(frozen_button, "pink", "white")

    others_button=Button(window, width=15, height=15, text="他の\n種類の\n食品", font=('Times New Roman', 18), command=product_info)
    others_button.place(relx=0.805, rely=0.43)
    changeOnHover(others_button, "pink", "white")

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

def settings():
    remove()

    bg.create_image(720, 450, image=img[5])

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

    name_label=Label(window, text=name, font=('Times New Roman', 30), bg='#647d23')
    name_label.place(relx=0.3, rely=0.18)

    email_label=Label(window, text=email, font=('Times New Roman', 30), bg='#647d23')
    email_label.place(relx=0.3, rely=0.33)

    phone_label=Label(window, text=phone, font=('Times New Roman', 30), bg='#647d23')
    phone_label.place(relx=0.3, rely=0.47)

    change_pass=Entry(window)
    change_pass.place(relx=0.7, rely=0.2, width=300, height=50)

    change_name=Entry(window)
    change_name.place(relx=0.7, rely=0.47, width=300, height=50)

    def confirm():
        global name
        name_c=change_name.get()
        pass_c=change_pass.get()
        if len(name_c)!=0 and len(pass_c)!=0:
            name=name_c
            messagebox.showinfo("Success", "Username and password changed successfully")
        elif len(name_c)!=0:
            name=name_c
            messagebox.showinfo("Success", "Username changed successfully")
        elif len(pass_c)!=0:
            messagebox.showinfo("Success", "Password changed successfully")
        else:
            messagebox.showwarning("Error", "Missing credentials")

    confirm_button=Button(window, text='CONFIRM', font=('Times New Roman', 20), command=confirm)
    confirm_button.place(relx=0.75, rely=0.6)
    changeOnHover(confirm_button, "pink", "white")

def info():
    remove()

    bg.create_image(720, 450, image=img[9], anchor=CENTER)

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

    def TOS_question():
        remove()

        bg.create_image(720, 450, image=img[0], anchor=CENTER)

        tos = Text(window, yscrollcommand=True, width=90, height=26, font=("Times New Roman", 18))
        tos.insert(INSERT, "契約条件")
        tos['state'] = 'disabled'
        tos.place(relx=0.1, rely=0.1)

        back_button=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
        back_button.place(relx=0.9, rely=0.03)
        changeOnHover(back_button, "pink", "white")

    tos_button=Button(window, width=20, height=3, text="契約条件", font=('Times New Roman', 20), command=TOS_question)
    tos_button.place(relx=0.23, rely=0.3)

    def get_help():
        remove()

        bg.create_image(720, 450, image=img[12], anchor=CENTER)

        back_button=Button(window, text='戻る', font=("Times New Roman", 20), command=mainmenu, fg='red')
        back_button.place(relx=0.9, rely=0.03)
        changeOnHover(back_button, "pink", "white")

    gethelp_button=Button(window, width=20, height=3, text="サポートセンター", font=('Times New Roman', 20), command=get_help)
    gethelp_button.place(relx=0.54, rely=0.3)

def mail():
    chat()


def login():
    remove()

    bg.create_image(720, 450, image=img[2], anchor=CENTER)

    name_entry=Entry(window)
    name_entry.place(relx=0.352, rely=0.505, height=30, width=500)

    pass_entry = Entry(window)
    pass_entry.place(relx=0.352, rely=0.605, height=30, width=500)

    def login_get():
        name = name_entry.get()
        password=pass_entry.get()
        if len(name)!=0 and len(password)!=0:
            messagebox.showinfo("Success", "Logged-in successfully")
            mainmenu()
        else:
            messagebox.showwarning("Error", "Missing credentials")

    lg_button=Button(window, text="ログイン", font=("Times New Roman", 18), command=login_get)
    lg_button.place(relx=0.48, rely=0.705)
    changeOnHover(lg_button, "spring green", "white")

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=startmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")

def TOS():
    remove()

    bg.create_image(720, 450, image=img[0], anchor=CENTER)

    tos = Text(window, yscrollcommand=True, width=90, height=26, font=("Times New Roman", 18))
    tos.insert(INSERT, "契約条件")
    tos['state'] = 'disabled'
    tos.place(relx=0.1, rely=0.1)

    check=Button(window, text="同意", font=("Times New Roman", 20), command=mainmenu)
    check.place(relx=0.53, rely=0.91)
    changeOnHover(check, "spring green", "white")

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=startmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")


def register():
    global name, email, phone
    remove()

    bg.create_image(720, 450, image=img[3], anchor=CENTER)
    pass_entry = Entry(window)
    pass_entry.place(relx=0.352, rely=0.505, height=30, width=500)

    cc_entry=Entry(window)
    cc_entry.place(relx=0.352, rely=0.605, height=30, width=500)

    email_entry=Entry(window)
    email_entry.place(relx=0.352, rely=0.705, height=30, width=500)

    phone_entry=Entry(window)
    phone_entry.place(relx=0.352, rely=0.805, height=30, width=500)

    def register_get():
        global name, email, phone, password
        name = name_entry.get()
        password=pass_entry.get()

    name_entry=Entry(window)
    name_entry.place(relx=0.352, rely=0.305, height=30, width=500)

    pass_entry = Entry(window)
    pass_entry.place(relx=0.352, rely=0.405, height=30, width=500)

    cc=cc_entry.get()
    email=email_entry.get()
    phone=phone_entry.get()
    if len(name)!=0 and len(password)!=0 and len(cc)!=0 and len(email)!=0 and len(phone)!=0:
        messagebox.showinfo("Success", "Registered successfully")
        TOS()
    else:
        messagebox.showwarning("Error", "Missing credentials")

    reg_confirm_button=Button(window, borderwidth=0, text="登録", font=("Times New Roman", 18),command=register_get)
    reg_confirm_button.place(relx=0.45, rely=0.93, height=50, width=200)
    changeOnHover(reg_confirm_button, "spring green", "white")

    back_button_menu=Button(window, text='戻る', font=("Times New Roman", 20), command=startmenu, fg='red')
    back_button_menu.place(relx=0.9, rely=0.03)
    changeOnHover(back_button_menu, "pink", "white")


if __name__=='__main__':
    boot()
