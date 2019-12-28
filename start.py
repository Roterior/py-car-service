import tkinter as tk
import mysql.connector as db
import yaml
from tkinter import ttk


class Tester:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('What is ' + self.name)


def white(event):
    print('white')


def red(event):
    print('red')


if __name__ == '__main__':
    with open("config.yml", 'r') as yml:
        cfg = yaml.safe_load(yml)
    db = db.connect(**cfg['mysql'])

    # print(db)

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM Client")

    res_arr = []
    for row in mycursor:
        print(row)
        for cell in row:
            res_arr.append(cell)

    print(res_arr)

    def show():
        # db.cursor().execute('SELECT * FROM Client')

        temp_list = [res_arr, ['Dave', '0.67', '0.67', '0.67']]
        # temp_list = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
        # temp_list.sort(key=lambda e: e[1], reverse=True)
        for (uuid, name, price, quantity) in temp_list:
            listBox.insert("", "end", values=(uuid, name, price, quantity))


    scores = tk.Tk()
    label = tk.Label(scores, text="Registered Clients", font=("Arial", 30)).grid(row=0, columnspan=3)
    # create Treeview with 3 columns
    cols = ('Position', 'Name', 'Score', 'Yes')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
    closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

    scores.mainloop()

    # main = tk.Tk()
    # app = Main(main)
    # app.pack()
    # main.title('Car Service')
    # main.geometry('650x450+300+200')
    # main.resizable(False, False)
    # main.mainloop()
    # print('gg')
    # tst = Tester('dog')
    # tst.say()
    # window = tk.Tk()
    # window.overrideredirect(True)
    # window.title("Alex App")
    # window.geometry('300x200')
    # window.mCan = Canvas(height=768, width=768)
    # window.mCan.pack()
    # btn = Button(text="Click")
    # btn.bind('<Enter>', red)
    # btn.bind('<Leave>', white)
    # btn.pack()
    # window.mainloop()
