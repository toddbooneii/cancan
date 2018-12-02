try:
    import tkinter as tk
    from tkinter import font
except ImportError:
    import Tkinter as tk

import csv_to_dataframe
import numpy as np

buttonColor = '#c5dfb4'
otherColor = '#384F2E'

#Set up the root tk frame
def initializeRoot():
    global root
    parent = tk.Tk()
    parent.title('background image')

    global background_label
    bg_image = tk.PhotoImage(file="Home.gif")
    # get the width and height of the image
    w = bg_image.width()
    h = bg_image.height()
    # size the window so the image will fill it
    parent.geometry("%dx%d+50+30" % (w, h))
    root = tk.Canvas(width=w, height=h)
    root.pack(side='top', fill='both', expand='yes')
    root.create_image(0, 0, image=bg_image, anchor='nw')

    root.parent = parent
    root.image = bg_image

def clearPage():
    for widget in root.grid_slaves():
        widget.grid_forget()
    for i in range(10):
        root.grid_columnconfigure(i, minsize=0)
        root.grid_rowconfigure(i, minsize=0)

# First GUI to open with categories of materials
class CategoriesGUI():

    def __init__(self):
        #All elements for Categories GUI
        self.catButtons = []
        self.infoButtons = []
        self.frames = []
        self.createButtons()

    #Defines the buttons displayed on the first page
    def createButtons(self):
        #Use frank's web scrape here!
        btn_nms = ['Aluminum', 'Battery', 'Computers', 'E-Cycling', 'Glass',
                            'Mobile Phone', 'Paper', 'Plastic', 'Tires', 'Waste']

        i = 0
        for b in btn_nms:
            self.frames.append(tk.Frame(root))
            self.catButtons.append(tk.Button(self.frames[i], text=b, font = ("consolas", 18), bg=buttonColor))
            self.catButtons[i].pack(side=tk.TOP)
            self.infoButtons.append(tk.Button(self.frames[i], text="More info", font = ("consolas", 10), bg=buttonColor))
            self.infoButtons[i].pack(side=tk.TOP)
            i += 1

        #Buttons bound to showMaterials with correct category
        self.catButtons[0].config(command = lambda: matGUI.showMaterials(self.catButtons[0]['text']))
        self.catButtons[1].config(command = lambda: matGUI.showMaterials(self.catButtons[1]['text']))
        self.catButtons[2].config(command = lambda: matGUI.showMaterials(self.catButtons[2]['text']))
        self.catButtons[3].config(command = lambda: matGUI.showMaterials(self.catButtons[3]['text']))
        self.catButtons[4].config(command = lambda: matGUI.showMaterials(self.catButtons[4]['text']))
        self.catButtons[5].config(command = lambda: matGUI.showMaterials(self.catButtons[5]['text']))
        self.catButtons[6].config(command = lambda: matGUI.showMaterials(self.catButtons[6]['text']))
        self.catButtons[7].config(command = lambda: matGUI.showMaterials(self.catButtons[7]['text']))
        self.catButtons[8].config(command = lambda: matGUI.showMaterials(self.catButtons[8]['text']))
        self.catButtons[9].config(command = lambda: matGUI.showMaterials(self.catButtons[9]['text']))

        #Buttons bound to catiGUI.showCategoryInfo with correct category
        self.infoButtons[0].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[0]['text']))
        self.infoButtons[1].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[1]['text']))
        self.infoButtons[2].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[2]['text']))
        self.infoButtons[3].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[3]['text']))
        self.infoButtons[4].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[4]['text']))
        self.infoButtons[5].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[5]['text']))
        self.infoButtons[6].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[6]['text']))
        self.infoButtons[7].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[7]['text']))
        self.infoButtons[8].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[8]['text']))
        self.infoButtons[9].config(command = lambda: catiGUI.showCategoryInfo(self.catButtons[9]['text']))


    #Show category page
    def showCategories(self):
        clearPage()
        root.parent.title("Recycling Categories")

        newBackground = tk.PhotoImage(file="Home.gif")
        root.create_image(0, 0, image=newBackground, anchor='nw')

        i = 0
        j = 0
        for b in self.frames:
            if(i > 4):
                i = 0
                j += 3
            root.grid_columnconfigure(i, minsize=(root.image.width()/5))
            root.grid_rowconfigure(i, minsize=(root.image.height()/5))
            b.grid(column=i, row=j, padx=0, pady=0)
            i += 1

