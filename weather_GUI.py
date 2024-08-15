from tkinter import *
import tkinter as tk
import tkinter.messagebox as m
from tkinter import ttk
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderInsufficientPrivileges
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk
import os

#for main window
d = Tk()
d.title("Weather App")
d.geometry("900x500+300+200")
d.resizable(False, False)

icon_label = None
# for get the weather data by city
def getwether():
    city = textfeild.get()
    geolocator = Nominatim(user_agent="geoapiExercises")

    global icon_label

    if city == "":
        m.showinfo("Warning", "Please enter the city !")
    else:
        try:
            location = geolocator.geocode(city)
            if not location:
                raise AttributeError("Invalid city name!")

            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        except GeocoderInsufficientPrivileges as e:
            m.showerror("Error", f"Geocoding request failed: {e}")
        
        except AttributeError as a:
            m.showerror("Error", "Invalid city name !")

        
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")    # current_time = local_time.strftime("%I:%M %p")
        current_date = local_time.strftime("%d-%m-%Y")
        clock.config(text=current_time)
        date.config(text=current_date)
        name.config(text="Current Weather")

    #api setup
        API_key = YOUR API KEY
        url = YOUR API KEY URL

        data_info = requests.get(url).json()
        condition = data_info['weather'][0]['main']
        description = data_info['weather'][0]['description']
        temp = int(data_info['main']['temp']-273.15)
        pressure = data_info['main']['pressure']
        humidity = data_info['main']['humidity']
        wind = data_info['wind']['speed']
        icon_code = data_info['weather'][0]['icon']
        print(icon_code)    
        icon_url = YOUR WEATHER ICON URL


        city_name.config(text=city)
        t.config(text=f"{temp} °C")
        c.config(text=f"{condition} | feels like {temp} °C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity} %")
        des.config(text=description)
        p.config(text=f"{pressure} hPa")
        
     
        path = "suraj.jpg"
        print(os.path.exists(path))

    # for destroy previous image
        if icon_label is not None:
            icon_label.destroy()

    #for clear day sky
        if icon_code =="01d":
            icon_photo = PhotoImage(file="suraj.jpg")
            
        
     #for clear night sky
        if icon_code == "01n":
            icon_photo = PhotoImage(file="moon.png")
            

     #for few clouds: 11-25% for day
        if icon_code =="02d":
            icon_photo = PhotoImage(file="few_cloud.png")
            

    # for few clouds: 11-25% for night
        if icon_code == "02n":
            icon_photo = PhotoImage(file="few_cloud1.png")
         

    #for scattered clouds: 25-50%
        if icon_code =="03d" or icon_code == "03n":
            icon_photo = PhotoImage(file="scattered.png")
            

    #for broken and overcast clouds:51-54% and 85-100%
        if icon_code =="04d" or icon_code == "04n":
            icon_photo = PhotoImage(file="overcast.png")
                 

    #for snow condition 
        if icon_code =="13d" or icon_code == "13n":
            icon_photo = PhotoImage(file="snow.png")
            
        
    #for rain 09d
        if icon_code =="09d" or icon_code == "09n":
            icon_photo = PhotoImage(file="shower.png")
            

    #for rain 10d for day
        if icon_code =="10d":
            icon_photo = PhotoImage(file="rain.png")
            

    #for rain 10n for night
        if icon_code == "10n":
            icon_photo = PhotoImage(file="10n.png")
            

    #for thunderstorm for day 11d and night 11n
        if icon_code =="11d" or icon_code == "11n":
            icon_photo = PhotoImage(file="storm.png")
            
        
    #for mist or haze or dust or smoke or fog or tornado 50d
        if icon_code =="50d" or icon_code == "50n":
            icon_photo = PhotoImage(file="mist.png")
            
        icon_photo = icon_photo.subsample(2, 2)  # Resize by subsampling
        icon_label = Label(d, image=icon_photo)
        icon_label.place(x=640, y=130)
        icon_label.image = icon_photo
           

            
#search box
search_img = PhotoImage(file="search_bar.png")
myimage = Label(image=search_img)
myimage.place(x="20", y="20")

textfeild = tk.Entry(d, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfeild.place(x="50", y="40")
textfeild.focus()

    #for search button
search_icon = PhotoImage(file="search.png")
my_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", width=51, height=50, command=getwether)
my_icon.place(x="400", y="34")
   

    # for weather logo
Weather_logo = PhotoImage(file="weather1.png")
my_logo = Label(image=Weather_logo)
my_logo.place(x="80", y="100")

    # Create canvas for the circular icon
# canvas = Canvas(d, highlightthickness=0)    # width=150, height=150, bg="#3c6b6b",
# canvas.place(x="700", y="170")

    #for bottom box
box = PhotoImage(file="copy of box.png")
my_box = Label(image=box)
my_box.pack(padx=5, pady=5, side=BOTTOM,)

    #time
name = Label(d, font=("arial", 15, "bold"))
name.place(x="25", y="100")

clock = Label(d, font=("helvetica", 20))
clock.place(x="25",y="130")

date = Label(d, font=("helvetica", 15))
date.place(x="25", y="160")

    #labels
label1 = Label(d, text="WIND", font=("Helvetica", 15, "bold"),fg="white", bg="#1ab5ef")
label1.place(x="120", y="400")

label2 = Label(d, text="HUMIDITY", font=("Helvetica", 15, "bold"),fg="white", bg="#1ab5ef")
label2.place(x="250", y="400")

label3 = Label(d, text="DESCRIPTION", font=("Helvetica", 15, "bold"),fg="white", bg="#1ab5ef")
label3.place(x="430", y="400")

label4 = Label(d, text="PRESSURE", font=("Helvetica", 15, "bold"),fg="white", bg="#1ab5ef")
label4.place(x="650", y="400")

city_name = Label(font=("arial", 20, "bold"), fg="#101820")
city_name.place(x="400", y="110")

    # label for temperature
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x="400", y="150")

    #label for condition
c = Label(font=("arial", 15, "bold"))
c.place(x="400", y="250")

    #label for wind
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x="120", y="430")

    #label for humidity
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x="250", y="430")

    #label for description
des = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
des.place(x="430", y="430")

    #label for pressure
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x="650", y="430")

d.mainloop()