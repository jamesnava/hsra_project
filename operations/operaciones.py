import sys
from tkinter import messagebox
sys.path.append('..')
from queries import consulta
class Operaciones(object):
	
	def __init__(self):
		self.objeto_consulta=None
		self.objeto_consulta=consulta.Consultar()
	
	def add_people(self,dni,nombre,apellidop,apellidom):
		self.objeto_consulta.get_puntero('nodo','resolucion','sa','1234')
		valor=self.objeto_consulta.insert_people(dni,nombre,apellidop,apellidom)
		if valor:
			messagebox.showinfo("Alerta", "Se Insertó Correctamente")
		else:
			messagebox.showinfo('Alerta','Error al Insertar')