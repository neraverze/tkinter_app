from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

root = Tk()
root.title("Add Address")

# Building the database connection
conn = sql.connect("address_book.db")
crsr = conn.cursor()

# Building the tables
crsr.execute("""
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY,
        f_name TEXT, 
        l_name TEXT, 
        number TEXT,
        zipcode INTEGER,
        state TEXT,
        country TEXT
    )
""")

# building up the GUI INTEFRACE

# Creating a frame for holding the form
form_frame = Frame(root, padx=10, pady=10)

entry_points = []
data_points = ['First Name', "Last Name", "Mobile Number", "State", "Country", "Zip Code"]
for i in range(0, 6):
    entry_points.append(Entry(form_frame, width=30))
    Label(form_frame, text=data_points[i]).grid(row=i, column=0)
    entry_points[i].grid(row=i, column=1, pady=5)

form_frame.grid(row=0, column=0, sticky='nesw')

def addRecord():
    # checking if any of the entries are null
    for entry in entry_points:
        if not entry.get():
            messagebox.showwarning("Incomplete Details", "Fill the details properly.")
            return
    
    # records tuple
    recTuple = (
        entry_points[0].get(),
        entry_points[1].get(),
        entry_points[2].get(),
        entry_points[3].get(),
        entry_points[4].get(),
        entry_points[5].get(),
    )

    # updating the records in the database
    try:
        crsr.execute("""
            INSERT INTO address
                (f_name, l_name, number, zipcode, state, country)
                VALUES
                (?, ?, ?, ?, ?, ?)
        """, recTuple)
    except Exception as e:
        messagebox.showwarning("Database Error", f"{e}")
        return
    
    messagebox.showinfo("Success", "Records added successfully.")
    return

# Building the frame for showing record
tableHeader = []
recordsFrame = Frame(root, padx=5, pady=5)
for i in range(0, 6):
    tableHeader.append(Label(recordsFrame, text=data_points[i]))

# showing the header
def showHeader():
    global tableHeader
    for i in range(0, 6):
        tableHeader[i].grid(row=0, column=i, padx=5, pady=5)

# Hide header
def hideHeader():
    global tableHeader
    for i in range(0, 6):
        tableHeader[i].grid_forget()

# build a row for data output
def build_row():
    row = []
    # creating the labels for data entry header
    for i in range(0, 6):
        row.append(Label(recordsFrame))
    
    return row

# add records to the table
recordsTable = []
def showRecordsTable():
    showHeader()
    global recordsTable

    # fetching the results
    try:
        rows = crsr.execute("SELECT * FROM address").fetchall()
    except Exception as e:
        messagebox.showwarning("Database Error", f"{e}")
        hideHeader()
        return
    
    # building rows and displaying
    index = 0
    for row in rows:
        placeholder = build_row()
        index += 1
        for i in range(0, 6):
            placeholder[i].config(text=row[i + 1])
            placeholder[i].grid(row=index, column=i, padx=5, pady=5)
    
    return
        
    
# Building the Buttons
Button(root, text='Add Record', command=addRecord).grid(row=1, column=0, sticky='nesw', pady=5, padx=5)
Button(root, text='Show All Records', command=showRecordsTable).grid(row=2, column=0, sticky='nesw', pady=5, padx=5)

# showing the records frame
recordsFrame.grid(row=3, column=0, padx=5, pady=5)

# last remenants
root.mainloop()
conn.commit()
conn.close()