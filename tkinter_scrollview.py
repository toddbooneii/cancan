from tkinter import *
import csv_to_dataframe

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root)
listbox.pack()

materials_filename = "Waste_Recycling.csv"
locations_filename = "Locations.csv"
materials, locations = csv_to_dataframe.get_dataframes(materials_filename, locations_filename)

for i in range(100):
    listbox.insert(END, materials.iloc[i,0])

# bind listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

mainloop()