from tkinter import *
import json
from tkinter import ttk

works = []
with open("quotes.json") as f:
    quotes_dict = json.load(f)
    for work in quotes_dict["works"]:
        works.append(work["work_title"])


def register_quote():
    work_title = work_var.get()
    new_quote = {
        "page": int(e_page_num.get()),
        "quote": t_quote.get(0., END)
    }

    # 該当作品の検索 and 新しい引用の追加
    def sort_by_page(e):
        return e['page']

    for work in quotes_dict['works']:
        if work_title in work["work_title"]:
            work["quotes"].append(new_quote)
        work["quotes"].sort(key=sort_by_page)

    # データの書き込み
    with open("quotes.json", "w") as f:
        json.dump(quotes_dict, f, indent=2, ensure_ascii=False)

    # テキストボックスなどのリセット
    e_page_num.delete(0, END)
    t_quote.delete(0., END)


def create_w_for_new_work():
    def add_new_work():
        new_title = e.get()
        if new_title != "":
            works.append(new_title)
            new_work_dict = {
                "work_title": new_title,
                "quotes": []
            }
            quotes_dict["works"].append(new_work_dict)
            with open("quotes.json", "w") as f:
                json.dump(quotes_dict, f, indent=2, ensure_ascii=False)

            om_work_title.set_menu(works[0], *works)

            sub_window.destroy()

    sub_window = Toplevel()
    sub_window.title("Add new title")
    sub_window.geometry("300x50+120+0")

    e = Entry(sub_window)
    e.pack()

    b_submit_new_title = Button(sub_window, text="追加", command=add_new_work)
    b_submit_new_title.pack()


window = Tk()
window.config(width=300, height=400)
window.title("Quote Manager")

b_new_work = Button(text="Add New Title", command=create_w_for_new_work)

l_work_title = Label(text="Work Title: ")
l_page_num = Label(text="Page Number: ")
l_quote = Label(text="Quote: ")

work_var = StringVar(window)
work_var.set(works[0])
om_work_title = ttk.OptionMenu(window, work_var, *works)
e_page_num = Entry()
t_quote = Text()

b_submit = Button(text="Register", command=register_quote)

b_new_work.grid(row=1, column=2)
l_work_title.grid(row=1, column=0)
l_page_num.grid(row=2, column=0)
l_quote.grid(row=3, column=0)
om_work_title.grid(row=1, column=1)
e_page_num.grid(row=2, column=1)
t_quote.grid(row=3, column=1)
b_submit.grid(row=4, column=1)


window.mainloop()