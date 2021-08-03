import tkinter as tk
import tkinter.font
from tkinter import filedialog
from PIL import ImageTk, Image

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Browse...", filetypes = [("images", "*.jpg")])
    #NeuralNet(img_path = filename)

#TODO: add tabb for infomation on training data (which cars were contained in data set )
#def NeuralNet(img_path):
    #get image file name
    #reshape image to needed size for NN
    #feed through NN
    #Return result

# create and reconfig window
window = tk.Tk()
window.title("Car Classification Application")
window.geometry("600x600")

# get banner image and set label 
raw_img = Image.open("car background.jpg")
ban_size = (600,200)
raw_img = raw_img.resize(ban_size)
ban_img = ImageTk.PhotoImage(raw_img)
ban_label = tk.Label(window, image=ban_img)
ban_label.grid(row = 1, column = 1)

# create text labels 
page_title = tk.Label(window, text="What Car is This?", font = 'Bold')
step_1 = tk.Label(text = "Step 1: Upload image")
results = tk.Label(text = "Results: ")
trade_in = tk.Label(text="Trade-in value: ")


#position labels 
page_title.place(relx = 0.5, rely = 0.1, anchor = 'center')
step_1.place(relx = 0.13, rely = 0.4, anchor = 'center')
results.place(relx = 0.07, rely = 0.6, anchor = 'center')
trade_in.place(relx = 0.1, rely = 0.8, anchor = 'center')

#upload button 
upload = tk.Button(text = 'Browse...', command = browseFiles)
upload.place(relx = 0.17, rely = 0.5, anchor = 'center')

#make/ model/ year 


window.mainloop()