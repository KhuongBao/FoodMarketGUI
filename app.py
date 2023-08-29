import json
import random
from tkinter import *
import time

def chat():
    global count
    count=0
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    window = Tk()
    window.geometry('800x600')

    window.title("Chat")
    window.resizable(width=False, height=False)
    window.configure(width=470, height=550, bg=BG_COLOR)

    # head label
    head_label = Label(window, bg=BG_COLOR, fg=TEXT_COLOR,
                       text="Welcome", font=FONT_BOLD, pady=10)
    head_label.place(relwidth=1)

    # tiny divider
    line = Label(window, width=450, bg=BG_GRAY)
    line.place(relwidth=1, rely=0.07, relheight=0.012)

    # text widget
    text_widget = Text(window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
    text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
    text_widget.configure(cursor="arrow", state=DISABLED)

    # scroll bar
    scrollbar = Scrollbar(text_widget)
    scrollbar.place(relheight=1, relx=0.974)
    scrollbar.configure(command=text_widget.yview)

    # bottom label
    bottom_label = Label(window, bg=BG_GRAY, height=80)
    bottom_label.place(relwidth=1, rely=0.825)

    def get_response():
        global count
        with open('intents.json', 'rb') as f:
            file = json.load(f)['intents']
        if count==0:
            for fl in file:
                if fl['tag']=='greeting':
                    response=random.choice(fl['responses'])
                    count += 1
                    return response
        if count==1:
            for fl in file:
                if fl['tag']=='confirm':
                    response=random.choice(fl['responses'])
                    count += 1
                    return response
        if count==2:
            for fl in file:
                if fl['tag']=='goodbye':
                    response=random.choice(fl['responses'])
                    count += 1
                    return response

    def _insert_message(msg, sender):
        if not msg:
            return
        msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg1)
        text_widget.configure(state=DISABLED)
        time.sleep(0.3)

        text_widget.see(END)

        msg2 = get_response()+"\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg2)
        text_widget.configure(state=DISABLED)

        text_widget.see(END)

    def _on_enter_pressed():
        msg = msg_entry.get()
        _insert_message(msg, "You")

    # message entry box
    msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
    msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
    msg_entry.focus()
    msg_entry.bind("<Return>", _on_enter_pressed())

    # send button
    send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                         command=lambda: _on_enter_pressed())
    send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


    window.mainloop()