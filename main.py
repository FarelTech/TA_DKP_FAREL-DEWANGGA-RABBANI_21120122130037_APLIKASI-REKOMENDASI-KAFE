import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import database
import tkinter as tk

#---------------------------------------- Function Aplikasi ---------------------------------------------------------------------------------------------------------------

def search_kafe():
    selection = variable6.get()
    if selection != 'Select':
        row = database.search_kafe(selection)
        nama_hasil_label.configure(text=row[0])
        kenyamanan_hasil_label.configure(text=row[1])
        harga_hasil_label.configure(text=row[2])
        pelayanan_hasil_label.configure(text=row[3])
        kopi_hasil_label.configure(text=row[4])
        rec_hasil_label.configure(text=row[5])
    else:
        messagebox.showerror('Error', 'Pilih Kafe!')

def insert_nama_options():
    nama = database.fetch_all_nama()
    search_options.configure(values=nama)

def new_kafe():
    nama_entry.delete(0, END)
    variable1.set('Biasa Saja')
    variable2.set('')
    variable3.set('Standar')
    variable4.set('Biasa')
    variable5.set('')

def submit_kafe():
    nama = nama_entry.get()
    kenyamanan = variable1.get()
    harga = variable2.get()
    pelayanan = variable3.get()
    kopi = variable4.get()
    rec = variable5.get()
    try:
        if not (nama and kenyamanan and harga and pelayanan and kopi and rec):
            messagebox.showerror('Error', 'Mohon Masukkan Semua Datanya.')
        elif database.nama_exists(nama):
            messagebox.showerror('Error', 'Kafe Sudah Ada Rating.')
        else:
            database.insert_kafe(nama, kenyamanan, harga, pelayanan, kopi, rec)
            insert_nama_options()
            messagebox.showinfo('Success', 'Kafe Berhasil Diberi Rating.')
    except:
            messagebox.showerror('Error', 'Error')
            
            
#---------------------------------------- window GUI & Class ---------------------------------------------------------------------------------------------------------------
class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.title('Aplikasi Rekomendasi Kafe')
        self.master.geometry('700x600')
        self.master.config(bg='#131314')
        self.master.resizable(False,False)
        
if __name__ == '__main__' :
    app = ctk.CTk()
    gui = App(master = app)

font1 = ('Helvetica', 30, 'bold')
font2 = ('Helvetica', 20, 'bold')
font3 = ('Helvetica', 15, 'bold')


#---------------------------------------- Frame GUI ---------------------------------------------------------------------------------------------------------------

title_label = ctk.CTkLabel(app, font= font1, text= "Masukkan Rekomendasi Kafe:", text_color= '#fff', bg_color= '#131314')
title_label.place(x=25, y=20)

frame1 = ctk.CTkFrame(app, bg_color='#131314', fg_color= '#292933', corner_radius= 10, border_width= 2, border_color= '#e36254', width= 650, height= 230)
frame1.place(x= 25, y= 70)

frame2 = ctk.CTkFrame(app, bg_color='#131314', fg_color= '#292933', corner_radius= 10, border_width= 2, border_color= '#e36254', width= 650, height= 200)
frame2.place(x= 25, y= 350)

#---------------------------------------- frame 1 GUI -------------------------------------------------------------------------------------------------------------

nama_label = ctk.CTkLabel(frame1, font= font2, text= 'Nama Kafe?', text_color= '#fff', bg_color='#292933')
nama_label.place(x=50, y=15)

nama_entry = ctk.CTkEntry(frame1, font= font3, text_color= '#000', fg_color= '#fff', border_color= '#fff', border_width= 2, width= 150)
nama_entry.place(x=50, y=45)

kenyamanan_label = ctk.CTkLabel(frame1, font= font2, text= 'Kenyamanan?', text_color= '#fff', bg_color='#292933')
kenyamanan_label.place(x=245, y=15)

variable1 = StringVar()
options = ['Sangat Tidak Nyaman', 'Tidak Nyaman', 'Biasa Saja', 'Nyaman', 'Sangat Nyaman']

kenyamanan_options = ctk.CTkComboBox(frame1, font= font3, text_color= '#000', fg_color= '#fff', dropdown_hover_color= '#fff', button_color= '#fff', border_color= '#fff', width= 150, variable= variable1, values= options, state= 'readonly')
kenyamanan_options.set('Biasa Saja')
kenyamanan_options.place(x= 245, y= 45)

harga_label = ctk.CTkLabel(frame1, font= font2, text= 'Harga?', text_color= '#fff', bg_color='#292933')
harga_label.place(x=445, y=15)

variable2 = StringVar()
rb1 = ctk.CTkRadioButton(frame1, text= 'Murah', fg_color= '#fff', hover_color= '#fff', font= font3, variable= variable2, value= 'Murah')
rb2 = ctk.CTkRadioButton(frame1, text= 'Mahal', fg_color= '#fff', hover_color= '#fff', font= font3, variable= variable2, value= 'Mahal')
rb1.place(x=445, y= 45)
rb2.place(x=525, y=45)

pelayanan_label = ctk.CTkLabel(frame1, font= font2, text= 'Pelayanan?', text_color= '#fff', bg_color='#292933')
pelayanan_label.place(x=50, y=90)

variable3 = StringVar()
options = ['Sangat Tidak Baik', 'Tidak Baik', 'Standar', 'Baik', 'Sangat Baik']

