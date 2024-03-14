search_hotel_endpoint = "http://127.0.0.1:8000/search/hotel"
search_reservation_endpoint = "http://127.0.0.1:8000/search/reservation"
login_endpoint = "http://127.0.0.1:8000/auth/login"
logout_endpoint = "http://127.0.0.1:8000/auth/logout"
register_endpoint = "http://127.0.0.1:8000/auth/register"
get_personal_information_endpoint = "http://127.0.0.1:8000/account/profile"
get_my_travelling_endpoint = "http://127.0.0.1:8000/account/MyReservations"
get_my_favorite_hotel_end_point = "http://127.0.0.1:8000/account/MyFavoriteHotel"
add_my_favorite_hotel_endpoint = "http://127.0.0.1:8000/account/AddFavoriteHotel"
remove_my_favorite_hotel_endpoint = "http://127.0.0.1:8000/account/UnFavoriteHotel"
hotel_ratelist_endpoint = "http://127.0.0.1:8000/reservation/rateListMenu"
booking_review_endpoint = "http://127.0.0.1:8000/reservation/reviewDetails"
show_coupon_endpoint = "http://127.0.0.1:8000/payment/showcoupon"
payment_method_endpoint = "http://127.0.0.1:8000/payment/methodselect"
payment_coupon_endpoint = "http://127.0.0.1:8000/payment/couponselect"
payment_process_endpoint = "http://127.0.0.1:8000/payment/process"
admin_add_hotel_endpoint = "http://127.0.0.1:8000/admin/AddHotel"
admin_delete_hotel_endpoint = "http://127.0.0.1:8000/admin/DeleteHotel"
admin_cancel_booking_endpoint = "http://127.0.0.1:8000/admin/CancelBooking"
customer_cancel_booking_endpoint = "http://127.0.0.1:8000/account/CancelBooking"

import tkinter as tk
from tkinter import *    
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
from datetime import date
from PIL import ImageTk, Image 
import requests

root = ttk.Window(themename="cyborg")
root.title("เเอปจองโรงเเรม")
root.geometry("1280x720")

style = ttk.Style()
style.configure("TNotebook.Tab", font=('Helvetica', 16))
my_travelling_notebook = ttk.Notebook(root, bootstyle="cyborg", width=1280, height=720)

frame_home = ttk.Frame(root)
frame_register = ttk.Frame(root)
frame_login = ttk.Frame(root)
frame_search_hotel = ttk.Frame(root)
frame_search_reservation = ttk.Frame(root)
frame_hotel = ttk.Frame(root)
frame_ratelist = ttk.Frame(root)
frame_review = ttk.Frame(root)
frame_method = ttk.Frame(root)
frame_transaction = ttk.Frame(root)
frame_reservation = ttk.Frame(root)
frame_account = ttk.Frame(root)
frame_personal_information = ttk.Frame(root)
frame_my_favorite_hotel = ttk.Frame(root)
arriving_tab = ttk.Frame(my_travelling_notebook)
cancelled_tab = ttk.Frame(my_travelling_notebook)
frame_admin = ttk.Frame(root)
frame_admin_add_hotel = ttk.Frame(root)
frame_admin_delete_hotel = ttk.Frame(root)
frame_admin_cancel_booking = ttk.Frame(root)
frame_customer_cancel_booking = ttk.Frame(root)

label_alert_excess = []
label_hotel_excess = []
label_reservation_excess = []
label_personal_information_excess = []
label_my_travelling_excess = []
label_my_favorite_hotel_excess = []
label_admin_add_hotel_excess = []
label_admin_delete_hotel_excess = []
label_admin_cancel_booking_excess = []

isclick_button_list = []

def backward(page, current_frame):
    show_page(page, current_frame)

    for label in label_hotel_excess:
        label.grid_forget()
    label_hotel_excess.clear()
    for label in label_reservation_excess:
        label.grid_forget()
    label_reservation_excess.clear()
    for label in label_personal_information_excess:
        label.grid_forget()
    label_personal_information_excess.clear()
    for label in label_my_travelling_excess:
        label.grid_forget()
    label_my_travelling_excess.clear()
    for label in label_my_favorite_hotel_excess:
        label.grid_forget()
    label_my_favorite_hotel_excess.clear()
    for label in label_admin_add_hotel_excess:
        label.grid_forget()
    label_admin_add_hotel_excess.clear()
    for label in label_admin_delete_hotel_excess:
        label.grid_forget()
    label_admin_delete_hotel_excess.clear()
    for label in label_admin_cancel_booking_excess:
        label.grid_forget()
    label_admin_cancel_booking_excess.clear()

    isclick_button_list.clear()
    

def show_page(page, current_frame=frame_home):
    current_frame.pack_forget()

    for label in label_alert_excess:
        label.grid_forget()

    if page == "home":
        email.set("")
        password.set("")
        current_firstname.set(None)
        current_lastname.set(None)
        frame_home.pack()
    elif page == "register":
        frame_register.pack(expand=True)
    elif page == "login":
        frame_login.pack()
    elif page == "search_hotel":
        frame_search_hotel.pack()
    elif page == "search_reservation":
        frame_search_reservation.pack()
    elif page == "hotel":
        frame_hotel.pack()
    elif page == "ratelist":
        frame_ratelist.pack()
    elif page == "review":
        frame_review.pack()
    elif page == "method":
        frame_method.pack()
    elif page == "transaction":
        frame_transaction.pack()
    elif page == "reservation":
        frame_reservation.pack()
    elif page == "account":
        frame_account.pack()
    elif page == "personal_information":
        frame_personal_information.pack()
    elif page == "my_travelling":
        my_travelling_notebook.pack()
        my_travelling_notebook.add(arriving_tab, text="กำลังจะมาถึง")
        my_travelling_notebook.add(cancelled_tab, text="ยกเลิกเเล้ว")
    elif page == "my_favorite_hotel":
        frame_my_favorite_hotel.pack()
    elif page == "admin":
        frame_admin.pack()
    elif page == "admin_add_hotel":
        frame_admin_add_hotel.pack()
    elif page == "admin_delete_hotel":
        frame_admin_delete_hotel.pack()
    elif page == "admin_cancel_booking":
        frame_admin_cancel_booking.pack()
    elif page == "customer_cancel_booking":
        frame_customer_cancel_booking.pack()

def on_click_confirm_payment_button(method_confirm_button):
    if payment_method.get() == "C":
        payment_arg1_label.config(text="หมายเลขบัตรเครดิต")
        payment_arg2_label.config(text="หมายเลข CVV")
        method_confirm_button.configure(state="!disabled")
    elif payment_method.get() == "M":
        payment_arg1_label.config(text="เลขที่บัญชีธนาคาร")
        payment_arg2_label.config(text="ธนาคาร")
        method_confirm_button.configure(state="!disabled")
    elif payment_method.get() == "P":
        payment_arg1_label.config(text="หมายเลข Paypal")
        payment_arg2_label.config(text="ที่อยู่อีเมล")
        method_confirm_button.configure(state="!disabled")
    sum_price_label.configure(text=f"ราคารวม : {sum_price.get()}")
    
def on_click_confirm_method_button(selection,transaction_arg1,transaction_arg2,coupon_confirm_button):
    payload = {
        "selection" : selection,
        "transaction_arg1" : transaction_arg1,
        "transaction_arg2" : transaction_arg2
    }
    response = requests.post(payment_method_endpoint, json=payload)
    data = response.json()

    if 'transaction_type' in data:
        coupon_confirm_button.configure(state="!disabled")
    else:
        method_alert_label.grid(row=5,column=1,pady=50)

def on_click_confirm_coupon_button(coupon_id,isclick,payment_process_button):
    if isclick.get() == False:
        payload = {
            "coupon_id" : coupon_id
        }
        response = requests.post(payment_coupon_endpoint, json=payload)
        data = response.json()

        sum_price_label.configure(text=f"ราคารวม : {data['current price']}")
        payment_process_button.configure(state="!disabled")
        isclick.set(True)

