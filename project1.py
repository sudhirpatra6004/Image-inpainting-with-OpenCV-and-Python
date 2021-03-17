from tkinter import *
import cv2 
import numpy as np
# loading Python Imaging Library 
from PIL import ImageTk, Image 
  
# To get the dialog box to open when required  
from tkinter import filedialog
original_image=None
mask_image=None
def demo(original,mask,x1,y1):
    print(mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    print(mask)
    output = cv2.inpaint(original, mask, 3, flags=cv2.INPAINT_TELEA)
    #cv2.imshow('result',output)
    #output = output - 18
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    img= Image.fromarray(output)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image = img)
    panel.image = img
    panel.place(x=x1,y=y1)
def open_img(x1,y1,ori): 
    # Select the Imagename  from a folder  
    x = openfilename() 
  
    # opens the image 
    img = Image.open(x) 
    print(type(img))
    if ori==True:
        global original_image
        original_image=img
        
        original_image=np.array(original_image)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        #print(original_image)
        #cv2.imshow('original',original_image)
    else:
        global mask_image
        mask_image=img 
        mask_image=np.array(mask_image)
        #print(mask_image)
        #cv2.imshow('mask',mask_image)
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((250, 250), Image.ANTIALIAS) 
    
    
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
   
    # create a label 
    panel = Label(root, image = img) 
      
    # set the image as img  
    
    panel.image = img 
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    panel.place(x=x1,y=y1)

def openfilename(): 
  
    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
    filename = filedialog.askopenfilename(title ='"pen') 
    return filename

root = Tk() 
  
# Set Title as Image Loader 
root.title("Image Loader") 
  
# Set the resolution of window 
root.geometry("1050x1050") 
  
# Allow Window to be resizable 
root.resizable(width = True, height = True) 
  
# Create a button and place it into the window using grid layout 
btn = Button(root, text ='open image',width =10,height =3, command = lambda : open_img(100,300,True)).place( 
                                        x = 200, y = 70) 

btn1 = Button(root, text ='mask image',width =10,height =3, command = lambda : open_img(400,300,False)).place( 
                                        x = 500, y = 70) 
btn2 = Button(root, text ='inpaint',width =10,height =3, command = lambda : demo(original_image,mask_image,700,300)).place( 
                                             x = 800, y = 70)

root.mainloop() 