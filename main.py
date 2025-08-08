from tkinter import *
import tkinter as tk
import pytz
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import requests
from PIL import Image, ImageTk  
from tkinter import messagebox


root = Tk()
root.title("Weather App")
root.geometry("750x470+300+200")
root.resizable(False, False)
root.config(bg = "#202731")


#ICON

img_icon = PhotoImage(file = "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/logo.png")
root.iconphoto(False, img_icon)

round_box = PhotoImage(file = "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/Rounded Rectangle 1.png")
Label(root, image=round_box, bg ="#207231").place(x= 30, y = 60 )


#LABEL

label1 = Label(root, text = "Temperature", font = ("Helvetica", 11), bg = "#aad1c8", fg = "#323661")
label1.place(x =50, y = 120)

label2 = Label(root, text = "Humidity", font = ("Helvetica", 11), bg = "#aad1c8", fg = "#323661")
label2.place(x =50, y = 140)

label3 = Label(root, text = "Pressure", font = ("Helvetica", 11), bg = "#aad1c8", fg = "#323661")
label3.place(x =50, y = 160)

label4 = Label(root, text = "Wind speed", font = ("Helvetica", 11), bg = "#aad1c8", fg = "#323661")
label4.place(x =50, y = 180)

label5 = Label(root, text = "Description", font = ("Helvetica", 11), bg = "#aad1c8", fg = "#323661")
label5.place(x =50, y = 200)

#Search Box

Search_img = PhotoImage(file  = "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/Rounded Rectangle 3.png")
myimg = Label(root, image = Search_img, bg = '#202731')
myimg.place(x = 2710, y  = 122)



root.mainloop()