import tkinter as tk
from weather_forecast import get_forecast

def forecast():
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

    city = entry.get()
    data = get_forecast(city)
    temp = data[0]
    desc = data[1]

    entry2.insert(0, f"{temp} C")
    entry3.insert(0, desc)

# Create a window
window = tk.Tk()

# Create a label
label = tk.Label(text="Weather Forecast", fg="white", bg="black", font=('Poppins', 25))
label.pack()

# Entry for City
entry = tk.Entry(font=('Poppins', 15))
entry.pack()

btn = tk.Button(text="Forecast", width=10, font=('Poppins', 10), command=forecast)
btn.pack()

label2 = tk.Label(text="Temperature:", font=('Poppins', 18))
label2.pack()

# Entry for Temperature
entry2 = tk.Entry(font=('Poppins', 15))
entry2.pack()

label3 = tk.Label(text="Weather Description:", font=('Poppins', 18))
label3.pack()

# Entry for Desc
entry3 = tk.Entry(font=('Poppins', 15))
entry3.pack()

# It would run the window
window.mainloop()