def on_click_payment_process_button():
    response = requests.get(payment_process_endpoint)
    data = response.json()

    size = 16
    transaction_title_label.grid(row=0,column=0,pady=20)
    booking_title_label.grid(row=1,column=0,sticky='w')
    transaction_title2_label.grid(row=1,column=1,sticky='w')

    booking_name_label = ttk.Label(frame_transaction,text="ชื่อ-นามสกุล : " + data['Your Booking'].get('Firstname') + data['Your Booking'].get('Lastname'), font=("Helevetica",size), bootstyle="light")
    booking_no_label = ttk.Label(frame_transaction,text="หมายเลขการจอง : " + data['Your Booking'].get('Booking number'), font=("Helevetica",size), bootstyle="light")
    hotel_label = ttk.Label(frame_transaction,text="โรงแรม : " + data['Your Booking'].get('Hotel'), font=("Helevetica",size), bootstyle="light")
    room_type_label = ttk.Label(frame_transaction,text="ประเภทห้อง : " + data['Your Booking'].get('Room Type'), font=("Helevetica",size), bootstyle="light")
    amount_label = ttk.Label(frame_transaction,text="จำนวนห้อง : " + str(data['Your Booking'].get('Room Amount')), font=("Helevetica",size), bootstyle="light")
    booking_status_label = ttk.Label(frame_transaction,text="สถานะการจอง : " + data['Your Booking'].get('Status'), font=("Helevetica",size), bootstyle="success")
    booking_checkin_label = ttk.Label(frame_transaction,text="วันที่เช็คอิน : " + data['Your Booking'].get('Date').get('checkin'), font=("Helevetica",size), bootstyle="light")
    booking_checkout_label = ttk.Label(frame_transaction,text="วันที่เช็คเอาท์ : " + (data['Your Booking'].get('Date')).get('checkout'), font=("Helevetica",size), bootstyle="light")

    transaction_method_label = ttk.Label(frame_transaction,text="วิธีชำระเงิน : " + data['Your Booking'].get('Transaction').get('Transaction Method'), font=("Helevetica",size), bootstyle="light")
    transaction_no_label = ttk.Label(frame_transaction,text="หมายเลขการชำระเงิน : " + data['Your Booking'].get('Transaction').get('Transaction number'), font=("Helevetica",size), bootstyle="light")
    transaction_status_label = ttk.Label(frame_transaction,text="สถานะการชำระเงิน : " + data['Your Booking'].get('Transaction').get('Transaction Status'), font=("Helevetica",size), bootstyle="success")
    transaction_date_label = ttk.Label(frame_transaction,text="วันที่ชำระเงิน : " + data['Your Booking'].get('Transaction').get('Transaction Date'), font=("Helevetica",size), bootstyle="light")
    transaction_arg1_label = ttk.Label(frame_transaction,text="ข้อมูล : " , font=("Helevetica",size), bootstyle="light")
    transaction_arg2_label = ttk.Label(frame_transaction,text="ข้อมูล : " , font=("Helevetica",size), bootstyle="light")

    if payment_method.get() == "C":
        transaction_arg1_label.config(text="หมายเลขบัตรเครดิต : " + data['Your Booking'].get('Transaction').get('Credit Card Number'))
        transaction_arg2_label.config(text="หมายเลข CVV : " + data['Your Booking'].get('Transaction').get('Credit Card CVV'))
        
    elif payment_method.get() == "M":
        transaction_arg1_label.config(text="เลขที่บัญชีธนาคาร : " + data['Your Booking'].get('Transaction').get('Customer Bank Account ID'))
        transaction_arg2_label.config(text="ธนาคาร : " + data['Your Booking'].get('Transaction').get('Customer Bank'))

    elif payment_method.get() == "P":
        transaction_arg1_label.config(text="หมายเลข Paypal ลูกค้า : " + data['Your Booking'].get('Transaction').get('Customer Paypal ID'))
        transaction_arg2_label.config(text="ที่อยู่อีเมลลูกค้า : " + data['Your Booking'].get('Transaction').get('Customer Email Address'))
        transaction_arg3_label = ttk.Label(frame_transaction,text="ที่อยู่อีเมลโรงแรม : " + data['Your Booking'].get('Transaction').get('Hotel Email Address'), font=("Helevetica",size), bootstyle="light")
        transaction_arg3_label.grid(row=7,column=1,sticky='w')

    transaction_price_label = ttk.Label(frame_transaction,text="จำนวนเงินรวม : " + str(sum_price.get()) + " บาท", font=("Helevetica",size), bootstyle="light")
    transaction_coupon_id_label = ttk.Label(frame_transaction,text="หมายเลขคูปอง : " + data['Your Booking'].get('Transaction').get('Coupon used').get('coupon id'), font=("Helevetica",size), bootstyle="light")
    transaction_coupon_amount_label = ttk.Label(frame_transaction,text="ส่วนลด : " + str(data['Your Booking'].get('Transaction').get('Coupon used').get('discount amount')) + " บาท", font=("Helevetica",size), bootstyle="light")
    transaction_amount_label = ttk.Label(frame_transaction,text="จำนวนเงินสุทธิ : " + str(data['Your Booking'].get('Transaction').get('Transaction amount')) + " บาท",font=("Helevetica",size), bootstyle="light")

    backward_button = ttk.Button(frame_transaction, text="กลับสู่หน้าหลัก", bootstyle="secondary", command=lambda: backward("home", frame_transaction))

    booking_name_label.grid(row=2,column=0,sticky='w')
    booking_no_label.grid(row=3,column=0,sticky='w')
    hotel_label.grid(row=4,column=0,sticky='w')
    room_type_label.grid(row=5,column=0,sticky='w')
    amount_label.grid(row=6,column=0,sticky='w')
    booking_status_label.grid(row=7,column=0,sticky='w')
    booking_checkin_label.grid(row=9,column=0,sticky='w')
    booking_checkout_label.grid(row=10,column=0,sticky='w')
    
    transaction_method_label.grid(row=2,column=1,sticky='w')
    transaction_no_label.grid(row=3,column=1,sticky='w')
    transaction_status_label.grid(row=4,column=1,sticky='w')
    transaction_date_label.grid(row=5,column=1,sticky='w')
    transaction_arg1_label.grid(row=6,column=1,sticky='w')
    transaction_arg2_label.grid(row=7,column=1,sticky='w')

    transaction_price_label.grid(row=9,column=1,sticky='w')
    transaction_coupon_id_label.grid(row=10,column=1,sticky='w')
    transaction_coupon_amount_label.grid(row=11,column=1,sticky='w')
    transaction_amount_label.grid(row=12,column=1,sticky='w')

    backward_button.grid(row=13,column=0,sticky='w')

    show_page("transaction",frame_method)

def turn_json_to_coupon_list(data):
    output = []
    if 'detail' in data:
        if data['detail'].get('message') == "Please login first":
            return "Loginfirst"
        else:
            return "Cannotopen"
    else:
        for name,content in data.items():
            output.append(content['Coupon id'] + " (" + str(content['Amount']) + ")")
        output.append('None')
    return output

def on_click_confirm_booking_button():
    isclick.set(False)
    payment_title_label.grid(row=0,column=1,pady=20)
    payment_select_label.grid(row=1,column=0,sticky='w',pady=(50,20))
    payment_warning_label.grid(row=1,column=1,sticky='w',padx=50)

    method_select_button1 = ttk.Radiobutton(frame_method,bootstyle="danger", text="Credit Card", variable=payment_method, value="C")
    method_select_button2 = ttk.Radiobutton(frame_method,bootstyle="danger", text="Mobile Banking", variable=payment_method, value="M")
    method_select_button3 = ttk.Radiobutton(frame_method,bootstyle="danger", text="Paypal", variable=payment_method, value="P")
    method_select_button1.grid(row=2,column=0,sticky='w',pady=(0,50))
    method_select_button2.grid(row=3,column=0,sticky='w')
    method_select_button3.grid(row=4,column=0,sticky='w',pady=(50,0))

    payment_process_button = ttk.Button(frame_method,text="ยืนยัน",bootstyle="danger", command=lambda :on_click_payment_process_button(),state="disabled")
    coupon_confirm_button = ttk.Button(frame_method,text="ยืนยันคูปอง",bootstyle="danger", command=lambda :on_click_confirm_coupon_button(coupon_select_combobox.get()[0:4],isclick,payment_process_button),state="disabled")
    method_confirm_button = ttk.Button(frame_method,text="ยืนยันวิธีชำระเงิน",bootstyle="danger", command=lambda :on_click_confirm_method_button(payment_method.get(),transaction_arg1.get(),transaction_arg2.get(),coupon_confirm_button),state="disabled")
    payment_method_button = ttk.Button(frame_method,text="เลือกวิธีชำระเงิน",bootstyle="danger", command=lambda :on_click_confirm_payment_button(method_confirm_button))

    payment_method_button.grid(row=5,column=0,pady=50) 

    if message_error.get() == "Invalid selection method" or message_error.get() == "Invalid argument(s) type" or message_error.get() == 'no matched card':#from press method confirm button
        method_alert_label.grid(row=5,column=1,pady=50)

    payment_arg1_label.grid(row=2,column=1,padx=30, pady=(30,20))
    payment_arg2_label.grid(row=2,column=2,padx=30, pady=(30,20))
    payment_arg1_entry.grid(row=3,column=1,padx=30,pady=(0,50))
    payment_arg2_entry.grid(row=3,column=2,padx=30,pady=(0,50))

    method_confirm_button.grid(row=3,column=3,padx=30,pady=(0,50))
    
    response = requests.get(show_coupon_endpoint)
    data = response.json()

    sum_price_label.grid(row=4,column=1,pady=20)

    if isinstance(turn_json_to_coupon_list(data),str):
        if turn_json_to_coupon_list(data) == "Cannotopen":
            coupon_alert_label.grid(row=6,column=1,pady=20)
    else:
        coupon_id_list = turn_json_to_coupon_list(data).copy()
        coupon_select_combobox = ttk.Combobox(frame_method,bootstyle="danger",values=coupon_id_list)
        coupon_select_combobox.grid(row=4,column=2,padx=20)
    
    coupon_confirm_button.grid(row=4,column=3,padx=20)
    payment_process_button.grid(row=5,column=3)

    backward_button = ttk.Button(frame_method, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("ratelist", frame_method))
    backward_button.grid(row=5,column=2)

    show_page("method",frame_review)

