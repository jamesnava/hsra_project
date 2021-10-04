from tkinter import *
from tkinter import ttk

class Login(object):
	"""docstring for Login"""
	def __init__(self):
		self.view_main=Tk()
		self.view_main.geometry('500x330+500+120')
		self.view_main.iconbitmap('../icons/libros.ico')
		self.view_main.title('Ingresar Credenciales')
		self.view_main.overrideredirect(True)
		btn_close=ttk.Button(self.view_main, text='cerrar')
		btn_close['command']=self.close
		btn_close.place(x=40,y=10)


	def ejecutar(self):
		self.view_main.mainloop()
	def close(self):
		self.view_main.destroy()
obj_login=Login()
obj_login.ejecutar()
		