class CategoryInfo():
    def __init__(self):
        #All elements for Categories GUI
        self.widgets = []
        self.createInfo()

    #Method for each button to open the correct materials page
    def openCategories(self):
        clearPage()
        catGUI.showCategories()

    #Defines the buttons displayed on the first page
    def createInfo(self):
        self.title = tk.Text(root, borderwidth=1, font=font.Font(size=18),
                                height=1)

        self.txt = tk.Text(root, font=("consolas", 12), wrap='word', bg='white',
                                height=10, width=30)

        self.backButton = tk.Button(root, text="Back", font = ("consolas", 18), bg=buttonColor)
        self.backButton.config(command = self.openCategories)

        self.scrollb = tk.Scrollbar(root, command=self.txt.yview)
        self.txt['yscrollcommand'] = self.scrollb.set

    #Show category info page
    def showCategoryInfo(self, category):
        clearPage()
        root.parent.title(category + " Info")

        # newBackground = tk.PhotoImage(file=category+".gif")
        # root.image = newBackground
        # root.create_image(0, 0, image=newBackground, anchor='nw')

        self.title.config(state=tk.NORMAL)
        self.title.delete("1.0", tk.END)
        self.title.insert(tk.END, category + " Info")
        self.title.config(state=tk.DISABLED, width=len(category+" Info")-3)
        self.title.grid(row=0, column=0, sticky = 'nw')

        self.txt.grid(row=1, column=0, padx=2, pady=2, sticky = 'nw')
        self.txt.insert(tk.END, "Insert frank info here")
        self.txt.config(state=tk.DISABLED)
        self.scrollb.grid(row=1, column=1, sticky = "nw")

        self.backButton.grid(row=0, column=1, padx=2, pady=2, sticky = 'nw')


# Second GUI to open with materials of category chosen
class MaterialsGUI():

    def __init__(self):
        #All elements for Materials GUI
        self.materialList()

    #Create the widgets to be displayed on second page
    def materialList(self):
        self.scroll = tk.Scrollbar(root)
        self.options = tk.Listbox(root)

        self.materials_filename = "Waste_Recycling.csv"

        self.title = tk.Text(root, borderwidth=1, font=font.Font(size=18),
                                height=1)

        # bind listbox to scrollbar
        self.options.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.options.yview)

        self.search = tk.Entry(root)
        self.searchButton = tk.Button(root, text="Search")
        self.searchButton.config(command = lambda: self.searchMaterials())

        self.backButton = tk.Button(root, text = "Back")
        self.backButton.config(command = lambda: catGUI.showCategories())

        def openInformation():
            for i in range(len(self.currentMaterials)):
                if(self.options.selection_includes(i)):
                    infGUI.showInformation(self.currentMaterials[i])

        self.showMore = tk.Button(root, text="More Info\non Material")
        self.showMore.config(command = openInformation)

    def searchMaterials(self):
        userEntry = self.search.get()
        for i in range(len(self.currentMaterials)):
            if(userEntry.lower() in self.currentMaterials[i].lower() and userEntry):
                self.options.selection_set(i)

    #Method to show Materials page
    def showMaterials(self, category):
        clearPage()
        self.category = category
        root.parent.title("Materials of Type: " + category)

        # newBackground = tk.PhotoImage(file=category+".gif")
        # root.image = newBackground
        # root.create_image(0, 0, image=newBackground, anchor='nw')

        self.title.grid(row=0, column=0, padx = 5, pady=5, sticky = 'w')
        self.title.config(state=tk.NORMAL)
        self.title.delete("1.0", tk.END)
        self.title.insert(tk.END, "Materials of Type: "+category)
        self.title.config(state=tk.DISABLED, width=len("Materials of Type: "+category)-7)

        materials = csv_to_dataframe.get_dataframes(self.materials_filename)
        self.currentMaterials = materials.loc[materials['Type'] == category, 'Material Title']

        #Update options pane
        self.options.grid(column=0, row=2, padx = 5, pady=5, sticky = 'w')
        self.options.delete(0, tk.END)
        for i in self.currentMaterials:
            self.options.insert(tk.END, i)

        self.backButton.grid(column=1, row=0, padx = 5, pady=5, sticky = 'w')

        self.search.grid(column=0, row=1, padx = 5, pady=5, sticky = 'w')
        self.search.delete(0, tk.END)
        self.search.focus_set()

        self.searchButton.grid(column=1, row=1, padx = 5, pady=5, sticky = 'w')

        self.showMore.grid(column=1,row=2, padx = 5, pady=5, sticky = 'w')

