from tkinter import *
from Ventana import *

def main():
    root=Tk()
    root.wm_title("Inventario UDC")
    root.iconbitmap(r"C:\Users\juans\Desktop\Aplicativo Inventario\unnamed.ico")
    app = Ventana (root)
    app.mainloop()
    

if __name__ == '__main__':
    main()
    
    