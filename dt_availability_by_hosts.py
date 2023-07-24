#!/usr/bin/env python3
# dt_availabiliy_by_hosts - the app gets availability by host from dynatrace 
# Copyright (c) 2021 by
# Author: Ruslan Variushkin, ruslansvs@yahoo.com

#Import the libraries
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import time
import datetime
import sys
import json
import requests
import xlwt

global url
global token
global customer

customer="TEST"
url = ""
token = ""

def generete_report(start_date, end_date):
    # Generate report
    global url
    global token
    
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Api-Token '+token
    }
    
    url = url+"/api/v1/timeseries/com.dynatrace.builtin:host.availability.percent?includeData=true&startTimestamp="+str(start_date)+"&endTimestamp="+str(end_date)+"&queryMode=TOTAL"
    
    response = requests.get(url, headers=headers)
    
    end_date=int(end_date)
    Filename=customer+'Dynatrace-availability'
    
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Servers Availability")
    sheet1.write(0, 0, "Server Name")
    sheet1.write(0, 1, "Availability (%)")
    sheet1.write(0, 2, "Start Date - End Date")
    row=1
    
    
    print("Converting JSON encoded data into XLS file")
    developer = response.json()
    for host in developer["dataResult"]["dataPoints"]:
        Server_name = developer["dataResult"]["entities"][host]
        date = developer["dataResult"]["dataPoints"][host][0][0]
        av = developer["dataResult"]["dataPoints"][host][0][1]
        date_start = time.strftime('%Y-%m-%d', time.gmtime(int(str(date)[:-3])))
    
        date_end = time.strftime('%Y-%m-%d', time.gmtime(int(str(end_date)[:-3])))
        sheet1.write(row, 0, Server_name)
        sheet1.write(row, 1, av)
        sheet1.write(row, 2, date_start + " - " + date_end)
        row += 1
    
    return book.save(sys.path[0]+"\\"+Filename+".xls")


def time_to_unixtime(from_date):
    # convert time to unix format
    conv_date=str(from_date)+" +00:00"
    conv_date=datetime.datetime.strptime(conv_date, "%Y-%m-%d %z").timestamp()
    conv_date=(int(conv_date)*1000)
    return conv_date

def error_output(text):
    # error output
    from tkinter import messagebox
    # hide main window
    root = Tk()
    root.withdraw()
    messagebox.showerror(title="Error", message=text)
    sys.exit()


def maya_calandar():
    # calendar UI
    START=True
    start_date=None
    end_date=None
    #Create an instance of tkinter frame or window
    win= Tk()
    win.title("Availability Calendar")
    win.geometry("800x600")
    win.resizable(width=None, height=None)
    my_Label = Label
    delta_Label = Label
    
    cal=Calendar(win, setmode="day", locate="en_En", date_pattern="dd-mm-y")
    cal.pack(pady=20, fill="both", expand=True)

    
    def get_date():
    #Define Function to select the date
        nonlocal START
        nonlocal start_date
        nonlocal end_date
        if START:
            label.config(text="Start Date: "+cal.get_date())
            start_date=cal.selection_get()
            START=False
        else:
            my_label.config(text="End Date: "+cal.get_date())
            end_date=cal.selection_get()
            START=True
        if end_date:
            delta=start_date-end_date
            delta_label.config(text="Delta :"+str(delta).replace("-","").replace(",","").replace("0:00:00", ""))
    
    def close_X():
        sys.exit()
    
    button= Button(win, text= "Select the Date", command= get_date)
    button.pack(pady=20)
    
    button= Button(win, text= "Generate report", command= win.destroy)
    button.pack(pady=20)
    label = Label(win, text="Start Date")
    label.pack(pady=20)
    
    my_label = my_Label(win,  text="End Date")
    my_label.pack(pady=20)
    
    delta_label = delta_Label(win, text="")
    delta_label.pack(pady=20, side = LEFT)
    
    win.protocol('WM_DELETE_WINDOW', close_X)


    win.mainloop()

    current_date = datetime.date.today();
    if start_date == None and end_date == None:
        error_output("It looks like you've forgotten something...\nStart date and end date are empty.\
                      \n\nPlease pick the dates!")
    elif end_date == None:
        error_output("Sorry.. but do you expect me to be a mind reader? :(\nEnd date is empty\
                    \n\nPlease pick the date!")
    elif start_date > end_date:
        error_output("Oh.. that would be difficult; end date is greater than start date.\
                    \nStart date: "+str(start_date)+" End date: "+str(end_date)+"."+\
                    "\n\nPlease change the end date!")
    elif start_date > current_date:
        error_output("Unfortunately, Dynatrace is not a fortune teller.\
                    \nStart date is "+str(start_date)+", but today is "+str(current_date)+"."+\
                   "\n\nPlease change the start date!")
    else:
        return [start_date, end_date]
    
def maja():
    # The main function
    chosen_date=maya_calandar()
    generete_report(time_to_unixtime(chosen_date[0]), time_to_unixtime(chosen_date[1]))

maja()

