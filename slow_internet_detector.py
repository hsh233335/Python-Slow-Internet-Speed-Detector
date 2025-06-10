from urllib.error import URLError
import speedtest
import notifypy
import tkinter.messagebox
import time
import socket

# Shows information that the program is already open, and shouldn't be closed.
tkinter.messagebox.showinfo("Information:", "Speedtest from slow_internet_detector.py is currently running... \n Please leave it on even when you're gonna close your computer.")
# Main program loop
while True:
    try:
        # Get the speedtest object.
        sp = speedtest.Speedtest()
    # If your internet is down, or too many requests with speedtest.net through the speedtest library.
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
            # Shows current download and upload speed.
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
        # If you put your files in the wrong directory (must be in the same directory), it will show an error using tkinter messagebox, and stops the program.
        except (FileNotFoundError, PermissionError):
            tkinter.messagebox.showerror("Error!", "Icon Image Not Found! For the notifications.")
    elif result is None:
        continue
    else:
        continue
    # Sends a notification warning, if your download and upload speed is less than 20.
    if download_speed < 20:
        notification.title = "Warning: Slow Internet!"
        notification.message = f"Your internet download speed is lower than 20! Check your internet speed! It is {download_speed:.2f} Mbps. Another notification will be sent in 3 seconds..."
        notification.send()
    elif upload_speed < 20:
        notification.title = "Warning: Slow Internet"
        notification.message = f"Your internet upload speed is lower than 20! Check your internet upload speed! It is {upload_speed:.2f} Mbps. No more notifications will be sent from now on."
        notification.send()
    # Sends a tkinter messagebox and a notification if your internet speed is more than 400
    elif download_speed > 400:
        tkinter.messagebox.showinfo("Wow!", f"Wow! Your internet is so fast! Your download speed is {download_speed:.2f} Mbps and your upload speed is {upload_speed:.2f} Mbps!")
        notification.title = "Wow!: Fast Internet!"
        notification.message = f"Wow! Your internet is so fast! Your download speed is {download_speed:.2f} Mbps and your upload speed is {upload_speed:.2f} Mbps!"
        notification.send()
    # Loop again after 3600 seconds, or 1 hour.
    time.sleep(3600)
