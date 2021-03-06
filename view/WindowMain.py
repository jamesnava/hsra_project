from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
sys.path.append("..")
from operations import operaciones
class Window_Main(object):
	
	def __init__(self):
		self.obj_operaciones=None
		
		#ventanas
		self.ventana_persona=None
		self.ventana_User=None

		#crear variable pestañas
		self.Frame_Agregar=None
		self.Frame_Consultar=None
		self.P_Contenedor=None

		#fin variable Pestaña
		#menues...
		self.Menu_Editar=None
		#widget Pestaña agregar
		self.Txt_Cabecera=None
		self.Txt_Descripcion=None
		self.Cargar_pdf=None

		#fin widget pestaña agregar

		#widget Pestaña consultar
		self.Txt_Buscar=None

		#fin widget pestaña consultar
		self.Ventana_Principal=Tk()
		self.Ventana_Principal.geometry('1200x630+50+50')
		self.Ventana_Principal.iconbitmap('../icons/libros.ico')
		self.Ventana_Principal.title('Gestion de Documentos')
		#ejecucion de funciones
		self.add_Menues()
		self.add_tabs()
		self.ejecutar()
	def add_tabs(self):
		#pestaña agregar
		self.P_Contenedor=ttk.Notebook(self.Ventana_Principal)
		#creando el contenido de las pestañas
		self.Frame_Agregar=ttk.Frame(self.P_Contenedor,width=1190,height=580)
		self.add_Frame_Agregar()
		self.Frame_Consultar=ttk.Frame(self.P_Contenedor,width=1190,height=580)
		self.add_Frame_Consultar()
		
		#agregando como pestañas
		self.P_Contenedor.add(self.Frame_Agregar,text='Agregar')
		self.P_Contenedor.add(self.Frame_Consultar,text='Consultar')
		self.P_Contenedor.pack(fill='both',expand=True)
	def add_Menues(self):
		#menu 1
		self.Menu_Editar=Menu(self.Ventana_Principal)
		self.Ventana_Principal.config(menu=self.Menu_Editar)
		#opciones menu1
		option1=Menu(self.Menu_Editar)
		option1.add_command(label="Datos Personales",command=self.Top_Persona)
		#opcion usuario
		option1.add_command(label="Crear Usuario",command=self.Top_User)
		#tipo de documento
		option1.add_command(label="Nueva Categoria Documento")

		self.Menu_Editar.add_cascade(label="Editar",menu=option1)

	def add_Frame_Agregar(self):
		font_s=('Verdana',20,'italic')
		etiqueta=ttk.Label(self.Frame_Agregar,text="Cabecera:")
		etiqueta['font']=font_s
		etiqueta.place(x=100,y=10)
		#agregando textbox
		self.Txt_Cabecera=ttk.Entry(self.Frame_Agregar,width=52)
		self.Txt_Cabecera.place(x=300,y=20)
		#descripcion
		etiqueta2=ttk.Label(self.Frame_Agregar,text="Descripcion:",font=font_s)
		etiqueta2.place(x=100,y=50)

		self.Txt_Descripcion=Text(self.Frame_Agregar,width=40,height=5)
		self.Txt_Descripcion.place(x=300,y=50)

		#cargar pdf
		etiqueta3=ttk.Label(self.Frame_Agregar,text="Cargar PDF:",font=font_s)
		etiqueta3.place(x=100,y=180)
		btn_open=ttk.Button(self.Frame_Agregar,text='Examinar...',command=self.Open_Pdf,width=50)
		btn_open.place(x=300,y=180)

	def add_Frame_Consultar(self):
		font_s=('Verdana',20,'italic')
		etiquetaC=ttk.Label(self.Frame_Consultar,text='Buscar',font=font_s)
		etiquetaC.place(x=100,y=10)

		self.Txt_Buscar=ttk.Entry(self.Frame_Consultar)
		self.Txt_Buscar.place(x=250,y=20)


	def Open_Pdf(self):
		self.Cargar_pdf=filedialog.askopenfilename(title="seleccione un archivo",filetypes=(("archivos pdf","*.pdf"),))

	def Top_Persona(self):
		self.obj_operaciones=operaciones.Operaciones()
		vary=30
		varx=50
		font_p=('Verdana',16,'italic')
		
			#self.Ventana_Principal.withdraw()
		self.ventana_persona=Toplevel()
		self.ventana_persona.title('Ingresar Datos')
		self.ventana_persona.geometry('800x500+100+150')
		self.ventana_persona.grab_set()
		self.ventana_persona.focus_set()

		dni=StringVar()
		nombre=StringVar()
		apellidoP=StringVar()
		apellidoM=StringVar()

		txt_dni=ttk.Entry(self.ventana_persona,textvariable=dni)
		txt_nombre=ttk.Entry(self.ventana_persona,textvariable=nombre)
		txt_apellidoP=ttk.Entry(self.ventana_persona,textvariable=apellidoP)
		txt_apellidoM=ttk.Entry(self.ventana_persona,textvariable=apellidoM)
			#self.ventana_persona.overrideredirect(True)
		labelDni=ttk.Label(self.ventana_persona,text='Dni:', font=font_p)
		labelDni.place(x=varx,y=vary)
		txt_dni.place(x=varx+220,y=vary)

		labelNombre=ttk.Label(self.ventana_persona,text='Nombre:',font=font_p)
		labelNombre.place(x=varx,y=vary+40)
		txt_nombre.place(x=varx+220,y=vary+40)

		labelApellidoP=ttk.Label(self.ventana_persona,text='Apellido Paterno:', font=font_p)
		labelApellidoP.place(x=varx,y=vary+80)
		txt_apellidoP.place(x=varx+220,y=vary+80)

		labelApellidoM=ttk.Label(self.ventana_persona,text='Apellido Materno:',font=font_p)
		labelApellidoM.place(x=varx,y=vary+120)
		txt_apellidoM.place(x=varx+220,y=vary+120)

					
		boton=ttk.Button(self.ventana_persona,text="Aceptar")
		boton['command']=lambda:[self.obj_operaciones.add_people(dni.get(),nombre.get(),apellidoP.get(),apellidoM.get()),txt_nombre.delete(0,'end'),txt_dni.delete(0,'end'),txt_apellidoP.delete(0,'end'),txt_apellidoM.delete(0,'end')]	
		boton.place(x=400,y=vary+160)
			#self.Ventana_Principal.iconify()
		#getting data
	def Top_User(self):
		self.obj_operaciones=operaciones.Operaciones()
		vary=30
		varx=50
		font_p=('Verdana',16,'italic')
		
			#self.Ventana_Principal.withdraw()
		self.ventana_User=Toplevel()
		self.ventana_User.title('Crea un nuevo Usuario')
		self.ventana_User.geometry('800x500+100+150')
		self.ventana_User.grab_set()
		self.ventana_User.focus_set()
		#widget
		usuario=StringVar()
		clave=StringVar()
		Rclave=StringVar()
		txt_Usurio=ttk.Entry(self.ventana_User,textvariable=usuario)
		txt_pass=ttk.Entry(self.ventana_User,textvariable=clave)
		txt_Rpass=ttk.Entry(self.ventana_User,textvariable=Rclave)
		

	def ejecutar(self):
		self.Ventana_Principal.mainloop()
obj=Window_Main()


		
