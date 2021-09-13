from tkinter import *
from tkinter import ttk
from tkinter import filedialog
class Window_Main(object):
	def __init__(self):
		#crear variable pestañas
		self.Frame_Agregar=None
		self.Frame_Consultar=None
		self.P_Contenedor=None

		#fin variable Pestaña
		#widget Pestaña agregar
		self.Txt_Cabecera=None
		self.Txt_Descripcion=None
		self.Cargar_pdf=None

		#fin widget pestaña agregar
		self.Ventana_Principal=Tk()
		self.Ventana_Principal.geometry('1200x630')
		self.Ventana_Principal.title('Gestion de Documentos')
		#ejecucion de funciones
		self.add_tabs()
		self.ejecutar()
	def add_tabs(self):
		#pestaña agregar
		self.P_Contenedor=ttk.Notebook(self.Ventana_Principal)
		#creando el contenido de las pestañas
		self.Frame_Agregar=ttk.Frame(self.P_Contenedor,width=1190,height=580)
		self.add_Frame_Agregar()
		self.Frame_Consultar=ttk.Frame(self.P_Contenedor,width=1190,height=580)
		
		#agregando como pestañas
		self.P_Contenedor.add(self.Frame_Agregar,text='Agregar')
		self.P_Contenedor.add(self.Frame_Consultar,text='Consultar')
		self.P_Contenedor.pack(fill='both',expand=True)
	def add_Frame_Agregar(self):
		etiqueta=ttk.Label(self.Frame_Agregar,text="Cabecera:")
		etiqueta.grid(column=2,row=5)
		#agregando textbox
		self.Txt_Cabecera=ttk.Entry(self.Frame_Agregar)
		self.Txt_Cabecera.grid(column=4,row=5)
		#descripcion
		etiqueta2=ttk.Label(self.Frame_Agregar,text="Descripcion:")
		etiqueta2.grid(column=2,row=10)

		self.Txt_Descripcion=Text(self.Frame_Agregar,width=40,height=5)
		self.Txt_Descripcion.grid(column=4,row=10)

		#cargar pdf
		etiqueta3=ttk.Label(self.Frame_Agregar,text="Cargar PDF:")
		etiqueta3.grid(column=2,row=20)
		btn_open=ttk.Button(self.Frame_Agregar,text='Examinar...',command=self.Open_Pdf)
		btn_open.grid(column=4,row=20)


	def Open_Pdf(self):
		self.Cargar_pdf=filedialog.askopenfilename(title="seleccione un archivo")

	def ejecutar(self):
		self.Ventana_Principal.mainloop()
obj=Window_Main()


		
