from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
from tkinter import messagebox as msg
import os

class Text_editor:
	def __init__(this,text,path):
		this.win=Tk()
		this.win.geometry("1000x700")
		this.win.title(path)
		this.namafile=path
		this.cmd_simpan=Button(this.win,text="Simpan",command=this.save_text)
		this.cmd_del=Button(this.win,text="Hapus",command=this.delete_text)
		this.txt=Text(this.win,width=100,height=40)
		this.txt.insert(END,text)

		this.txt.grid(column=0,row=0,rows=2)
		this.cmd_simpan.grid(column=2,row=0)
		this.cmd_del.grid(column=2,row=1)
		
		this.win.mainloop()
	def save_text(this):
		isi_teks=this.txt.get("1.0",END)
		fl=open(this.namafile,"w")
		fl.write(isi_teks)
		fl.close()
		perintah="javac "+this.namafile
		os.system(perintah)
		msg.showinfo("pesan","file disimpan")
	def delete_text(this):
		tanya=msg.askquestion("pesan","hapus teks ?")
		if(tanya=="yes"):
			this.txt.delete("1.0",END)