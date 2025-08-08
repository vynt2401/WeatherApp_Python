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


weat_img = PhotoImage(file = "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/Layer 7.png")
weatherimgae = Label(root, image=weat_img, bg = "#333c4c")
weatherimgae.place(x = 280, y = 122)

textField = tk.Entry(root, justify="center", width=15, font=("poppins", 25, 'bold'), bg = "#333c4c",border=0, fg = "white")
textField.place(x= 340, y = 124)

Search_icon = PhotoImage(file = "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/Layer 6.png")
myimg_icon = Button(root, image= Search_icon, bg = "#333c4c", borderwidth=0,cursor="hand2")
myimg_icon.place(x= 630, y = 125)




#bottom box

frame = Frame(root, width = 900, height=180, bg = "#7094d4")
frame.pack(side = BOTTOM)

#boxes 
first_box = PhotoImage(file= "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/Rounded Rectangle 2.png")
second_box = PhotoImage(file= "/run/media/ntv/MAIN/Python_testing/APP/app_weather/OpenWeather 5 day API/Images/Rounded Rectangle 2 copy.png")


Label(frame, image=first_box, bg = "#7094d4").place(x= 30, y = 20)
Label(frame, image=second_box, bg = "#7094d4").place(x= 300, y = 30)
Label(frame, image=second_box, bg = "#7094d4").place(x= 400, y = 30)
Label(frame, image=second_box, bg = "#7094d4").place(x= 500, y = 30)
Label(frame, image=second_box, bg = "#7094d4").place(x= 600, y = 30)


#clock 
clock = Label(root , font = ("Helvetica", 20), bg = "#202731", fg = "white")
clock.place(x = 30, y = 20)

#time zone 

timeZone = Label(root, font = ("Helvetica", 20), bg = "#202731", fg = "white")
timeZone.place(x = 500, y = 20)


long_lat = Label(root, font = ("Helvetica", 10), bg = "#202731", fg = "white")
long_lat.place(x = 500, y = 50)


#thpwd

t = Label(root, font = ("Helvetica", 9), bg = "#333c4c", fg = "white")
t.place(x = 150, y =120)

h = Label(root, font = ("Helvetica", 9), bg = "#333c4c", fg = "white")
h.place(x = 150, y =140)

p = Label(root, font = ("Helvetica", 9), bg = "#333c4c", fg = "white")
p.place(x = 150, y =160)

w = Label(root, font = ("Helvetica", 9), bg = "#333c4c", fg = "white")
w.place(x = 150, y =180)

d = Label(root, font = ("Helvetica", 9), bg = "#333c4c", fg = "white")
d.place(x = 150, y =200)


#first_cell

first_frame = Frame(frame, width = 200, height=150, bg = "#aad1c8")
first_frame.place(x = 35, y = 135)

first_img = Label(first_frame, bg = "#323661")
first_img.place(x = 1, y = 15)


root.mainloop()