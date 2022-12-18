import mysql.connector

class datos:
    
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="1519", database="Inventario")

    def __str__(self):
        datos=self.consulta_datos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_datos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Datos")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_producto(self, ID):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM datos WHERE ID = {}".format(ID)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    
    def inserta_productos(self,Nombre,Tipo, Cantidad,Operando):
        cur=self.cnn.cursor()
        sql='''INSERT Datos (Nombre, Tipo, Cantidad, Operando)
        VALUES ('{}', '{}','{}','{}')'''.format(Nombre, Tipo, Cantidad, Operando)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
     
    def elimina_producto(self,ID):
         cur = self.cnn.cursor()
         sql='''DELETE FROM Datos WHERE ID = {}'''.format(ID)
         cur.execute(sql)
         n=cur.rowcount
         self.cnn.commit()    
         cur.close()
         return n  
     
    def modifica_producto(self,ID,Nombre,Tipo,Cantidad,Operando):
        cur = self.cnn.cursor()
        sql='''UPDATE Datos SET Nombre='{}', Tipo='{}', Cantidad='{}',
        Operando='{}' WHERE Id={}'''.format(Nombre, Tipo, Cantidad, Operando,ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
         
