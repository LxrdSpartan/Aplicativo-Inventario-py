from tkinter import *
from tkinter import ttk
from Productos import datos
from tkinter import messagebox





class Ventana (Frame):
    productos =datos()
    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master=master
        self.pack()
        self.create_widgets()
        self.llenardatos()
        self.habilitarframes("disabled")
        self.habilitarbtnpri("normal")
        self.habilitarbotonguardado("disabled")
        self.id=-1  
        
    def habilitarframes(self, estado):
        self.txtNombre.configure(state=estado)
        self.txtTipo.configure(state=estado)
        self.txtCantidad.configure(state=estado)
        self.txtOperando.configure(state=estado)
        
    def habilitarbtnpri(self,estado):
        self.btnAgregar.configure(state=estado)
        self.btnmodificar.configure(state=estado)
        self.btneliminar.configure(state=estado)
    
    def habilitarbotonguardado(self,estado):
        self.btnguardar.configure(state=estado)                
        self.btncancelar.configure(state=estado)
         
    def limpiarframes(self):
        self.txtNombre.delete(0,END)
        self.txtTipo.delete(0,END)
        self.txtCantidad.delete(0,END)
        self.txtOperando.delete(0,END)
        
    def limpiarGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
            
    def llenardatos(self):
        datos = self.productos.consulta_datos()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4]))
            
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
        
    def fAgregar(self):
        self.habilitarframes("normal")
        self.habilitarbtnpri("disabled")
        self.habilitarbotonguardado("normal")
        self.limpiarframes()
        self.txtNombre.focus()
        
    def fModificar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Seleccionar un elemento.')            
        else:      
            self.id= clave
            self.habilitarframes("normal")
            valores = self.grid.item(selected,'values')
            self.limpiarframes() 
            self.txtNombre.insert(0,valores[0])
            self.txtTipo.insert(0,valores[1])
            self.txtCantidad.insert(0,valores[2])
            self.txtOperando.insert(0,valores[3])  
            self.habilitarbtnpri("disabled") 
            self.habilitarbotonguardado("normal")
            self.txtNombre.focus()
            
    def fEliminarobjeto(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Selecciona un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.productos.elimina_producto(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiarGrid()
                    self.llenardatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                              
    
    def fGuardar(self):
        if self.id ==-1:       
            self.productos.inserta_productos(self.txtNombre.get(),self.txtTipo.get(),self.txtCantidad.get(),self.txtOperando.get())            
            messagebox.showinfo("Insertar", 'Elemento Agregado correctamente.')
        else:
            self.productos.modifica_producto(self.id,self.txtNombre.get(),self.txtTipo.get(),self.txtCantidad.get(),self.txtOperando.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1   
        self.limpiarGrid()
        self.llenardatos()    
        self.limpiarframes()
        self.habilitarbotonguardado("disabled")   
        self.habilitarbtnpri("normal")
        self.habilitarframes("disabled")
        
           
    
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarframes()
            self.habilitarbotonguardado("disabled")
            self.habilitarbtnpri("normal")
            self.habilitarframes("disabled")
            
        
        
        
    def create_widgets(self):
        frame1= Frame(self, bg="midnight blue")
        frame1.place(x=0, y=0, width=110, height=260)
        
        self.btnAgregar=Button(frame1, text= "Agregar Objeto", command=self.fAgregar, bg="goldenrod", fg="Black")
        self.btnAgregar.place(x=5, y=50, width=100, height=30)

        
        self.btnmodificar=Button(frame1, text= "Modificar Objeto", command=self.fModificar, bg="goldenrod", fg="Black")
        self.btnmodificar.place(x=5, y=100, width=100, height=30)
        
        self.btneliminar=Button(frame1, text= "Eliminar Objeto", command=self.fEliminarobjeto, bg="goldenrod", fg="Black")
        self.btneliminar.place(x=5, y=150, width=100, height=30)
        
        frame2= Frame(self, bg="goldenrod")
        frame2.place(x=115, y=0, width=160, height=260)
        
        Label1=Label(frame2, text="Nombre:", bg="goldenrod")
        Label1.place(x=3,y=3)
        
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3, y=25, width= 150, height=20 )
        
        Label2=Label(frame2, text="Tipo:", bg="goldenrod")
        Label2.place(x=3,y=50)
        
        self.txtTipo=Entry(frame2)
        self.txtTipo.place(x=3, y=70, width= 150, height=20 )
        
        Label3=Label(frame2, text="Cantidad:", bg="goldenrod")
        Label3.place(x=3,y=100)
        
        self.txtCantidad=Entry(frame2)
        self.txtCantidad.place(x=3, y=120, width= 150, height=20 )
        
        Label4=Label(frame2, text="Operando:", bg="goldenrod")
        Label4.place(x=3,y=150)
        
        self.txtOperando=Entry(frame2)
        self.txtOperando.place(x=3, y=172, width= 150, height=20 )
        
        
        self.btnguardar=Button(frame2, text= "Guardar", command=self.fGuardar, bg="goldenrod", fg="Black")
        self.btnguardar.place(x=10, y=210, width=65, height=30)
        
        
        self.btncancelar=Button(frame2, text= "Cancelar", command=self.fCancelar, bg="goldenrod", fg="Black")
        self.btncancelar.place(x=85, y=210, width=65, height=30)
        
        
        self.grid= ttk.Treeview(self, columns=("COL1", "COL2", "COL3", "COL4"))
        
        
        self.grid.column("#0", width=50)
        self.grid.column("COL1", width=60, anchor= CENTER)
        self.grid.column("COL2", width=90, anchor= CENTER)
        self.grid.column("COL3", width=90, anchor= CENTER)
        self.grid.column("COL4", width=90, anchor= CENTER)
        
        self.grid.heading("#0", text="ID", anchor= CENTER)
        self.grid.heading("COL1", text="Nombre", anchor= CENTER)
        self.grid.heading("COL2", text="Tipo", anchor= CENTER)
        self.grid.heading("COL3", text="Cantidad", anchor= CENTER)
        self.grid.heading("COL4", text="Operando", anchor= CENTER)
        
        self.grid.place(x=280,y=0, width=395, height=260)
        self.grid.insert("", END, text="", values=(" "))


    
   
    

     
     