def on_click_choose_room_button(hotel_name,room_type,price):
    if current_firstname.get() == "None" and current_lastname.get() == "None":
        review_alert_label.grid(row=18,column=2,padx=30)
    else:
        payload = {
            "hotel_name" : hotel_name,
            "checkin" : date_checkin.get(),
            "checkout" : date_checkout.get(),
            "amount" : room_amount.get(),
            "room_type" : room_type
        }
        response = requests.post(booking_review_endpoint, json=payload)
        data = response.json()
        booking_detail_label.grid(row=0,pady=20)

        room_type_label = ttk.Label(frame_review,text="ประเภทห้อง : " + data['room type'], font=("Helvetica", 16), bootstyle="light")
        check_in_label = ttk.Label(frame_review,text="วันที่เช็คอิน : " + data['checkin_date'],font=("Helvetica", 16), bootstyle="light")
        check_out_label = ttk.Label(frame_review,text="วันที่เช็คเอาท์ : " + data['checkout_date:'],font=("Helvetica", 16), bootstyle="light")
        room_amount_label = ttk.Label(frame_review,text="จำนวนห้อง : " + str(data['amount']),font=("Helvetica", 16), bootstyle="light")
        price_pernight_label = ttk.Label(frame_review,text="ราคาห้องพักต่อคืน : " + str(price),font=("Helvetica", 16), bootstyle="light")
        night_amount_label = ttk.Label(frame_review,text="จำนวนคืนที่เข้าพัก : " + str(data['night']),font=("Helvetica", 16), bootstyle="light")
        sum_price_label = ttk.Label(frame_review,text="ราคารวม : "+str(data['summary of charges']),font=("Helevetica", 16),bootstyle="light")

        sum_price.set(int(data['summary of charges']))

        room_type_label.grid(row=1,column=0,pady=(0,30),sticky='w')
        check_in_label.grid(row=2,column=0,pady=(0,30),sticky='w')
        check_out_label.grid(row=3,column=0,pady=(0,30),sticky='w')
        room_amount_label.grid(row=4,column=0,pady=(0,30),sticky='w')
        price_pernight_label.grid(row=5,column=0,pady=(0,30),sticky='w')
        night_amount_label.grid(row=6,column=0,pady=(0,30),sticky='w')
        sum_price_label.grid(row=7,column=0,pady=(0,30),sticky='w')

        confirm_button = ttk.Button(frame_review, text="ยืนยันการจอง", bootstyle="danger",command=on_click_confirm_booking_button)
        confirm_button.grid(row=7,column=1,padx=20)

        backward_button = ttk.Button(frame_review, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("ratelist", frame_review))
        backward_button.grid(row=7, column=2,pady=20)

        show_page("review",frame_ratelist)

def on_click_choose_hotel_button(hotel_name,row):
    payload = {
        "hotel_name" : hotel_name,
        "checkin" : date_checkin.get(),
        "checkout" : date_checkout.get(),
        "amount" : room_amount.get()
    }
    response = requests.post(hotel_ratelist_endpoint, json=payload)
    data = response.json()
    
    if 'detail' in data:
        room_amount_alert_label.grid(row=row+1,column=2)
    else:
        ratelist_title_label.configure(text=hotel_name)
        ratelist_title_label.grid(row=0,column=1,pady=20)
        current_row = 1
        for name,content in data.items():
            if name == "small room type":
                room_image = Image.open("images\\small_room_type.jpg")
                resize_room_image = room_image.resize((200,100))
                room_imagetk = ImageTk.PhotoImage(resize_room_image)
                room_image_label = ttk.Label(frame_ratelist,image=room_imagetk)
            elif name == "medium room type":
                room_image = Image.open("images\\medium_room_type.jpg")
                resize_room_image = room_image.resize((200,100))
                room_imagetk = ImageTk.PhotoImage(resize_room_image)
                room_image_label = ttk.Label(frame_ratelist,image=room_imagetk)
            elif name == "large room type":
                room_image = Image.open("images\\large_room_type.jpg")
                resize_room_image = room_image.resize((200,100))
                room_imagetk = ImageTk.PhotoImage(resize_room_image)
                room_image_label = ttk.Label(frame_ratelist,image=room_imagetk)
            elif name == "message":#no room available
                room_alert.grid(padx=5)
                break
            room_image_label.room_image = room_imagetk
            room_image_label.grid(row=current_row,column=0,rowspan=2,columnspan=2)
   
            room_type_label = ttk.Label(frame_ratelist,text=name,font=("Helvetica", 16), bootstyle="light")
            room_price_label = ttk.Label(frame_ratelist,text="Price per 1 night : " + str(content['price per night']),bootstyle="light")
            choose_button = ttk.Button(frame_ratelist, text="เลือก",command=lambda room_type = name[0:-10],price = content['price per night']: on_click_choose_room_button(hotel_name,room_type,price),bootstyle="danger")#command = none
            room_type_label.grid(row=current_row, column=2,sticky="w")
            choose_button.grid(row=current_row, column=3,padx=100, sticky="w")
            room_price_label.grid(row=current_row+1, column=2,pady=(0,60),sticky="w")
            current_row += 3

        backward_button = ttk.Button(frame_ratelist, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("search_hotel", frame_ratelist))
        backward_button.grid(row=20, column=1, pady=100)

        show_page("ratelist",frame_hotel)
        
def on_click_search_hotel_button():
    payload = {
        "country": country.get(),  
        "province": province.get()
    }
    response = requests.post(search_hotel_endpoint, json=payload)
    if response.ok:
        data = response.json()
        if 'message' in data:
            search_hotel_alert.grid(row=4, pady=10, columnspan=2)
        else:
            result_hotel_label.grid(row=0,column=0, pady=20)
            date_checkin_label.grid(row=1, column=0)
            date_checkout_label.grid(row=1, column=1)
            room_amount_label.grid(row=1, column=2, sticky="w")

            date_checkin_entry.grid(row=2, column=0, sticky="w",padx=(0,100))
            date_checkout_entry.grid(row=2, column=1, sticky="w")
            room_amount_entry.grid(row=2, column=2, sticky="w",padx=(100,0))

            row = 3
            for index_hotel in range(len(data['hotel_list'])):
                isclick_button_list.append(False)
                hotel_name_label = ttk.Label(frame_hotel, text=""+str(data['hotel_list'][index_hotel]["hotel_name"]), font=("Helvetica", 18), bootstyle="light")
                choose_button = ttk.Button(frame_hotel, text="เลือก",command=lambda index=index_hotel: on_click_choose_hotel_button(data['hotel_list'][index]["hotel_name"],row),bootstyle="danger")
                change_hotel_button = ttk.Button(frame_hotel,text="ชื่นชอบโรงแรม", command=lambda index=index_hotel:on_click_confirm_change_hotel_button(data['hotel_list'][index]["hotel_name"],row,index), bootstyle="danger")
                hotel_name_label.grid(row=row, column=0, ipady=20, sticky='w')
                choose_button.grid(row=row, column=1,sticky='e',pady=30)
                change_hotel_button.grid(row=row,column=2,pady=30)
                label_hotel_excess.append(hotel_name_label)
                label_hotel_excess.append(choose_button)
                row += 1
            hotel_backward.grid(row=row+2, column=0, pady=100, columnspan=2)

            show_page("hotel", frame_search_hotel)
            
