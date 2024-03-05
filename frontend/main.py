# import tkinter as tk
from tkinter import *
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/search/hotel"

def on_click():
    print("on click")
    payload = {
        "start_date": country.get(),
        "start_time": province.get(),
    }
    response = requests.post(API_ENDPOINT1, json=payload)
    if response.ok:
        data = response.json()
        data = data["all_hotel"]
        hotel_list = []
        for hotel in data:
            hotel_list.append({"hotel_name": hotel["hotel_name"]})
    return hotel_list

root = Tk()
root.option_add("*Font", "impact 18")
country = StringVar()
province = StringVar()


user1 = StringVar()
subject = StringVar()
data_list = ['0']

Label(root, text="Country :").grid(row=0, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=country, width=12, justify="left").grid(row=0, column=1, padx=10)
Label(root, text="Province :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=province, width=12, justify="left").grid(row=1, column=1, padx=10)
Button(root, text=" Search ", bg="green", command=on_click).grid(row=5, column=0, columnspan=2)

root.mainloop()