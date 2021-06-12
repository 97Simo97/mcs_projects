import numpy
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from scipy.fftpack import dctn
from scipy.fftpack import idctn
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

img = []

# Funzione per generare finestra "Per saperne di più"
def show_about_message():

    box_title = "Compressione JPEG"
    box_message = "Un semplice software in grado di comprimere immagini .bmp \
     in toni di grigio secondo i parametri F e d scelti dall'utente"
    messagebox.showinfo(box_title, box_message)

# Funzione per far scegliere l'immagine all'utente
# Immagine letta con libreria cv2 e convertita in toni di grigio
def choice(window):

    global img

    filename = filedialog.askopenfilename(
        defaultextension = ".bmp",
        filetypes=[("Tutti i file", "*.*"),
                   ("Foto in toni di grigio bitmap", "*.bmp"),])

    if filename:
        sud_label = tk.Label(window, text="File caricato: " + f"{filename}")
        sud_label.grid(row = 9, column =0 , sticky = "S", pady = 20)
        img_old = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = numpy.array(img_old)
    else:
        img = []

# Funzione che effettua la compressione dell'immagine
def compress(window, f, d):

    global img

    if (not(numpy.array_equal(img, []))):
        if (f != "" and d != ""):
            f = int(f)
            d = int(d)
            if (d >= 0 and d <= (2 * f - 2)):
                if(f <= img.shape[0] and f <= img.shape[1]):
                    blocchi = decompose(f)
                    blocchi = dct2(blocchi, d)
                    immagine_compressa = compose(blocchi, f)
                    show(img, immagine_compressa)
                else:
                    messagebox.showerror("Errore", "Il parametro F deve essere inferiore alle dimensioni dell'immagine")
            else:
                messagebox.showerror("Errore", "Il parametro d deve essere compreso fra 0 e (2F - 2)")
        elif (f == "" and d != ""):
            messagebox.showerror("Errore", "Immagine caricata, ma parametro F non selezionato")
        elif (f != "" and d == ""):
            messagebox.showerror("Errore", "Immagine caricata, ma parametro d non selezionato")
        else:
            messagebox.showerror("Errore", "Immagine caricata, ma parametri F e d non selezionati")
    else:
         if (f != "" and d != ""):
            messagebox.showerror("Errore", "Immagine non caricata")
         elif (f == "" and d != ""):
            messagebox.showerror("Errore", "Immagine non caricata e parametro F non selezionato")
         elif (f != "" and d == ""):
            messagebox.showerror("Errore", "Immagine non caricata e parametro d non selezionato")
         else:
            messagebox.showerror("Errore", "Immagine non caricata e parametri F e d non selezionati")

# Funzione che suddivide l’immagine in blocchi quadrati di pixel
# di dimensioni F×F partendo in alto a sinistra, scartando gli avanzi
def decompose(f):

    global img
    blocchi = []  
    k = 0
    p = 0

    for i in range (int((len(img))/f)):
        for j in range (int((len(img[0]))/f)):
            blocco = img[k : f + k, p : f + p]
            blocchi.append(blocco)

            p += f  
        k += f
        p = 0 

    return blocchi

# Funzione che applica la DCT2 ad ogni blocco dell'immagine
# ed elimina le frequenze c[k, l] con k + l >= d
def dct2(blocchi, d):

    nuovi_blocchi = []

    for b in blocchi:
        # DCT2 sul blocco
        bloccodct = dctn(b, type = 2, norm = 'ortho')

        # Eliminazione frequenze
        for k in range(len(bloccodct)):
            for l in range(len(bloccodct[0])):
                if (k + l) >= d:
                    bloccodct[k, l] = 0

        # IDCT2 sul blocco
        bloccoidct = idctn(bloccodct, type = 2, norm = 'ortho')

        # Arrotondamento dei valori all'intero piu vicino
        # I valori minori di 0 vengono messi a 0
        # I valori maggiori di 255 vengono messi a 255
        for k in range(len(bloccoidct)):
            for l in range(len(bloccoidct[0])):
                bloccoidct[k, l] = int(round(bloccoidct[k, l],0))
                if (bloccoidct[k, l] < 0):
                    bloccoidct[k, l] = 0
                elif (bloccoidct[k, l] > 255):
                    bloccoidct[k, l] = 255

        nuovi_blocchi.append(bloccoidct)

    return nuovi_blocchi

