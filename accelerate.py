import pandas as pd
import tkinter as tk
from tkinter import ttk

#Read and analyze accelerometer data
path = 'Acceleration_data.xlsx'
accel = pd.read_excel(path, sheet_name="Acceleration_data")     #Reading the emulated Data
time_resp = accel['time']
accel_resp = accel['aT (m/s^2)']
#
# observers[] = List
#
# def init():
#     observer.push(new Observer());
#
# def notifyObserver(k):
#     for observer in observers
#         observer.notify(k);

def acceleration(x):                                            #Defining function
    c = 0
    for k in accel_resp:
        if(k>5):                                                #Initializing Condition to compare
            c += 1
    if (c>0):
        print("Movement Detected")
        #notifyObserver(k)
        popup = tk.Tk()                                         #Displaying popup message
        ttk.Label(popup, text="Movement Detected").pack()
        popup.mainloop()
    if(x>5):
        return True
    else:
        return False
# def time(y):
#     d = 0
#     for t in time_resp:
#         if (t<1):
#             d+=1
#     if(d>0):
#         print("time")
#
#     if (y>0.01):
#         return True
#     else:
#         return False

acceleration(6)
# time(1)