def on_click_search_hotel_backward_button():
    if current_firstname.get() == "None" and current_lastname.get() == "None":
        backward("home",frame_search_hotel)
    else:
        backward("account",frame_search_hotel)

def on_click_search_reservation_backward_button():
    if current_firstname.get() == "None" and current_lastname.get() == "None":
        backward("home",frame_search_reservation)
    else:
        backward("account",frame_search_reservation)

def on_click_search_reservation_button():
    year, month, day = check_in_date.entry.get().split("-")
    Date = date(int(year), int(month), int(day)).strftime("%d-%m-%Y")
    payload = {
        "firstname": firstname.get(),
        "lastname": lastname.get(),
        "booking_no": booking_no.get(),
        "check_in_date": Date
    }
    response = requests.post(search_reservation_endpoint, json=payload)
    if response.ok:
        data = response.json()
        title_label = ttk.Label(frame_reservation, text="ผลการค้นหาการจอง", font=("Helvetica", 36), bootstyle="light")
        title_label.grid(pady=30)
        firstname_label = ttk.Label(frame_reservation, text="ชื่อจริง : "+ str(data["firstname"]), font=("Helvetica", 18), bootstyle="danger")
        firstname_label.grid(row=1, column=0, padx=10, ipady=10)
        lastname_label = ttk.Label(frame_reservation, text="นามสกุล : "+ str(data["lastname"]), font=("Helvetica", 18), bootstyle="danger")
        lastname_label.grid(row=2, column=0, padx=10, ipady=10)
        booking_no_label = ttk.Label(frame_reservation, text="หมายเลขการจอง : "+ str(data["booking_no"]), font=("Helvetica", 18), bootstyle="danger")
        booking_no_label.grid(row=3, column=0, padx=10, ipady=10)
        hotel_label = ttk.Label(frame_reservation, text="โรงเเรม : "+ str(data["hotel"]["hotel_name"]), font=("Helvetica", 18), bootstyle="danger")
        hotel_label.grid(row=4, column=0, padx=10, ipady=10)
        type_label = ttk.Label(frame_reservation, text="ประเภทห้อง : "+ str(data["room_type"]), font=("Helvetica", 18), bootstyle="danger")
        type_label.grid(row=5, column=0, padx=10, ipady=10)
        quantity_label = ttk.Label(frame_reservation, text="จำนวนห้อง : "+ str(data["room_quantity"]), font=("Helvetica", 18), bootstyle="danger")
        quantity_label.grid(row=6, column=0, padx=10, ipady=10)
        check_in_date_label = ttk.Label(frame_reservation, text="วันที่เช็คอิน : "+ str(data["check_in_date"]), font=("Helvetica", 18), bootstyle="danger")
        check_in_date_label.grid(row=7, column=0, padx=10, ipady=10)
        check_out_date_label = ttk.Label(frame_reservation, text="วันที่เช็คเอาท์ : "+ str(data["check_out_date"]), font=("Helvetica", 18), bootstyle="danger")
        check_out_date_label.grid(row=8, column=0, padx=10, ipady=10)
        status_label = ttk.Label(frame_reservation, text="สถานะ : "+ str(data["status"]), font=("Helvetica", 18), bootstyle="danger")
        status_label.grid(row=9, column=0,padx=10, ipady=10)
        backward_button = ttk.Button(frame_reservation, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("search_reservation", frame_reservation))
        backward_button.grid(row=10, column=0, pady=50, columnspan=2)
        label_reservation_excess.append(title_label)
        label_reservation_excess.append(firstname_label)
        label_reservation_excess.append(lastname_label)
        label_reservation_excess.append(booking_no_label)
        label_reservation_excess.append(hotel_label)
        label_reservation_excess.append(type_label)
        label_reservation_excess.append(quantity_label)
        label_reservation_excess.append(check_in_date_label)
        label_reservation_excess.append(check_out_date_label)
        label_reservation_excess.append(status_label)
        label_reservation_excess.append(backward_button)
        show_page("reservation", frame_search_reservation)
    else:
        data = response.json()
        search_reservation_alert.grid(row=6, pady=10, columnspan=2)
        
def on_click_login_button():
    payload = {
        "email": email.get(),
        "password": password.get(),
    }
    response = requests.post(login_endpoint, json=payload)
    if response.ok:
        data = response.json()
        current_firstname.set(data["first_name"])
        current_lastname.set(data["last_name"])
        if data["message"] == "Customer login Successfully":
            account_title_label_customer.configure(text=f"{current_firstname.get()}"+ " " + f"{current_lastname.get()}")
            account_title_label_customer.grid(row=0, pady=30)
            search_hotel_button.grid(row=1, pady=30)
            search_reservation_button.grid(row=2, pady=30)
            customer_cancel_booking_button.grid(row=3,pady=30)
            personal_information_button.grid(row=4, pady=30)
            my_travelling_button.grid(row=5, pady=30)
            my_favorite_hotel_button.grid(row=6, pady=30)
            logout_button_customer.grid(row=7, pady=30)
            show_page("account", frame_login)
        else:
            account_title_label_admin.configure(text=f"{current_firstname.get()}" + " " + f"{current_lastname.get()}")
            account_title_label_admin.grid(row=0, pady=30)
            add_hotel_button.grid(row=1, pady=30)
            delete_hotel_button.grid(row=2, pady=30)
            admin_cancel_booking_button.grid(row=3, pady=30)
            logout_button_admin.grid(row=4, pady=20)
            show_page("admin", frame_login)
    else:
        data = response.json()
        data = data["detail"]
        data = data["message"]
        if(data == "Wrong Password"):
            login_alert1.grid(row=4, column=0, pady=10, columnspan=2)
        else:
            login_alert2.grid(row=4, column=0, pady=10, columnspan=2)

def on_click_logout_button():
    response = requests.put(logout_endpoint)
    if response.ok:
        current_firstname.set(None)
        current_lastname.set(None)
        email.set("")
        password.set("")
        show_page("login", frame_account)

def on_click_logout_button2():
    response = requests.put(logout_endpoint)
    current_firstname.set(None)
    current_lastname.set(None)
    email.set("")
    password.set("")
    if response.ok:
        show_page("login", frame_admin)

def on_click_register_button():
    year, month, day = birthday.entry.get().split("-")
    birthday_date = date(int(year), int(month), int(day)).strftime("%d-%m-%Y")
    payload = {
        "firstname": firstname.get(),
        "lastname": lastname.get(),
        "country": country.get(),
        "province": province.get(),
        "country": country.get(),
        "zip_code": zip_code.get(),
        "birthday": birthday_date, 
        "phone_number": phone_number.get(),
        "email": email.get(),
        "password": password.get(),
        "confirm_password": confirm_password.get()
    }
    response = requests.post(register_endpoint, json=payload)
    if response.ok:
        show_page("login", frame_register)
    else:
        data = response.json()
        data = data["detail"]
        data = data["message"]
        if(data == "Email already exist"):
            alert_register1.grid(row=12, column=0, pady=8, columnspan=2)
        else:
            alert_register2.grid(row=12, column=0, pady=8, columnspan=2)