# Funzione che ricompone l’immagine mettendo insieme i blocchi nell’ordine giusto
def compose(blocchi, f):

    global img
    nblocks = len(blocchi)
    index = 0
    ncol = int(len(img[0]) - (len(img[0]) % f))
    nblocks_per_row = int(ncol / f)

    immagine_compressa = numpy.array([],  dtype = numpy.int64).reshape(0, ncol)

    for i in range(int(nblocks / nblocks_per_row)):
        blocchi_da_comporre = blocchi[index : index + nblocks_per_row]
        index += nblocks_per_row
        immagine_compressa = numpy.vstack((immagine_compressa, numpy.hstack(blocchi_da_comporre)))

    cv2.imwrite('immagine_compressa.bmp', immagine_compressa)

    return immagine_compressa 

# Funzione che visualizza sullo schermo l’immagine originale e l’immagine compressa affiancate
def show(img,new_img):

    window = tk.Tk()
    window.geometry('1000x1000')
    window.wm_title("Risultato")
    comparison = Figure(figsize = (6, 6), dpi = 100) 
    comparison.add_subplot(121).imshow(img, cmap = 'gray', vmin = 0, vmax = 255)
    comparison.add_subplot(122).imshow(new_img, cmap = 'gray', vmin = 0, vmax = 255)
    canvas = FigureCanvasTkAgg(comparison, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side = "top", fill = "both", expand = 1)
    window.mainloop()

# Main
def main():

    global img
    window = tk.Tk()
    window.geometry("900x500")
    window.title("Compressione JPEG")
    window.grid_columnconfigure(0, weight = 1)
    window.configure(background = 'white')
    menubar = tk.Menu(window, font=("Helvetica", 10))
    window.config(menu = menubar)
    file_dropdown = tk.Menu(menubar, font = ("Helvetica", 12), tearoff = 0)
    file_dropdown.add_command(label = "Per saperne di più", command = show_about_message)
    menubar.add_cascade(label = "Per saperne di più", menu = file_dropdown)

    welcome_label = tk.Label(window, bg = "white", text = "Scegli una foto .bmp da comprimere:", font = ("Helvetica", 15))
    welcome_label.pack()
    welcome_label.grid(row = 0, column = 0, sticky = "N", padx = 20, pady = 10)

    choice_button = tk.Button(text = "Cerca", command = lambda:choice(window))

    choice_button.grid(row = 2, column = 0, sticky = "WE", pady = 20, padx = 400)
    f_label = tk.Label(window, bg = "white", text = "Scegli il parametro F:", font = ("Helvetica", 14))

    f_label.grid(row = 3, column = 0, sticky = "N", padx = 20, pady = 4)

    fchoice = ttk.Combobox(window, values = [i for i in range(1000)])

    fchoice.grid(row = 4, column = 0,sticky = "WE", pady = 20, padx = 400)

    fchoice.set("3")
    d_label = tk.Label(window, bg = "white", text = "Scegli il parametro d compreso fra 0 e (2F - 2):", font = ("Helvetica", 14))

    d_label.grid(row = 5, column = 0, sticky = "N", padx = 20, pady = 4)

    dchoice = ttk.Combobox(window, values = [i for i in range(1000)])

    dchoice.grid(row = 6, column = 0, sticky = "WE", pady = 20, padx = 400)
    dchoice.set("4")

    compress_button = tk.Button(text="Comprimi", command = lambda:compress(window, fchoice.get(), dchoice.get()))

    compress_button.grid(row = 7, column = 0, sticky = "WE", pady = 20, padx = 400)
    window.mainloop()

if __name__ == "__main__":
    main()