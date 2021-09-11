import time
import os
import text_editor as te
os.chdir(os.path.dirname(__file__))
class animated_word:
	def __init__(this,word):
		this.word=word
	def dissapear_word(this):
		i=len(this.word)-1
		while i>=0:
			os.system('cls')
			j=0
			while j<=i:
				print(this.word[j])
				j+=1
			time.sleep(0.0001)
			i-=1
		else:
			os.system('cls')
	def show_word(this,inp=False):
		for wr in this.word:
			time.sleep(0.005)
			print(wr)
		if inp==True:
			input()		

def check_word(isi):
	cek="! @ # $ % ^ & * ( ) + = { } [ ] \\ | : ; \" ' < > , . ? / ~ `"
	cek=cek.split(" ")
	ada_data=False
	for ck in cek:
 		ada=isi.find(ck)
 		if(ada>0):
 			ada_data=True
 			break
	if ada_data==False:
 		ada=isi.find(" ")
 		if(ada>0):
 			ada_data=True
	return ada_data

class java_compiler:
	def __init__(this):
		this.te=te
		this.currentfile=""
	def delete_current_project(this):
		if(this.currentfile!=""):
			tanya=input("Hapus Proyek Ini ?[Y/T] :")
			if((tanya=="y")or(tanya=="Y")):
				os.system("del /q \""+this.currentfile+"\"")
				os.system("rmdir \""+this.currentfile+"\"")
				print("Proyek sudah dihapus")
				this.currentfile=""
		else:
			print("tidak ada proyek aktif")
		input()
	def list_project(this):
		os.system("cls")
		daftar=os.listdir()
		isi_real=[]
		isi_kalimat=[]
		for df in daftar:
			if(os.path.exists(df+"/"+df+".java")):
				isi_real.append(df)
		if(len(isi_real)==0):
			isi_kalimat.append("Tidak ada project java tersedia")
		else:
			isi_kalimat.append("Proyek java yang tersedia :")
			for ir in isi_real:
				isi_kalimat.append("[+]"+ir)
		aw=animated_word(isi_kalimat)
		aw.show_word(inp=True)
		aw.dissapear_word()
	def set_file(this):
		os.system("cls")
		daftar=os.listdir()
		isi_real=[]
		isi_kalimat=[]
		for df in daftar:
			if(os.path.exists(df+"/"+df+".java")):
				isi_real.append(df)
		if(len(isi_real)==0):
			isi_kalimat.append("Tidak ada project java tersedia")
		else:
			isi_kalimat.append("Project Java Yang Tersedia")
			for ir in isi_real:
				isi_kalimat.append("[+]"+ir)
		aw=animated_word(isi_kalimat)
		aw.show_word()
		file=input("Masukkan nama proyek :")
		cek=os.path.exists(file+"/"+file+".java")
		if(cek):
			this.currentfile=file
			aw.dissapear_word()
		else:
			print("File tidak ada")
			aw.dissapear_word()
			input()
	def run_java(this):
		perintah="javac \""+this.currentfile+"/"+this.currentfile+".java\""
		os.system(perintah)
		perintah="java \""+this.currentfile+"/"+this.currentfile+".java\""
		os.system(perintah)
		input()
	def write_java(this):
		proyekbaru=input("Masukkan nama file java baru ")
		ada_kata=check_word(proyekbaru)
		if(ada_kata):
			print("nama proyek tidak boleh memakai karakter !@#$, spasi dan sebagainya")
		else:
			if(proyekbaru!=""):
				try:
					if(os.path.exists(proyekbaru)):
						print("Proyek sudah ada")
					else:
						this.currentfile=proyekbaru
						isi="public class "+this.currentfile+"{\n"
						isi=isi+" public static void main (String args[]){"
						isi=isi+"\n   ///tulis kode disini \n"
						isi=isi+" }\n}"
						os.system("mkdir \""+this.currentfile+"\"")
						namafile=this.currentfile+"/"+this.currentfile+".java"
						fd=open(namafile,"w+")
						fd.write(isi)
						fd.close()
						perintah="javac \""+namafile+"\""
						os.system(perintah)
						print("File java selesai dibuat")
				except:
					print("Terjadi Kesalahan")
			else:
				print("Proyek kosong")
		input()
	def edit_file(this):
		if(this.currentfile!=""):
			namafile=this.currentfile+"/"+this.currentfile+".java"
			try:
				baca_file=open(namafile,"r")
				te.Text_editor(baca_file.read(),namafile)
			except:
				print("file tidak ada")

os.system("cls")
pil=""
je=java_compiler()
word_begin=[
"==================================================",
"| |     <--> |    | |      | <---- -----         |",
"| |     |  | |    | |      | |       |           |",
"| |     <--| |    | |      | <----   |           |",
"| |     |  | | /\\ | |      | |       |           |",
"| <---- |  | |/  \\| <----  | <----   |           |",
"|                                                |",
"| <----> <----> <---->       | <---- <---- ----- |",
"| |    | |    | |    |       | |     |       |   |",
"| <----> <----> |    |       | <---- |       |   |",
"| |      |\\     |    |  |    | |     |       |   |",
"| |      | \\    |    |  |    | |     |       |   |",
"| |      |  \\   <---->  <----> <---- <----   |   |",
"|                                                |",
"|  Github : https://github.com/Cypher999/        |",
"|  Name   : Sandi M. Irvan                       |",
"|  Press Enter                                   |",
"==================================================",
]
titlescreen=animated_word(word_begin)
titlescreen.show_word(True)
titlescreen.dissapear_word()
while pil!="X" and pil!="x":
	os.system("cls")
	word_menu=[
	"Java compiler with python",
	"Proyek saat ini :"+je.currentfile,
	"\n\nMasukkan pilihan :",
	"[1] Buat File Java",
	"[2] Set File Proyek Yang Dipakai",
	"[3] Edit file Proyek",
	"[4] Eksekusi Proyek",
	"[5] Hapus Proyek",
	"[6] Lihat Proyek Yang Tersedia",
	"[X] Keluar"]
	menu_screen=animated_word(word_menu)
	menu_screen.show_word()
	pil=input("Pilihan anda : ")
	if(pil=="1"):
		menu_screen.dissapear_word()
		je.write_java()
	elif(pil=="2"):
		menu_screen.dissapear_word()
		je.set_file()
	elif(pil=="3"):
		menu_screen.dissapear_word()
		je.edit_file()
	elif(pil=="4"):
		menu_screen.dissapear_word()
		je.run_java()
	elif(pil=="5"):
		menu_screen.dissapear_word()
		je.delete_current_project()
	elif(pil=="6"):
		menu_screen.dissapear_word()
		je.list_project()