def on_click_personal_information_button():
    response = requests.get(get_personal_information_endpoint)
    if response.ok:
        data = response.json()
        title_label = ttk.Label(frame_personal_information, text="ข้อมูลส่วนตัว", font=("Helvetica", 36), bootstyle="light")
        title_label.grid(pady=30)
        firstname_label = ttk.Label(frame_personal_information, text="ชื่อจริง : "+ str(data["firstname"]), font=("Helvetica", 18), bootstyle="danger")
        firstname_label.grid(row=1, column=0, padx=10, ipady=10)
        lastname_label = ttk.Label(frame_personal_information, text="นามสกุล : "+ str(data["lastname"]), font=("Helvetica", 18), bootstyle="danger")
        lastname_label.grid(row=2, column=0, padx=10, ipady=10)
        country_label = ttk.Label(frame_personal_information, text="ประเทศ : "+ str(data["country"]), font=("Helvetica", 18), bootstyle="danger")
        country_label.grid(row=3, column=0, padx=10, ipady=10)
        province_label = ttk.Label(frame_personal_information, text="จังหวัด : "+ str(data["province"]), font=("Helvetica", 18), bootstyle="danger")
        province_label.grid(row=4, column=0, padx=10, ipady=10)
        zip_code_label = ttk.Label(frame_personal_information, text="รหัสไปรษณีย์ : "+ str(data["zip_code"]), font=("Helvetica", 18), bootstyle="danger")
        zip_code_label.grid(row=5, column=0, padx=10, ipady=10)
        birthday_label = ttk.Label(frame_personal_information, text="วันเกิด : "+ str(data["birthday"]), font=("Helvetica", 18), bootstyle="danger")
        birthday_label.grid(row=6, column=0, padx=10, ipady=10)
        phone_number_label = ttk.Label(frame_personal_information, text="เบอร์โทรศัพท์ : "+ str(data["phone_number"]), font=("Helvetica", 18), bootstyle="danger")
        phone_number_label.grid(row=7, column=0, padx=10, ipady=10)
        backward_label = ttk.Button(frame_personal_information, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("account", frame_personal_information))
        backward_label.grid(row=8, column=0, pady=200, columnspan=2)
        label_personal_information_excess.append(title_label)
        label_personal_information_excess.append(firstname_label)
        label_personal_information_excess.append(lastname_label)
        label_personal_information_excess.append(country_label)
        label_personal_information_excess.append(province_label)
        label_personal_information_excess.append(zip_code_label)
        label_personal_information_excess.append(birthday_label)
        label_personal_information_excess.append(phone_number_label)
        label_personal_information_excess.append(backward_label)
        show_page("personal_information", frame_account)

def on_click_my_travelling_button():
    response = requests.get(get_my_travelling_endpoint)
    if response.ok:
        data = response.json()
        arriving = data["arriving"]
        cancelled = data["cancelled"]
        column = 0
        if(len(arriving) != 0):
            for index_reservation in range(len(arriving)):
                firstname_label = ttk.Label(arriving_tab, text="ชื่อจริง : "+ str(arriving[index_reservation]["firstname"]), font=("Helvetica", 14), bootstyle="light")
                firstname_label.grid(row=0, column=column, padx=20, ipady=10)
                lastname_label = ttk.Label(arriving_tab, text="นามสกุล : "+ str(arriving[index_reservation]["lastname"]), font=("Helvetica", 14), bootstyle="light")
                lastname_label.grid(row=1, column=column, padx=20, ipady=10)
                booking_no_label = ttk.Label(arriving_tab, text="หมายเลขการจอง : "+ str(arriving[index_reservation]["booking_no"]), font=("Helvetica", 14), bootstyle="light")
                booking_no_label.grid(row=2, column=column, padx=20, ipady=10)
                country_label = ttk.Label(arriving_tab, text="โรงเเรม : "+ str(arriving[index_reservation]["hotel"]["hotel_name"]), font=("Helvetica", 14), bootstyle="light")
                country_label.grid(row=3, column=column, padx=20, ipady=10)
                type_label = ttk.Label(arriving_tab, text="ประเภทห้อง : "+ str(arriving[index_reservation]["room_type"]), font=("Helvetica", 14), bootstyle="light")
                type_label.grid(row=4, column=column, padx=20, ipady=10)
                quantity_label = ttk.Label(arriving_tab, text="จำนวนห้อง : "+ str(arriving[index_reservation]["room_quantity"]), font=("Helvetica", 14), bootstyle="light")
                quantity_label.grid(row=5, column=column, padx=20, ipady=10)
                check_in_date_label = ttk.Label(arriving_tab, text="วันที่เช็คอิน : "+ str(arriving[index_reservation]["check_in_date"]), font=("Helvetica", 14), bootstyle="light")
                check_in_date_label.grid(row=6, column=column, padx=20, ipady=10)
                check_out_date_label = ttk.Label(arriving_tab, text="วันที่เช็คเอาท์ : "+ str(arriving[index_reservation]["check_out_date"]), font=("Helvetica", 14), bootstyle="light")
                check_out_date_label.grid(row=7, column=column, padx=20, ipady=10)
                column += 1
                label_my_travelling_excess.append(firstname_label)
                label_my_travelling_excess.append(lastname_label)
                label_my_travelling_excess.append(booking_no_label)
                label_my_travelling_excess.append(country_label)
                label_my_travelling_excess.append(type_label)
                label_my_travelling_excess.append(quantity_label)
                label_my_travelling_excess.append(check_in_date_label)
                label_my_travelling_excess.append(check_out_date_label)
        else:
            result_my_travelling = ttk.Label(arriving_tab, text="ไม่พบข้อมูล", font=("Helvetica", 16), bootstyle="danger")
            result_my_travelling.grid(row=0, column=0, padx=20, ipady=30)
            label_my_travelling_excess.append(result_my_travelling)
        column = 0
        if(len(cancelled) != 0):
            for index_reservation in range(len(cancelled)):
                firstname_label = ttk.Label(cancelled_tab, text="ชื่อจริง : "+ str(cancelled[index_reservation]["firstname"]), font=("Helvetica", 14), bootstyle="danger")
                firstname_label.grid(row=0, column=column, padx=20, ipady=10)
                lastname_label = ttk.Label(cancelled_tab, text="นามสกุล : "+ str(cancelled[index_reservation]["lastname"]), font=("Helvetica", 14), bootstyle="danger")
                lastname_label.grid(row=1, column=column, padx=20, ipady=10)
                booking_no_label = ttk.Label(cancelled_tab, text="หมายเลขการจอง : "+ str(cancelled[index_reservation]["booking_no"]), font=("Helvetica", 14), bootstyle="danger")
                booking_no_label.grid(row=2, column=column, padx=20, ipady=10)
                country_label = ttk.Label(cancelled_tab, text="โรงเเรม : "+ str(cancelled[index_reservation]["hotel"]["hotel_name"]), font=("Helvetica", 14), bootstyle="danger")
                country_label.grid(row=3, column=column, padx=20, ipady=10)
                type_label = ttk.Label(cancelled_tab, text="ประเภทห้อง : "+ str(cancelled[index_reservation]["room_type"]), font=("Helvetica", 14), bootstyle="danger")
                type_label.grid(row=4, column=column, padx=20, ipady=10)
                quantity_label = ttk.Label(cancelled_tab, text="จำนวนห้อง : "+ str(cancelled[index_reservation]["room_quantity"]), font=("Helvetica", 14), bootstyle="danger")
                quantity_label.grid(row=5, column=column, padx=20, ipady=10)
                check_in_date_label = ttk.Label(cancelled_tab, text="วันที่เช็คอิน : "+ str(cancelled[index_reservation]["check_in_date"]), font=("Helvetica", 14), bootstyle="danger")
                check_in_date_label.grid(row=6, column=column, padx=20, ipady=10)
                check_out_date_label = ttk.Label(cancelled_tab, text="วันที่เช็คเอาท์ : "+ str(cancelled[index_reservation]["check_out_date"]), font=("Helvetica", 14), bootstyle="danger")
                check_out_date_label.grid(row=7, column=column, padx=20, ipady=10)
                column += 1
                label_my_travelling_excess.append(firstname_label)
                label_my_travelling_excess.append(lastname_label)
                label_my_travelling_excess.append(booking_no_label)
                label_my_travelling_excess.append(country_label)
                label_my_travelling_excess.append(type_label)
                label_my_travelling_excess.append(quantity_label)
                label_my_travelling_excess.append(check_in_date_label)
                label_my_travelling_excess.append(check_out_date_label)
        else:
            result_my_travelling = ttk.Label(cancelled_tab, text="ไม่พบข้อมูล", font=("Helvetica", 16), bootstyle="danger")
            result_my_travelling.grid(row=0, column=0, padx=20, ipady=30)
            label_my_travelling_excess.append(result_my_travelling)
        arriving_button = ttk.Button(arriving_tab, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("account", my_travelling_notebook))
        arriving_button.grid(row=8, column=0, pady=275, sticky="w",)
        cancelled_button = ttk.Button(cancelled_tab, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("account", my_travelling_notebook))
        cancelled_button.grid(row=8, column=0, pady=275, sticky="w")
        label_my_travelling_excess.append(arriving_button)
        label_my_travelling_excess.append(cancelled_button)
        show_page("my_travelling", frame_account)
        
