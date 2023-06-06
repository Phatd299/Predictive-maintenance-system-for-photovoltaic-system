import tkinter as tk
from tkinter import ttk

def login():
    root.destroy()

# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)
# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
# login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()


from tkinter import filedialog

def submit_values():
    irradiance = irradiance_entry.get()
    temperature = temperature_entry.get()
    voltage = voltage_entry.get()
    humidity = humidity_entry.get()
    
    # Do something with the entered values, such as calculations or further processing
    print("Solar Irradiance:", irradiance)
    print("Panel Temperature:", temperature)
    print("DC Voltage Output:", voltage)
    print("Humidity Level:", humidity)

def upload_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    print("Selected file:", file_path)

root = tk.Tk()
root.title("Maintenance System for PV System")

title_label = tk.Label(root, bg="#BFEFFF", text="PREDICTIVE MAINTENANCE SYSTEM FOR PHOTOVOLTAIC SYSTEM", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Set the initial window size
root.geometry("950x400")

# Set the background color
root.configure(bg="#BFEFFF")  # Light blue color

# Solar Irradiance
irradiance_label = tk.Label(root,bg="#BFEFFF", text="Enter solar irradiance level (0-100 W/m2):")
irradiance_label.grid(row=1, column=0, padx=10, pady=10)
irradiance_entry = tk.Entry(root)
irradiance_entry.grid(row=1, column=1, padx=10, pady=10)

# Panel Temperature
temperature_label = tk.Label(root,bg="#BFEFFF", text="Enter panel temperature (0-60 Celsius Degree):")
temperature_label.grid(row=2, column=0, padx=10, pady=10)
temperature_entry = tk.Entry(root)
temperature_entry.grid(row=2, column=1, padx=10, pady=10)

# DC Voltage Output
voltage_label = tk.Label(root,bg="#BFEFFF", text="Enter DC voltage output (0-1000V):")
voltage_label.grid(row=3, column=0, padx=10, pady=10)
voltage_entry = tk.Entry(root)
voltage_entry.grid(row=3, column=1, padx=10, pady=10)

# Humidity Level
humidity_label = tk.Label(root,bg="#BFEFFF", text="Enter humidity level (0-100%):")
humidity_label.grid(row=4, column=0, padx=10, pady=10)
humidity_entry = tk.Entry(root)
humidity_entry.grid(row=4, column=1, padx=10, pady=10)

# Upload Photo
upload_label = tk.Label(root,bg="#BFEFFF", text="Insert your solar panel image here:")
upload_label.grid(row=1, column=4, padx=10, pady=10)
upload_button = tk.Button(root, text="Upload", command=upload_photo)
upload_button.grid(row=2, column=4, padx=10, pady=10, rowspan=3)


submit_button = tk.Button(root, text="Submit", command=submit_values, font=("Arial", 12, "bold"))
submit_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()