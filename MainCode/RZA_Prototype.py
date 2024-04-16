import tkinter as tk
from tkinter import *
from customtkinter import *
import customtkinter
import PIL
from PIL import Image, ImageTk

#class SideBar():
    #bar = CTk()
    #min_w = 50
    #max_w = 100


    #sidemenu = customtkinter.CTkFrame(master = bar, fg_color="#F1FF00")
    #sidemenu.pack(anchor="left", )
    #expanded = False

    #def open():
        #.canvas.itemconfigure





class HomePage():


    def Startup():
        home = CTk()
        #Setup the theme and colours
        customtkinter.set_default_color_theme("green")
        customtkinter.set_appearance_mode('dark')
        #Size and title of the website
        home.title('Riget Zoo Adventures')
        home.geometry('600x600')
        #uses a frame to act as a different coloured background with a scroll bar
        frame = customtkinter.CTkScrollableFrame(master=home, fg_color="#A3790D")
        frame.pack(anchor="center",fill="both", expand=True)

        image = Image.open("Images\\Leopard.png", "r")
        image.load()
        background_img = customtkinter.CTkImage(image, size=(600, 200))

        bg_lbl = customtkinter.CTkLabel(home, size=(600, 200))
        bg_lbl.configure(text="", image=background_img)
        



        home.mainloop()
    Startup()














def main():

    

    HomePage()
main()