def on_click_my_favorite_hotel_button():
    response = requests.get(get_my_favorite_hotel_end_point)
    if response.ok:
        data = response.json()
        title_label = ttk.Label(frame_my_favorite_hotel, text="โรงเเรมที่ฉันชื่นชอบ", font=("Helvetica", 36), bootstyle="light")
        title_label.grid(pady=30)
        if 'message' in data:
            my_favorite_hotel_label = ttk.Label(frame_my_favorite_hotel, text="ไม่มีโรงเเรมที่คุณชื่นชอบ", font=("Helvetica", 18), bootstyle="danger")
            my_favorite_hotel_label.grid(row=1, column=0, pady=10)
            label_my_favorite_hotel_excess.append(my_favorite_hotel_label)
        else:
            data = data['my_fav_hotel']
            row = 1
            for index_my_favorite_hotel in range(len(data)):
                my_favorite_hotel_label = ttk.Label(frame_my_favorite_hotel, text="โรงเเรม : "+ str(data[index_my_favorite_hotel]["hotel_name"]), font=("Helvetica", 18), bootstyle="danger")
                my_favorite_hotel_label.grid(row=row, column=0, padx=20, ipady=10)
                row += 1
                label_my_favorite_hotel_excess.append(my_favorite_hotel_label)
        backward_button = ttk.Button(frame_my_favorite_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("account", frame_my_favorite_hotel))
        backward_button.grid(row=3, column=0, pady=100)
        label_my_favorite_hotel_excess.append(title_label)
        label_my_favorite_hotel_excess.append(backward_button)
        show_page("my_favorite_hotel", frame_account)

def on_click_confirm_change_hotel_button(hotel_name,row,index):
    payload = {
        "hotel_name" : hotel_name
    }
    if current_firstname.get() != "None" and current_lastname.get() != "None":
        if isclick_button_list[index] == False:
            response = requests.post(add_my_favorite_hotel_endpoint,json=payload)
            data = response.json()
            if data['message'] == 'Add Successfully':
                change_myfavhotel_success_label.configure(text="เพิ่มโรงแรมที่ฉันชื่นชอบแล้ว")
                change_myfavhotel_success_label.grid(row=row+1,column=0,sticky="w")
                isclick_button_list[index] = True

        elif isclick_button_list[index] == True:
            response = requests.post(remove_my_favorite_hotel_endpoint,json=payload)
            data = response.json()
            print(data)
            if data['message'] == 'Removed Successfully':
                change_myfavhotel_success_label.configure(text="นำโรงแรมออกจากโรงแรมที่ฉันชื่นชอบแล้ว")
                change_myfavhotel_success_label.grid(row=row+1,column=0,sticky="w")
                isclick_button_list[index] = False

def on_click_admin_add_hotel_button():
    payload = {
        "name": hotel_name.get(),
        "location": {"country": country.get(), "province": province.get()},
        "hotel_email": hotel_email.get()
    }
    response = requests.post(admin_add_hotel_endpoint, json=payload)
    if response.ok:
        alert = ttk.Label(frame_admin_add_hotel, text="เพิ่มโรงเเรมสำเร็จ", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=6, column=0, padx=10, ipady=10,columnspan=2)
    else:
        alert = ttk.Label(frame_admin_add_hotel, text="ใส่ข้อมูลไม่ถูกต้อง", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=6, column=0, padx=10, ipady=10, columnspan=2)
    label_admin_add_hotel_excess.append(alert)

def on_click_admin_delete_hotel_button():
    payload = {
        "hotel_name": hotel_name.get(),
    }
    response = requests.delete(admin_delete_hotel_endpoint, json=payload)
    if response.ok:
        alert = ttk.Label(frame_admin_delete_hotel, text="ลบโรงเเรมสำเร็จ", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=3, column=0, padx=10, ipady=10,columnspan=2)
    else:
        alert = ttk.Label(frame_admin_delete_hotel, text="ใส่ข้อมูลไม่ถูกต้อง", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=3, column=0, padx=10, ipady=10, columnspan=2)
    label_admin_delete_hotel_excess.append(alert)

def on_click_admin_cancel_booking_button():
    payload = {
        "booking_no": booking_no.get()
    }
    response = requests.put(admin_cancel_booking_endpoint, json=payload)
    if response.ok:
        alert = ttk.Label(frame_admin_cancel_booking, text="ยกเลิกการจองสำเร็จ", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=3, column=0, padx=10, ipady=10,columnspan=2)
    else:
        alert = ttk.Label(frame_admin_cancel_booking, text="ใส่ข้อมูลไม่ถูกต้อง", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=3, column=0, padx=10, ipady=10, columnspan=2)
    label_admin_cancel_booking_excess.append(alert)

def on_click_customer_cancel_booking_button():
    payload = {
        "booking_no": booking_no.get()
    }
    response = requests.put(customer_cancel_booking_endpoint, json=payload)
    data = response.json()
    if response.ok:
        alert = ttk.Label(frame_customer_cancel_booking, text="ยกเลิกการจองสำเร็จ", font=("Helvetica", 14), bootstyle="danger")
        alert.grid(row=3, column=0, padx=10, ipady=10,columnspan=2)
    else:
        if data['detail'].get('message') == 'no room has this interval':
            alert = ttk.Label(frame_customer_cancel_booking, text="ไม่สามารถยกเลิกการจองได้", font=("Helvetica", 14), bootstyle="danger")
            alert.grid(row=3, column=0, padx=10, ipady=10, columnspan=2)
        else:
            alert = ttk.Label(frame_customer_cancel_booking, text="ใส่ข้อมูลไม่ถูกต้อง", font=("Helvetica", 14), bootstyle="danger")
            alert.grid(row=3, column=0, padx=10, ipady=10, columnspan=2)
    label_alert_excess.append(alert)
        
province = StringVar()
country = StringVar()
firstname = StringVar()
lastname = StringVar()
current_firstname = StringVar()
current_lastname = StringVar()
booking_no = StringVar()
email = StringVar()     
password = StringVar()
confirm_password = StringVar()
zip_code = StringVar()
phone_number = StringVar()
date_checkin = StringVar()
date_checkout = StringVar()
room_amount = IntVar()
sum_price = IntVar()
payment_method = StringVar()
transaction_arg1 = StringVar()
transaction_arg2 = StringVar()
message_error = StringVar()
isclick = BooleanVar()
row_arrange = IntVar()
hotel_name = StringVar()
hotel_email = StringVar()

