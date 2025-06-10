from urllib.error import URLError
import speedtest
import notifypy
import tkinter.messagebox
import time
import socket

tkinter.messagebox.showinfo("Information:", "Speedtest from slow_internet_detector.py is currently running... \n Please leave it on even when you're gonna close your computer.")
while True:
    try:
        sp = speedtest.Speedtest()
    except (speedtest.ConfigRetrievalError, URLError, socket.gaierror):
        tkinter.messagebox.showerror("Error!", "Your speedtest couldn't be completed. \n Please check your internet and run this program again. \n Please try again after a few minutes. \n Exiting...")
        time.sleep(2)
        break
    download_speed = sp.download() / 1_000_000
    upload_speed = sp.upload() / 1_000_000
    notification = notifypy.Notify()
    result = tkinter.messagebox.askyesnocancel("Current Internet Speed", "Do you want to know your current internet speed? \n (Will be sent as a notification and message)")
    if result is True:
        try:
            tkinter.messagebox.showinfo("Current Internet Download Speed", f"Your current internet download speed is {download_speed:.2f} Mbps.")
            notification.title = "Current Internet Download Speed"
            notification.icon = "wifi_icon.png"
            notification.message = f"Your current internet download speed is {download_speed:.2f} Mbps."
            notification.send()
            time.sleep(2)
            tkinter.messagebox.showinfo("Current Internet Upload Speed", f"Your current internet upload speed is {upload_speed:.2f} Mbps.")
            notification.title = "Current Internet Upload Speed"
            notification.icon = "wifi_icon.png"
            notification.message = f"Your current internet upload speed is {upload_speed:.2f} Mbps."
            notification.send()
        except (FileNotFoundError, PermissionError):
            tkinter.messagebox.showerror("Error!", "Icon Image Not Found! For the notifications.")
    elif result is None:
        continue
    else:
        continue
    if download_speed < 20:
        notification.title = "Warning: Slow Internet!"
        notification.message = f"Your internet download speed is lower than 20! Check your internet speed! It is {download_speed:.2f} Mbps. Another notification will be sent in 3 seconds..."
        notification.send()
    elif upload_speed < 20:
        notification.title = "Warning: Slow Internet"
        notification.message = f"Your internet upload speed is lower than 20! Check your internet upload speed! It is {upload_speed:.2f} Mbps. No more notifications will be sent from now on."
        notification.send()
    elif download_speed > 400:
        tkinter.messagebox.showinfo("Wow!", f"Wow! Your internet is so fast! Your download speed is {download_speed:.2f} Mbps and your upload speed is {upload_speed:.2f} Mbps!")
        notification.title = "Wow!: Fast Internet!"
        notification.message = f"Wow! Your internet is so fast! Your download speed is {download_speed:.2f} Mbps and your upload speed is {upload_speed:.2f} Mbps!"
        notification.send()
    time.sleep(3600)