# Third GUI to open with information about material chosen
class InformationGUI():
    def __init__(self):
        #All elements for Information GUI
        self.widgets = []
        self.information()

    #####Todd function#####
    #####Output goes to directionsOutput####
    def getDirections(self):
        self.directionsOutput.config(state=tk.NORMAL)
        self.directionsOutput.delete(0, tk.END)

    #Create the widgets to be displayed on third page
    def information(self):
        #####Add location Information
        #####Add additional information for Materials
        self.directionsTitle = tk.Text(root, borderwidth=1, font=font.Font(size=14), height=3,
                                            width=20)
        self.directionsTitle.insert(tk.END, "Directions to nearest\nrecycling center*****\nHelp this title @peter")

        self.directionsEntry = tk.Entry(root)
        self.directionsSearch = tk.Button(root, text="Search")
        self.directionsSearch.config(command = lambda: self.getDirections())

        self.directionsOutput = tk.Text(root, font=("consolas", 12), wrap='word', bg='white',
                                height=10, width=30)
        self.scrollb = tk.Scrollbar(root, command=self.directionsOutput.yview)
        self.directionsOutput['yscrollcommand'] = self.scrollb.set

        self.moreInfoTitle = tk.Text(root, borderwidth=1, font=font.Font(size=14), height=1, width=30)

        self.moreInfo = tk.Text(root, font=("consolas", 12), wrap='word', bg='white',
                                height=10, width=30)

        self.restartButton = tk.Button(root, text = "Restart")
        self.restartButton.config(command = lambda: catGUI.showCategories())
        self.backButton = tk.Button(root, text = "Back")
        self.backButton.config(command = lambda: matGUI.showMaterials(matGUI.category))

    ####Frank info here. Set to self.moreInfo
    def setInfo(self, material):
        self.moreInfo.config(state=tk.NORMAL)
        if self.moreInfo:
            self.moreInfo.delete("1.0", tk.END)

    #Show information page
    def showInformation(self, material):
        clearPage()
        self.material = material
        root.parent.title("Additional Information on: " + material)

        self.directionsTitle.grid(column=0, row=0, padx=15, pady=15, sticky='w')
        self.directionsTitle.config(state=tk.DISABLED)
        self.directionsEntry.grid(column=0, row=1, padx=15, pady=15, ipadx=5, ipady=5, sticky='w')
        self.directionsEntry.delete(0, tk.END)
        self.directionsEntry.insert(tk.END, "Enter address here")
        self.directionsEntry.focus_set()
        self.directionsOutput.grid(column=0, row=2, rowspan=3, padx=15, pady=15, ipadx=5, ipady=5, sticky='w')
        self.directionsOutput.config(state=tk.DISABLED)

        self.moreInfoTitle.grid(column=1, row=0, padx=15, pady=15, ipadx=5, ipady=5, sticky='w')
        self.moreInfoTitle.config(state=tk.NORMAL)
        self.moreInfoTitle.delete("1.0", tk.END)
        self.moreInfoTitle.insert(tk.END, "More information on "+material)
        self.moreInfoTitle.config(state=tk.DISABLED)
        self.moreInfo.grid(column=1, row=2, rowspan=3, padx=15, pady=15, ipadx=5, ipady=5, sticky='w')
        self.setInfo(material)
        self.moreInfo.config(state=tk.DISABLED)

        self.restartButton.grid(column=2, row=0, padx=15, pady=15, ipadx=5, ipady=5, sticky='w')
        self.backButton.grid(column=2, row=1, padx=15, pady=15, ipadx=5, ipady=5, sticky='w')

#Run the application
def main():
    initializeRoot()
    global catGUI
    global catiGUI
    global matGUI
    global infGUI
    infGUI = InformationGUI()
    matGUI = MaterialsGUI()
    catiGUI = CategoryInfo()
    catGUI = CategoriesGUI()
    catGUI.showCategories()
    root.mainloop()

main()
