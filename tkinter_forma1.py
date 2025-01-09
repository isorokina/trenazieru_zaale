
import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('trenazieru_zale.db')
cursor = conn.cursor()

   
def sportistu_logs():
    def pievienot_sportistu():
        messagebox.showinfo("Pievienot sportistu", "Šeit tiks pievienots sportists.")

    def meklēt_sportistu():
        messagebox.showinfo("Meklēt sportistu", "Šeit varēs meklēt sportistu.")

    def dzēst_sportistu():
        messagebox.showinfo("Dzēst sportistu", "Šeit varēs dzēst sportistu.")

    sportisti_logs = tk.Toplevel()
    sportisti_logs.title("Sportistu pārvaldība")
    sportisti_logs.geometry("300x250")

    pievienot_btn = tk.Button(sportisti_logs, text="Pievienot sportistu", command=pievienot_sportistu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(sportisti_logs, text="Meklēt sportistu", command=meklēt_sportistu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(sportisti_logs, text="Dzēst sportistu", command=dzēst_sportistu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(sportisti_logs, text="Iziet", command=sportisti_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)

def izveidot_galveno_logu():
    def sportisti_poga():
        sportistu_logs()
        #messagebox.showinfo("Sportisti", "Atvērta sportistu pārvaldība.")

    def treneri_poga():
        messagebox.showinfo("Treneri", "Atvērta treneru pārvaldība.")

    def apmeklejumi_poga():
        messagebox.showinfo("Apmeklējumi", "Atvērta apmeklējumu pārvaldība.")

    logs = tk.Tk()
    logs.title("Trenažieru zāles pārvaldība")
    logs.geometry("300x200")

    sportisti_btn = tk.Button(logs, text="Sportisti", command=sportisti_poga, width=20, height=2, bg="lightblue")
    sportisti_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Treneri", command=treneri_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Apmeklējumi", command=apmeklejumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()

izveidot_galveno_logu()


