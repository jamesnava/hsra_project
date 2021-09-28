import pyodbc
class Conexion(object):
	def __init__(self, servidor,bd,user,password):
		self.servidor=servidor
		self.baseDatos=bd
		self.user=user
		self.password=password
		self.puntero=None
		self.conn=None
	def ejecutar_conn(self):
		self.conn=pyodbc.connect('DRIVER={SQL Server}; SERVER='+self.servidor+';DATABASE='+self.baseDatos+';UID'+self.user+';PWD'+self.password)
	def get_cursor(self):
		self.puntero=self.conn.cursor()
		return self.puntero