current_firstname.set(None)
current_lastname.set(None)
ttk.Label(frame_home, text="เเอปจองโรงเเรม", font=("Helvetica", 36), bootstyle="light").pack(pady=30)
ttk.Button(frame_home, text="สมัครสมาชิก", command=lambda: show_page("register"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="เข้าสู่ระบบ", command=lambda: show_page("login"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="ค้นหาโรงเเรม", command=lambda: show_page("search_hotel"), bootstyle="danger").pack(pady=30)
ttk.Button(frame_home, text="ค้นหาการจอง", command=lambda: show_page("search_reservation"), bootstyle="danger").pack(pady=30)

ttk.Label(frame_register, text="สมัครสมาชิก", font=("Helvetica", 36), bootstyle="light").grid(pady=25, columnspan=2)
ttk.Label(frame_register, text="ชื่อจริง:", font=("Helvetica", 14), bootstyle="light").grid(row=1, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=firstname, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_register, text="นามสกุล:", font=("Helvetica", 14), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=lastname, width=20).grid(row=2, column=1, padx=10)
ttk.Label(frame_register, text="ประเทศ:", font=("Helvetica", 14), bootstyle="light").grid(row=3, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=country, width=20).grid(row=3, column=1, padx=10)
ttk.Label(frame_register, text="จังหวัด :", font=("Helvetica", 14), bootstyle="light").grid(row=4, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=province, width=20).grid(row=4, column=1, padx=10)
ttk.Label(frame_register, text="รหัสไปรษณีย์ :", font=("Helvetica", 14), bootstyle="light").grid(row=5, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=zip_code, width=20).grid(row=5, column=1, padx=10)
ttk.Label(frame_register, text="วันเกิด:", font=("Helvetica", 14), bootstyle="light").grid(row=6, column=0, padx=10, ipady=10)
birthday = ttk.DateEntry(frame_register, dateformat="%Y-%m-%d", bootstyle="danger", startdate=date.today())
birthday.grid(row=6, column=1, padx=10)
ttk.Label(frame_register, text="เบอร์โทรศัพท์ :", font=("Helvetica", 14), bootstyle="light").grid(row=7, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=phone_number, width=20).grid(row=7, column=1, padx=10)
ttk.Label(frame_register, text="อีเมล:", font=("Helvetica", 14), bootstyle="light").grid(row=8, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=email, width=20).grid(row=8, column=1, padx=10)
ttk.Label(frame_register, text="รหัสผ่าน:", font=("Helvetica", 14), bootstyle="light").grid(row=9, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=password, width=20).grid(row=9, column=1, padx=10)
ttk.Label(frame_register, text="ยืนยันรหัสผ่าน:", font=("Helvetica", 14), bootstyle="light").grid(row=10, column=0, padx=10, ipady=10)
ttk.Entry(frame_register, textvariable=confirm_password, width=20).grid(row=10, column=1, padx=10)
ttk.Button(frame_register, text="สมัครสมาชิก", bootstyle="danger", command=on_click_register_button).grid(row=11, column=0, pady=15, columnspan=2)
ttk.Button(frame_register, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home", frame_register)).grid(row=13, pady=15, columnspan=2)
alert_register1 = ttk.Label(frame_register, text="อีเมลนี้มีผู้ใช้งานเเล้ว", font=("Helvetica", 14), bootstyle="danger")
alert_register2 = ttk.Label(frame_register, text="รหัสผ่านไม่ตรงกัน", font=("Helvetica", 14), bootstyle="danger")
label_alert_excess.append(alert_register1)
label_alert_excess.append(alert_register2)

ttk.Label(frame_login, text="เข้าสู่ระบบ", font=("Helvetica", 36), bootstyle="light").grid(ipady=30, columnspan=2)
ttk.Label(frame_login, text="อีเมล :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=20)
ttk.Entry(frame_login, textvariable=email, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_login, text="รหัสผ่าน :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_login, textvariable=password, width=20).grid(row=2, column=1, padx=10)
ttk.Button(frame_login, text="เข้าสู่ระบบ", bootstyle="danger", command=on_click_login_button).grid(row=3, column=0, pady=20, columnspan=2)
ttk.Button(frame_login, text="ย้อนกลับ", bootstyle="secondary", command=lambda: show_page("home", frame_login)).grid(row=5, column=0, pady=300, columnspan=2)
login_alert1 = ttk.Label(frame_login, text="รหัสผ่านไม่ถูกต้อง", font=("Helvetica", 18), bootstyle="danger")
login_alert2 = ttk.Label(frame_login, text="ไม่มีอีเมลผู้ใช้งานนี้", font=("Helvetica", 18), bootstyle="danger")
label_alert_excess.append(login_alert1)
label_alert_excess.append(login_alert2)

ttk.Label(frame_search_hotel, text="ค้นหาโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(row=0, column=0, ipady=30, columnspan=2)
ttk.Label(frame_search_hotel, text="ประเทศ :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=30)
ttk.Entry(frame_search_hotel, textvariable=country, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_search_hotel, text="จังหวัด :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_search_hotel, textvariable=province, width=20).grid(row=2, column=1, padx=10)
ttk.Button(frame_search_hotel, text="ค้นหาโรงเเรม", bootstyle="danger", command=on_click_search_hotel_button).grid(row=3, column=0, pady=20, columnspan=2)
ttk.Button(frame_search_hotel, text="ย้อนกลับ", bootstyle="secondary", command=on_click_search_hotel_backward_button).grid(row=5, column=0, pady=275, columnspan=2)
search_hotel_alert = ttk.Label(frame_search_hotel, text="ไม่พบโรงเเรมที่คุณต้องการ", font=("Helvetica", 18), bootstyle="danger")
label_alert_excess.append(search_hotel_alert)

result_hotel_label = ttk.Label(frame_hotel, text="ผลการค้นหาโรงเเรม", font=("Helvetica", 36), bootstyle="light")
date_checkin_label = ttk.Label(frame_hotel, text="วันที่เช็คอิน", font=("Helvetica", 10), bootstyle="light")
date_checkout_label = ttk.Label(frame_hotel, text="วันที่เช็คเอาท์", font=("Helvetica", 10), bootstyle="light")
room_amount_label = ttk.Label(frame_hotel, text="จำนวนห้อง", font=("Helvetica", 10), bootstyle="light")
date_checkin_entry = ttk.DateEntry(frame_hotel,dateformat="%Y-%m-%d")
date_checkout_entry = ttk.DateEntry(frame_hotel,dateformat="%Y-%m-%d")
date_checkin_entry.entry.configure(textvariable=date_checkin)
date_checkout_entry.entry.configure(textvariable=date_checkout)
room_amount_entry = ttk.Entry(frame_hotel,textvariable=room_amount,width=2)
change_myfavhotel_success_label = ttk.Label(frame_hotel,text="โรงแรมที่ฉันชื่นชอบแล้ว", font=("Helvetica", 10), bootstyle="success")
label_alert_excess.append(search_hotel_alert)
hotel_backward = ttk.Button(frame_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("search_hotel", frame_hotel))
room_amount_alert_label = ttk.Label(frame_hotel, text="ข้อมูลวันหรือจำนวนห้องไม่ถูกต้อง", font=("Helvetica", 10), bootstyle="light")
label_alert_excess.append(room_amount_alert_label)

ratelist_title_label = ttk.Label(frame_ratelist,text="โรงแรม",font=("Helvetica", 36), bootstyle="light")
room_alert = ttk.Label(frame_ratelist, text="โรงแรมนี้ห้องเต็มแล้ว", font=("Helevetica",24), bootstyle="light")
review_alert_label = ttk.Label(frame_ratelist,text="กรุณาล็อคอินก่อนทำการจองห้องพัก",font=("Helevetica",16), bootstyle="danger")
label_alert_excess.append(review_alert_label)

booking_detail_label = ttk.Label(frame_review, text="รายละเอียดการจอง", font=("Helevetica",36), bootstyle="light")

payment_title_label = ttk.Label(frame_method,text="ข้อมูลการชำระเงิน", font=("Helevetica",36), bootstyle="light")
payment_select_label = ttk.Label(frame_method,text="เลือกวิธีชำระเงิน :",font=("Helevetica",10),bootstyle="light")
payment_arg1_label = ttk.Label(frame_method,text="ข้อมูล",font=("Helevetica",10),bootstyle="light")
payment_arg2_label = ttk.Label(frame_method,text="ข้อมูล",font=("Helevetica",10),bootstyle="light")
payment_arg1_entry = ttk.Entry(frame_method, textvariable=transaction_arg1, width=20)
payment_arg2_entry = ttk.Entry(frame_method, textvariable=transaction_arg2, width=20)
payment_warning_label = ttk.Label(frame_method,text="โปรดกรอกข้อมูลอย่างระมัดระวัง",font=("Helevetica",10),bootstyle="light")
sum_price_label = ttk.Label(frame_method,text="ราคารวม : ",font=("Helevetica",10),bootstyle="light")

method_alert_label = ttk.Label(frame_method,text="กรุณาตรวจสอบข้อมูลที่ท่านกรอกอีกครั้ง",font=("Helevetica",10),bootstyle="light")
coupon_alert_label = ttk.Label(frame_method,text="ไม่สามารถเปิดรายการคูปองได้",font=("Helevetica",16), bootstyle="danger")
label_alert_excess.append(method_alert_label)
label_alert_excess.append(coupon_alert_label)

transaction_title_label = ttk.Label(frame_transaction, text="การจองเสร็จสมบูรณ์", font=("Helevetica",36), bootstyle="light")
booking_title_label = ttk.Label(frame_transaction, text="ข้อมูลการจอง :", font=("Helevetica",20), bootstyle="primary")
transaction_title2_label = ttk.Label(frame_transaction,text="ข้อมูลการชำระเงิน :", font=("Helevetica",20), bootstyle="primary")

ttk.Label(frame_search_reservation, text="ค้นหาการจอง", font=("Helvetica", 36), bootstyle="light").grid(row=0, column=0, ipady=30, columnspan=2)
ttk.Label(frame_search_reservation, text="ชื่อจริง :", font=("Helvetica", 18), bootstyle="light").grid(row=1, column=0, padx=10, ipady=15)
ttk.Entry(frame_search_reservation, textvariable=firstname, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_search_reservation, text="นามสกุล :", font=("Helvetica", 18), bootstyle="light").grid(row=2, column=0, padx=10, ipady=15)
ttk.Entry(frame_search_reservation,  textvariable=lastname, width=20).grid(row=2, column=1, padx=10)
ttk.Label(frame_search_reservation, text="หมายเลขการจอง :", font=("Helvetica", 18), bootstyle="light").grid(row=3, column=0, padx=10, ipady=15)
ttk.Entry(frame_search_reservation, textvariable=booking_no, width=20).grid(row=3, column=1, padx=10)
ttk.Label(frame_search_reservation, text="วันที่เช็คอิน :", font=("Helvetica", 18), bootstyle="light").grid(row=4, column=0, padx=10, ipady=15)
check_in_date = ttk.DateEntry(frame_search_reservation, bootstyle="danger",dateformat="%Y-%m-%d",startdate=date.today())
check_in_date.grid(row=4, column=1, padx=10)
ttk.Button(frame_search_reservation, text="ค้นหาการจอง", bootstyle="danger", command=on_click_search_reservation_button).grid(row=5, column=0, pady=20, columnspan=2)
ttk.Button(frame_search_reservation, text="ย้อนกลับ", bootstyle="secondary", command=on_click_search_reservation_backward_button).grid(row=7, column=0, pady=175, columnspan=2)
search_reservation_alert = ttk.Label(frame_search_reservation, text="ไม่พบข้อมูลการจอง", font=("Helvetica", 18), bootstyle="danger")
label_alert_excess.append(search_reservation_alert)

account_title_label_customer = ttk.Label(frame_account,text=f"{firstname.get()}" + f"{lastname.get()}",font=("Helvetica", 16), bootstyle="light")
search_hotel_button = ttk.Button(frame_account, text="ค้นหาโรงเเรม", command=lambda: show_page("search_hotel", frame_account), bootstyle="danger")
search_reservation_button = ttk.Button(frame_account, text="ค้นหาการจอง", command=lambda: show_page("search_reservation", frame_account), bootstyle="danger")
customer_cancel_booking_button = ttk.Button(frame_account, text="ยกเลิกการจอง", command=lambda: show_page("customer_cancel_booking", frame_account), bootstyle="danger")
personal_information_button = ttk.Button(frame_account, text="ข้อมูลส่วนตัว", command=on_click_personal_information_button, bootstyle="danger")
my_travelling_button = ttk.Button(frame_account, text="การเดินทางของฉัน", command=on_click_my_travelling_button, bootstyle="danger")
my_favorite_hotel_button = ttk.Button(frame_account, text="โรงเเรมที่ฉันชื่นชอบ", command=on_click_my_favorite_hotel_button, bootstyle="danger")
logout_button_customer = ttk.Button(frame_account, text="ออกจากระบบ", command=on_click_logout_button, bootstyle="secondary")

account_title_label_admin = ttk.Label(frame_admin,text=f"{firstname.get()}" + f"{lastname.get()}",font=("Helvetica", 16), bootstyle="light")
add_hotel_button = ttk.Button(frame_admin, text="เพิ่มโรงเเรม", command=lambda: show_page("admin_add_hotel", frame_admin), bootstyle="danger")
delete_hotel_button = ttk.Button(frame_admin, text="ลบโรงเเรม", command=lambda: show_page("admin_delete_hotel", frame_admin), bootstyle="danger")
admin_cancel_booking_button = ttk.Button(frame_admin, text="ยกเลิกการจอง", command=lambda: show_page("admin_cancel_booking", frame_admin), bootstyle="danger")
logout_button_admin = ttk.Button(frame_admin, text="ออกจากระบบ", command=on_click_logout_button2, bootstyle="secondary")

ttk.Label(frame_admin_add_hotel, text="เพิ่มโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(pady=25, columnspan=2)
ttk.Label(frame_admin_add_hotel, text="ชื่อโรงเเรม :", font=("Helvetica", 14), bootstyle="light").grid(row=1, column=0, padx=10, ipady=10)
ttk.Entry(frame_admin_add_hotel, textvariable=hotel_name, width=20).grid(row=1, column=1, padx=10)
ttk.Label(frame_admin_add_hotel, text="ประเทศ :", font=("Helvetica", 14), bootstyle="light").grid(row=2, column=0, padx=10, ipady=10)
ttk.Entry(frame_admin_add_hotel, textvariable=country, width=20).grid(row=2, column=1, padx=10)
ttk.Label(frame_admin_add_hotel, text="จังหวัด :", font=("Helvetica", 14), bootstyle="light").grid(row=3, column=0, padx=10, ipady=10)
ttk.Entry(frame_admin_add_hotel, textvariable=province, width=20).grid(row=3, column=1, padx=10)
ttk.Label(frame_admin_add_hotel, text="อีเมลของโรงเเรม :", font=("Helvetica", 14), bootstyle="light").grid(row=4, column=0, padx=10, ipady=10)
ttk.Entry(frame_admin_add_hotel, textvariable=hotel_email, width=20).grid(row=4, column=1, padx=10)
ttk.Button(frame_admin_add_hotel, text="ยืนยัน", bootstyle="danger", command=on_click_admin_add_hotel_button).grid(row=5, column=0, pady=20, columnspan=2)
ttk.Button(frame_admin_add_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("admin", frame_admin_add_hotel)).grid(row=7, column=0, pady=275, columnspan=2)

ttk.Label(frame_admin_delete_hotel, text="ลบโรงเเรม", font=("Helvetica", 36), bootstyle="light").grid(pady=25, columnspan=2)
ttk.Label(frame_admin_delete_hotel, text="ชื่อโรงเเรม :", font=("Helvetica", 14), bootstyle="light").grid(row=1, column=0, padx=10, ipady=10)
ttk.Entry(frame_admin_delete_hotel, textvariable=hotel_name, width=20).grid(row=1, column=1, padx=10)
ttk.Button(frame_admin_delete_hotel, text="ยืนยัน", bootstyle="danger", command=on_click_admin_delete_hotel_button).grid(row=2, column=0, pady=20, columnspan=2)
ttk.Button(frame_admin_delete_hotel, text="ย้อนกลับ", bootstyle="secondary", command=lambda: backward("admin", frame_admin_delete_hotel)).grid(row=4, column=0, pady=400, columnspan=2)

ttk.Label(frame_admin_cancel_booking, text="ยกเลิกการจอง", font=("Helvetica", 36), bootstyle="light").grid(pady=25, columnspan=2)
ttk.Label(frame_admin_cancel_booking, text="หมายเลขการจอง :", font=("Helvetica", 14), bootstyle="light").grid(row=1, column=0, padx=10, ipady=10)
ttk.Entry(frame_admin_cancel_booking, textvariable=booking_no, width=20).grid(row=1, column=1, padx=10)
ttk.Button(frame_admin_cancel_booking, text="ยืนยัน", bootstyle="danger", command=on_click_admin_cancel_booking_button).grid(row=2, column=0, pady=20, columnspan=2)
ttk.Button(frame_admin_cancel_booking, text="ยกเลิก", bootstyle="secondary", command=lambda: backward("admin", frame_admin_cancel_booking)).grid(row=4, column=0, pady=400,columnspan=2)

ttk.Label(frame_customer_cancel_booking, text="ยกเลิกการจอง", font=("Helvetica", 36), bootstyle="light").grid(pady=25, columnspan=2)
ttk.Label(frame_customer_cancel_booking, text="หมายเลขการจอง :", font=("Helvetica", 14), bootstyle="light").grid(row=1, column=0, padx=10, ipady=10)
ttk.Entry(frame_customer_cancel_booking, textvariable=booking_no, width=20).grid(row=1, column=1, padx=10)
ttk.Button(frame_customer_cancel_booking, text="ยืนยัน", bootstyle="danger", command=on_click_customer_cancel_booking_button).grid(row=2, column=0, pady=20, columnspan=2)
ttk.Button(frame_customer_cancel_booking, text="ยกเลิก", bootstyle="secondary", command=lambda: backward("account", frame_customer_cancel_booking)).grid(row=4, column=0, pady=400,columnspan=2)


current_frame = frame_home
current_frame.pack()

root.mainloop()
