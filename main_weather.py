# Weather Update App using Custom Tkinter
import requests
from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk

root = CTk()
root.geometry("560x450")
root.title("Weather Update App")

frame = CTkFrame(root, height=260, width = 300)
frame.grid(row = 0, column=0, rowspan = 3, columnspan = 4, padx = 20, pady = 20, sticky ="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# Weather icons
weather_icons = {
    'Clear': 'clear_icon.png',
    'Clouds': 'cloudy_icon.png',
    'Rain': 'rainy_icon.png',
    # Add more weather conditions and their respective icons as needed
}

# 1st part
frame_search = CTkFrame(frame, fg_color="transparent")
search_box = CTkEntry(frame_search, width=170, height=36, placeholder_text="Location", placeholder_text_color="#95A4B2", font=('Lato', 16, 'bold'))
search_box.grid(row=0, column=0, padx=(10, 20), pady=(10, 10))

search_btn = CTkButton(frame_search, text="Search", font=('Lato', 16, 'bold'), height=34, width=120, command=lambda: location())
search_btn.grid(row=0, column=1, padx=(20, 10), pady=(10, 10))

frame_search.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# 2nd part
frame_image = CTkFrame(frame, fg_color="transparent")
weather_icon_path = 'weather1.png'  # Default weather icon
weather_icon = Image.open(weather_icon_path)
weather_icon = ImageTk.PhotoImage(weather_icon)
weather_icon_label = Label(frame_image, image=weather_icon, bg="#2B2B2B")
weather_icon_label.grid(row=0, column=0)

place = CTkLabel(frame_image, text="- -", font=('Lato', 24, 'bold'))
place.grid(row=1, column=0, padx=(10, 10), pady=(20, 0))

frame_image.grid(row=1, column=0, padx=10, pady = 0, columnspan=3)

# 3rd part
info_frame = CTkFrame(frame)

# info
temp_frame = CTkFrame(info_frame)
temp_name = CTkLabel(temp_frame, text="Temp (°F)", font=('Lato', 16, 'bold'))
temp_name.grid(row=0, column=0, padx=20, pady=10)

temp = CTkLabel(temp_frame, text="- -", font=('Lato', 16, 'bold'))
temp.grid(row=1, column=0, padx=10, pady= 10)

temp_frame.grid(row=0, column=0, padx=(20, 10), pady=20)

# description
desc_frame = CTkFrame(info_frame)
desc_name = CTkLabel(desc_frame, text="Description", font=('Lato', 16, 'bold'))
desc_name.grid(row=0, column=1, padx=20, pady=10)

desc = CTkLabel(desc_frame, text="- -", font=('Lato', 16, 'bold'))
desc.grid(row=1, column=1, padx=10, pady = 10)

desc_frame.grid(row=0, column=1, padx=10, pady=20)

# wind
wind_frame = CTkFrame(info_frame)
wind_name = CTkLabel(wind_frame, text="Wind (m/s)", font=('Lato', 16, 'bold'))
wind_name.grid(row=0, column=2, padx=20, pady=10)

wind = CTkLabel(wind_frame, text="- -", font=('Lato', 16, 'bold'))
wind.grid(row=1, column=2, padx=10, pady=10)

wind_frame.grid(row=0, column=2, padx=(10, 20), pady=20)

info_frame.grid(row=2, column=0, padx=10, pady=20, columnspan=3)

api_key = 'f30f379d1ea2ca8b849bfeaac25ab246'

def location():
    text = search_box.get()
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={text}&units=imperial&APPID={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temperature = weather_data.json()['main']['temp']
    wind_speed = weather_data.json()['wind']['speed']

    place.configure(text=text)
    temp.configure(text=temperature)
    desc.configure(text=weather)
    wind.configure(text=wind_speed)

    # Update weather icon based on weather description
    weather_icon_path = weather_icons.get(weather, 'default_icon.png')  # Default icon if weather not found
    new_weather_icon = Image.open(weather_icon_path)
    new_weather_icon = ImageTk.PhotoImage(new_weather_icon)
    weather_icon_label.configure(image=new_weather_icon)
    weather_icon_label.image = new_weather_icon

root.mainloop()