pelayanan_options = ctk.CTkComboBox(frame1, font= font3, text_color= '#000', fg_color= '#fff', dropdown_hover_color= '#fff', button_color= '#fff', border_color= '#fff', width= 150, variable= variable3, values= options, state= 'readonly')
pelayanan_options.set('Standar')
pelayanan_options.place(x= 50, y= 125)

kopi_label = ctk.CTkLabel(frame1, font= font2, text= 'Kopi?', text_color= '#fff', bg_color='#292933')
kopi_label.place(x=245, y=90)

variable4 = StringVar()
options = ['Tidak Enak', 'Biasa', 'Enak']

kopi_options = ctk.CTkComboBox(frame1, font= font3, text_color= '#000', fg_color= '#fff', dropdown_hover_color= '#fff', button_color= '#fff', border_color= '#fff', width= 150, variable= variable4, values= options, state= 'readonly')
kopi_options.set('Biasa')
kopi_options.place(x= 245, y= 125)

rec_label = ctk.CTkLabel(frame1, font= font2, text= 'Recommended?', text_color= '#fff', bg_color='#292933')
rec_label.place(x=445, y=90)

variable5 = StringVar()
rb3 = ctk.CTkRadioButton(frame1, text= 'Iya!', fg_color= '#fff', hover_color= '#fff', font= font3, variable= variable5, value= 'Iya!')
rb4 = ctk.CTkRadioButton(frame1, text= 'Tidak.', fg_color= '#fff', hover_color= '#fff', font= font3, variable= variable5, value= 'Tidak.')
rb3.place(x=445, y= 125)
rb4.place(x=525, y=125)

submit_button = ctk.CTkButton(frame1, font= font2, command= submit_kafe, text_color= '#fff', text= 'Submit', fg_color= "#bd2211", hover_color= '#590f07', bg_color= '#292933', cursor = 'hand2', corner_radius= 5, width=100)
submit_button.place(x= 200, y=170)

clear_button = ctk.CTkButton(frame1, font= font2, command= new_kafe, text_color= '#fff', text= 'Clear', fg_color= "#000", hover_color= '#666', bg_color= '#292933', cursor = 'hand2', corner_radius= 5, width=100)
clear_button.place(x= 330, y=170)

#---------------------------------------- frame 2 GUI -------------------------------------------------------------------------------------------------------------

search_label = ctk.CTkLabel(app, font= font1, text= 'Search Kafe:', text_color= '#fff', bg_color='#131314')
search_label.place(x=25, y=312)

variable6 = StringVar()

search_options = ctk.CTkComboBox(app, font= font3, text_color= '#000', fg_color= '#fff', dropdown_hover_color= '#fff', button_color= '#fff', border_color= '#fff', width= 150, variable= variable6, state= 'readonly')
search_options.set('Pilih')
search_options.place(x= 250, y= 312)

search_button = ctk.CTkButton(app, font= font2, command = search_kafe, text_color= '#fff', text= 'Search', fg_color= "#bd2211", hover_color= '#590f07', bg_color= '#131314', cursor = 'hand2', corner_radius= 5, width=100)
search_button.place(x= 420, y=312)

nama_label = ctk.CTkLabel(frame2, font= font2, text= 'Nama Kafe:', text_color= '#fff', bg_color='#292933')
nama_label.place(x=50, y=15)

nama_hasil_label = ctk.CTkLabel(frame2, font= font2, text= '', text_color= '#22ab22', bg_color='#292933')
nama_hasil_label.place(x=50, y=45)

kenyamanan_label = ctk.CTkLabel(frame2, font= font2, text= 'Kenyamanan:', text_color= '#fff', bg_color='#292933')
kenyamanan_label.place(x=245, y=15)

kenyamanan_hasil_label = ctk.CTkLabel(frame2, font= font2, text= '', text_color= '#22ab22', bg_color='#292933')
kenyamanan_hasil_label.place(x=245, y=45)

harga_label = ctk.CTkLabel(frame2, font= font2, text= 'Harga:', text_color= '#fff', bg_color='#292933')
harga_label.place(x=445, y=15)

harga_hasil_label = ctk.CTkLabel(frame2, font= font2, text= '', text_color= '#22ab22', bg_color='#292933')
harga_hasil_label.place(x=445, y=45)

pelayanan_label = ctk.CTkLabel(frame2, font= font2, text= 'Pelayanan:', text_color= '#fff', bg_color='#292933')
pelayanan_label.place(x=50, y=90)

pelayanan_hasil_label = ctk.CTkLabel(frame2, font= font2, text= '', text_color= '#22ab22', bg_color='#292933')
pelayanan_hasil_label.place(x=50, y=125)

kopi_label = ctk.CTkLabel(frame2, font= font2, text= 'Kopi:', text_color= '#fff', bg_color='#292933')
kopi_label.place(x=245, y=90)

kopi_hasil_label = ctk.CTkLabel(frame2, font= font2, text= '', text_color= '#22ab22', bg_color='#292933')
kopi_hasil_label.place(x=245, y=125)

rec_label = ctk.CTkLabel(frame2, font= font2, text= 'Recommended:', text_color= '#fff', bg_color='#292933')
rec_label.place(x=445, y=90)

rec_hasil_label = ctk.CTkLabel(frame2, font= font2, text= '', text_color= '#22ab22', bg_color='#292933')
rec_hasil_label.place(x=445, y=125)

insert_nama_options()

pass
app.mainloop()
