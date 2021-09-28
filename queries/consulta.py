import connect
class Consultar(object):
	def __init__(self):
		self.puntero=None
	def get_people(self):
		sql='select * from persona'
		self.puntero.execute(sql)
		rows=self.puntero.fetchall()		
		
	def get_puntero(self,servidor,bd,user,password):
		obj_Connect=connect.Conexion(servidor,bd,user,password)
		obj_Connect.ejecutar_conn()
		self.puntero=obj_Connect.get_cursor()
