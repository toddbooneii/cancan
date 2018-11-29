try:
    import tkinter as tk
    from tkinter import font
except ImportError:
    import Tkinter as tk

class GUI(tk.Frame):
    # Define settings upon initialization
    # Unecessary for now, but can specify the colors, font styles, etc
    #   that are consistent throughout the windows
    def __init__(self, titleName=None, master=tk.Tk()):
        self.master = master
        backgroundColor = '#c5dfb4'
        widgetColor = '#384F2E'
        self.master.geometry("645x155")
        # parameters that you want to send through the Frame class.
        tk.Frame.__init__(self, background= backgroundColor)

# First GUI to open with categories of materials
class CategoriesGUI(GUI):
    def __init__(self):
        GUI.__init__(self)
        self.buttons = []
        self.create_buttons()
        self.category_grid()
        self.master.mainloop()

    def create_buttons(self):
        btn_nms = ['Aluminum', 'Battery', 'Computers', 'E-Cycling', 'Glass',
                            'Mobile Phone', 'Paper', 'Plastic', 'Tires', 'Waste']

        for b in btn_nms:
            self.buttons.append(tk.Button(self.master, text=b, font = font.Font(size=18)))

        def createMaterials(category):
            for b in self.buttons:
                b.grid_forget()
            MaterialsGUI(category['text'])

        self.buttons[0].config(command = lambda: createMaterials(self.buttons[0]))
        self.buttons[1].config(command = lambda: createMaterials(self.buttons[1]))
        self.buttons[2].config(command = lambda: createMaterials(self.buttons[2]))
        self.buttons[3].config(command = lambda: createMaterials(self.buttons[3]))
        self.buttons[4].config(command = lambda: createMaterials(self.buttons[4]))
        self.buttons[5].config(command = lambda: createMaterials(self.buttons[5]))
        self.buttons[6].config(command = lambda: createMaterials(self.buttons[6]))
        self.buttons[7].config(command = lambda: createMaterials(self.buttons[7]))
        self.buttons[8].config(command = lambda: createMaterials(self.buttons[8]))
        self.buttons[9].config(command = lambda: createMaterials(self.buttons[9]))

    def category_grid(self):
        self.master.title("Recycling Categories")
        i = 0
        j = 0
        for b in self.buttons:
            if(i > 4):
                i = 0
                j += 1
            b.grid(column=i, row=j, padx=15, pady=15, ipadx=5, ipady=5)
            i += 1

# Second GUI to open with materials of category chosen
class MaterialsGUI(GUI):
    def __init__(self, titleName):
        GUI.__init__(self, titleName)
        self.master.title("Materials of Type: " + titleName)
        self.material_list()
        self.master.mainloop()

    def createInformation(self, material):
        #widget.forget_grid all widgets in this class
        #create new informationGUI based on material
        self.button.grid_forget()
        InformationGUI(material)

    def material_list(self):
        #####Insert scrollable here and delete button
        #####Need to insert text line to search scrollable
        #####createInformation(material) will create last screen with info on material
        self.button = tk.Button(self.master, text = "new")
        self.button.grid(column=0, row=1, padx=15, pady=15, ipadx=5, ipady=5)
        self.button.config(command = lambda: self.createInformation(self.button['text']))

# Third GUI to open with information about material chosen
class InformationGUI(GUI):
    def __init__(self, titleName):
        GUI.__init__(self, titleName)
        self.master.title("Information on: " + titleName)
        self.material = titleName
        self.information()
        self.master.mainloop()

    def restartApp(self):
        #widget.forget_grid all widgets in this class
        self.button1.grid_forget()
        self.button2.grid_forget()
        CategoriesGUI()

    def createMaterials(self):
        #widget.forget_grid all widgets in this class
        self.button1.grid_forget()
        self.button2.grid_forget()
        MaterialsGUI(self.material)

    def information(self):
        #####Add location Information
        #####Add additional information for Materials

        self.button1 = tk.Button(self.master, text = "Restart")
        self.button1.grid(column=0, row=0, padx=15, pady=15, ipadx=5, ipady=5)
        self.button1.config(command = lambda: self.restartApp())
        self.button2 = tk.Button(self.master, text = "Materials")
        self.button2.grid(column=1, row=0, padx=15, pady=15, ipadx=5, ipady=5)
        self.button2.config(command = lambda: self.createMaterials())

categories = CategoriesGUI()
