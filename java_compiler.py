import os
import text_editor as te

class java_compiler:
	def __init__(this):
		this.te=te
		this.currentfile=""
	def delete_current_project(this):
		if(this.currentfile!=""):
			tanya=input("Hapus Proyek Ini ?[Y/T] :")
			if((tanya=="y")or(tanya=="Y")):
				os.system("del /q "+this.currentfile)
				os.system("rmdir "+this.currentfile)
				print("Proyek sudah dihapus")
				this.currentfile=""
		else:
			print("tidak ada proyek aktif")
		input()
	def list_project(this):
		os.system("cls")
		daftar=os.listdir()
		isi_real=[]
		for df in daftar:
			if(os.path.exists(df+"/"+df+".java")):
				isi_real.append(df)
		if(len(isi_real)==0):
			print("tidak ada proyek java")
		else:
			print("Proyek java yang tersedia :")
			for ir in isi_real:
				print("[+]"+ir)
		input()
	def set_file(this):
		os.system("cls")
		daftar=os.listdir()
		isi_real=[]
		for df in daftar:
			if(os.path.exists(df+"/"+df+".java")):
				isi_real.append(df)
		if(len(isi_real)==0):
			print("tidak ada proyek java")
		else:
			print("Proyek java yang tersedia :")
			for ir in isi_real:
				print("[+]"+ir)
		file=input("Masukkan nama proyek :")
		cek=os.path.exists(file+"/"+file+".java")
		if(cek):
			this.currentfile=file
		else:
			print("File tidak ada")
			input()
	def run_java(this):
		if(this.currentfile!=""):
			try:
				perintah="java "+this.currentfile+"/"+this.currentfile+".java"
				os.system(perintah)
				print("\n\neksekusi selesai")
			except:
				print("Class java tidak ditemukan")
		else:
			print("Nama class kosong")
		input()
	def write_java(this):
		proyekbaru=input("Masukkan nama file java baru ")
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
					os.system("mkdir "+this.currentfile)
					namafile=this.currentfile+"/"+this.currentfile+".java"
					fd=open(namafile,"w+")
					fd.write(isi)
					fd.close()
					perintah="javac "+namafile
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

lengkap=True
print("Mendeteksi Java")
jv=os.system("java --version")
jcv=os.system("javac --version")
if(jv!=0)or(jcv!=0):
	lengkap=False
if lengkap:
	pil=""
	je=java_compiler()
	while(pil!="X"):
		os.system("cls")
		print("Java compiler with python")
		print("Created By")
		print("-----------------------------------------------------")
		print("|   |      <----> |    | |      | <----- <------>   |")
		print("|   |      |    | |    | |      | |          |      |")
		print("|   |      <----> |    | |      | <-----     |      |")
		print("|   |      |    | | /\\ | |      | |          |      |")
		print("|   <----- |    | |/  \\| <----- | <-----     |      |")
		print()
		print("|   <----> <----> <---->      | <---- <----->       | ")
		print("|   |    | |    | |    |      | |        |          | ")
		print("|   <----> <----> |    | |    | <----    |          |")
		print("|   |      |\\\\    |    | |    | |        |          |")
		print("|   |      | \\\\   <----> <----> <----    |          |")
		print("|      Github : github.com/Cypher999/               |")
		print("-----------------------------------------------------")
		print("Proyek saat ini :"+je.currentfile)
		print("\n\nMasukkan pilihan :")
		print("[1] Buat File Java")
		print("[2] Set File Proyek Yang Dipakai")
		print("[3] Edit file Proyek")
		print("[4] Eksekusi Proyek")
		print("[5] Hapus Proyek")
		print("[6] Lihat Proyek Yang Tersedia")
		print("[X] Keluar")
		pil=input("Pilihan anda : ")
		if(pil=="1"):
			je.write_java()
		elif(pil=="2"):
			je.set_file()
		elif(pil=="3"):
			je.edit_file()
		elif(pil=="4"):
			je.run_java()
		elif(pil=="5"):
			je.delete_current_project()
		elif(pil=="6"):
			je.list_project()
else:
	print("Java atau Javac tidak terdeteksi")
	print("Silahkan install java dan jdk")
	print("Atau pastikan java dan jdk java sudah terdaftar di path environment variables")
	input()
