import tkinter as tk


def gradient_fill(canvas, color1, color2):
    width, height = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    for y in range(height):
        r = int(color1[0] * (height - y) / height + color2[0] * y / height)
        g = int(color1[1] * (height - y) / height + color2[1] * y / height)
        b = int(color1[2] * (height - y) / height + color2[2] * y / height)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, y, width, y, fill=color, tags='gradient')
        
def display_info():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()

    # Set background color based on input values or reset to white if empty
    name_entry.config(bg="lightblue" if name else "white")
    age_entry.config(bg="lightgreen" if age else "white")
    address_entry.config(bg="lightcoral" if address else "white")


    info_window = tk.Toplevel(root)
    info_window.title("Entered Information")

    tk.Label(info_window, text="Here's Your Info:", font=("Tahoma", 14, "bold")).pack()

    info_frame = tk.Frame(info_window)
    info_frame.pack(padx=20, pady=10)

    labels = ["Name:", "Age:", "Address:"]
    data = [name, age, address]

    for i in range(len(labels)):
        label = tk.Label(info_frame, text=labels[i], font=("Helvetica", 12, "italic"))
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

        info = tk.Label(info_frame, text=data[i], font=("Trebuchet MS", 13, "bold"))
        info.grid(row=i, column=1, sticky="w", padx=10, pady=5)

def main():
    global root, name_entry, age_entry, address_entry
    root = tk.Tk()
    root.title("Personal Information")
    
 # Gradient Background
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()
    gradient_fill(canvas, (255, 255, 255), (200, 200, 255))  # Gradient fill from white to light blue
    
    

    # Custom Font and Style for Header
    header_label = tk.Label(root, text="Enter your information below:", font=("Tahoma", 16, "bold"), fg="black")
    header_label.pack(pady=10)

    global name_entry, age_entry, address_entry

    fields_frame = tk.Frame(root)
    fields_frame.pack()

    tk.Label(fields_frame, text="Name:", font=("Trebuchet MS", 15)).grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(fields_frame, font=("Arial", 12, "bold"))
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(fields_frame, text="Age:", font=("Trebuchet MS", 15)).grid(row=1, column=0, padx=10, pady=5)
    age_entry = tk.Entry(fields_frame, font=("Arial", 12, "bold"))
    age_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(fields_frame, text="Address:", font=("Trebuchet MS", 15)).grid(row=2, column=0, padx=10, pady=5)
    address_entry = tk.Entry(fields_frame, font=("Arial", 12, "bold"))
    address_entry.grid(row=2, column=1, padx=10, pady=5)

    submit_button = tk.Button(root, text="Submit", command=display_info, font=("Arial", 12, "bold"), bg="blue", fg="white")
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
