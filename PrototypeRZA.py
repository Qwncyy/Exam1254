import tkinter as tk
from tkinter import *
import customtkinter 



root = tk.Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

def theme():

    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":

        root.tk.call("set_theme", "dark")



class HomePage():

    def Startup(self):
        self = tk.Toplevel
        self.title('Riget Zoo Adventures')
        self.geometry('600x350')




if __name__ == "__main__":
    root = customtkinter.CTk()
    #Set Website Theme
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    #call the GitHub Azure theme
    theme = theme()
    theme.pack
    
    
    home = HomePage(root)
    home.pack(fill="both", expand=True)

    root.update()

    root.mainloop()

