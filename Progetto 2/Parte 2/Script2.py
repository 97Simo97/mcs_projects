# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:09:45 2021

@author: Ritucci Simone, 813473
"""

import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from scipy.fftpack import dct, idct
import cv2 
#from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

img = []

def show_about_message():
        
    box_title = "My_compress 1.0"
    box_message = "Un semplice software in grado di comprimere immagini bitmap secondo i valori F e d da settare"
    messagebox.showinfo(box_title, box_message)
    
def choice(window):
    global img 
    global path
  
    filename = filedialog.askopenfilename(
        defaultextension=".bmp",
        filetypes=[("Tutti i file", "*.*"),
                   ("Foto in scala di grigi bitmap", "*.bmp"),])
    
    if filename:
        
        sud_label = tk.Label(window, text="File caricato: "+ f"{filename}")
        sud_label.grid(row=9, column=0, sticky="S", pady=20)
    
        img = cv2.imread(filename,0) #From bitmap to array
    else:
        img = []  
    

def compress(window,f,d):
    global img
    
    
    if (img!=[]):
        
        if (f!="" and d!=""):
            f = int(f)
            d = int(d)
            if(d>=0 and d <=(2*f-2)):
                if(f<=img.shape[0] and f<=img.shape[1]):
                    
                    blocchi_ff = decompose(f)
                    
                    nuovi_blocchi = dct2(blocchi_ff,d)
                    
                    new_img = compose(nuovi_blocchi, f)
                    
                    #a = Image.fromarray(img).show(title = "Immagine originale")
                    #b = Image.fromarray(new_img).show(title = "Immagine compressa")
                    
                    show(img,new_img)

                else:
                    messagebox.showerror("Errore", "Il valore F deve essere inferiore alle dimensioni dell'immagine") 
            else:
                messagebox.showerror("Errore", "Il valore d deve essere compreso fra 0 e 2*F-2")
        elif(f==""and d!=""):
            messagebox.showerror("Errore", "Immagine caricata ma valore F non selezionato") 
        elif(f!=""and d==""):
            messagebox.showerror("Errore", "Immagine caricata ma valore d non selezionato") 
        else:
            messagebox.showerror("Errore", "Immagine caricata ma valori F e d non selezionati") 

    else:
         
         if (f!="" and d!=""):
            messagebox.showerror("Errore", "Immagine non caricata") 
         elif(f==""and d!=""):
            messagebox.showerror("Errore", "Immagine non caricata e valore F non selezionato") 
         elif(f!=""and d==""):
            messagebox.showerror("Errore", "Immagine non caricata e valore d non selezionato") 
         else:
            messagebox.showerror("Errore", "Immagine non caricata e valori F e d non selezionati") 

def decompose(f):
    global img
    blocchi_ff = []  
    k = 0
    p = 0

    for i in range (int((len(img))/f)):
        for j in range (int((len(img[0]))/f)):
    
            blocco = img[k:f+k,p:f+p]
            blocchi_ff.append(blocco)
            
            p+=f  
        k+=f
        p = 0 
    
    return blocchi_ff

def dct2(blocchi,d):
    new_list = []
    
    for b in blocchi:
        #applico dct
        bloccodct = dct(np.transpose(dct(np.transpose(b), norm='ortho')), norm='ortho')
        
        #taglio freq
        for k in range(len(bloccodct)):
            for l in range(len(bloccodct[0])):
                if k + l >= d:
                    bloccodct[k,l] = 0
        
        #applico idct2
        bloccoidct = idct(np.transpose(idct(np.transpose(bloccodct), norm='ortho')), norm='ortho')

        #arrotondo i valori all'intero piu vicino e sistemo i valori <0 con 0 
        #e i valori >255 con 255
        for k in range(len(bloccoidct)):
            for l in range(len(bloccoidct[0])):
                bloccoidct[k,l] = int(bloccoidct[k,l])
                if (bloccoidct[k,l]>255):
                    bloccoidct[k,l]=255
                elif (bloccoidct[k,l]<0):
                    bloccoidct[k,l]=0
                    
        new_list.append(bloccoidct)
        
    return new_list

def compose(nuovi_blocchi,f):
    global img
    nblocks = len(nuovi_blocchi)
    index = 0
    ncol=int(len(img[0])-(len(img[0])%f))    
    nblocks_per_row = int(ncol/f)
   
    new_img = np.array([],  dtype=np.int64).reshape(0, ncol)
    
    for i in range(int(nblocks/nblocks_per_row)):
        
        blocchi_da_comporre = nuovi_blocchi[index:index + nblocks_per_row]
        
        index += nblocks_per_row

        new_img = np.vstack((new_img,np.hstack(blocchi_da_comporre)))  #funzioni hstack e vstack del modulo np
    cv2.imwrite('new_img.bmp', new_img)
    
    
    return new_img 

def show(img,new_img):
    window = tk.Tk()
    window.geometry('1000x1000')
    window.wm_title("Risultato")
    comparison = Figure(figsize=(6,6),dpi = 100) 
    comparison.add_subplot(121).imshow(img,cmap='gray', vmin=0, vmax=255)
    comparison.add_subplot(122).imshow(new_img, cmap='gray', vmin=0, vmax=255)
    canvas = FigureCanvasTkAgg(comparison, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    window.mainloop()

def main():
    global img
    window = tk.Tk()
    window.geometry("900x500")
    window.title("Compressione Jpeg")
    window.grid_columnconfigure(0, weight=1)
    window.configure(background = 'white')
    menubar = tk.Menu(window, font=("Helvetica",10))
    window.config(menu=menubar)
    file_dropdown = tk.Menu(menubar, font=("Helvetica",12), tearoff=0)
    file_dropdown.add_command(label="Per saperne di più",
                                   command=show_about_message)
    menubar.add_cascade(label="Per saperne di più", menu=file_dropdown)

    welcome_label = tk.Label(window, bg="white",
                             text="Scegli una foto .bmp da comprimere:",
                             font=("Helvetica", 15))
    welcome_label.pack()
    welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)
    
    choice_button = tk.Button(text="Cerca", command=lambda:choice(window))
    
    choice_button.grid(row=2, column=0, sticky="WE", pady=20, padx=400)
    f_label = tk.Label(window,bg="white",
                             text="Scegli un valore intero F:",
                             font=("Helvetica", 14))
    
    f_label.grid(row=3, column=0, sticky="N", padx=20, pady=4)

    fchoice =ttk.Combobox(window, 
                            values=[i for i in range(1000)])
    
    fchoice.grid(row=4, column=0,sticky="WE",pady=20, padx=400 )
    
    fchoice.set("3")
    d_label = tk.Label(window,bg="white",
                        text="Scegli un valore intero d (compreso fra 0 e 2*F - 2): ",
                             font=("Helvetica", 14))
   
    d_label.grid(row=5, column=0, sticky="N", padx=20, pady=4)

    dchoice =ttk.Combobox(window, 
                            values=[i for i in range(1000)])
   
    dchoice.grid(row=6, column=0,sticky="WE",pady=20, padx=400 )
    dchoice.set("4")
    
    compress_button = tk.Button(text="Comprimi", 
                                command=lambda:compress(window,fchoice.get(),dchoice.get()))
    
    compress_button.grid(row=7,column=0,sticky="WE",pady=20,padx=400)
    window.mainloop()
        
if __name__ == "__main__":
    main()
    
