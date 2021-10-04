import sys
sys.path.append('..')
from queries import connect
class Consultar(object):
	def __init__(self):
		self.puntero=None
	def get_people(self):
		sql='select * from persona'
		self.puntero.execute(sql)
		rows=self.puntero.fetchall()
	def insert_people(self,DNI,NOMBRE,APELLIDOP,APELLIDOM):
		sql="INSERT INTO persona (dni,nombre_pers,apellidop_pers,apellidom_pers) VALUES(?,?,?,?)"
		valor=False
		try:
			if DNI=='':
				valor=False
			else:
				self.puntero.execute(sql,DNI,NOMBRE,APELLIDOP,APELLIDOM)
				self.puntero.commit()
				valor=True
			return valor
		except Exception as e:
			valor=False
			return valor		
		
		
		
	def get_puntero(self,servidor,bd,user,password):
		obj_Connect=connect.Conexion(servidor,bd,user,password)
		obj_Connect.ejecutar_conn()
		self.puntero=obj_Connect.get_cursor()
