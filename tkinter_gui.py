from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np
from tkinter import filedialog
window = Tk()
window.title("ColorBold")

# Gamma correction is also known as the Power Law Transform.
# First, our image pixel intensities must be scaled from the range [0, 255] to [0, 1.0].
# From there, we obtain our output gamma corrected image by applying the following equation:
# O = I ^ (1 / G)
# Where I is our input image and G is our gamma value. The output image O is then scaled back to the range [0, 255].


def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # https: // www.pyimagesearch.com / 2015 / 10 / 05 / opencv - gamma - correction /
    # Gamma values < 1 will shift the image towards the darker end of the spectrum
    # while gamma values > 1 will make the image appear lighter.A gamma value of G=1
    # will have no affect on the input image:
    # apply gamma correction using the lookup table

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def clicked():
    global lbl
    # global img
    global path
    # lbl.configure(text="Button was clicked !!")
    path = filedialog.askopenfilename()
    # Load an color image
    img = cv2.imread(path)

    # Rearrang the color channel
    b, g, r = cv2.split(img)
    img = cv2.merge((r, g, b))

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)

    # Put it in the display window
    lbl = Label(window, image=imgtk, width = 500, height = 500)
    lbl.image = imgtk
    lbl.grid(column=0, row=0)


def show_red():
    global lbl
    img = cv2.imread(path)
    # print(path)
    # print("yolo")
    light_img = adjust_gamma(img, 10)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i, j, 2] > 100 and img[i, j, 0] < 50 and img[i, j, 1] < 50):
                light_img[i, j] = img[i, j]

     # Rearrang the color channel
    b, g, r = cv2.split(light_img)
    light_img = cv2.merge((r, g, b))

    im = Image.fromarray(light_img)
    imgtk = ImageTk.PhotoImage(image=im)

    # im_temp = imgtk.resize((250, 250), Image.ANTIALIAS)

    # Put it in the display window
    lbl = Label(window, image=imgtk, width=500, height=500)
    lbl.image = imgtk
    lbl.grid(column=0, row=0)


def show_green():
    global lbl
    img = cv2.imread(path)
    # print(path)
    # print("yolo")
    light_img = adjust_gamma(img, 10)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j, 2] < 100 and img[i, j, 1] >80 and img[i, j, 0] < 100:
                light_img[i, j] = img[i, j]

    # Rearrange the color channel
    b, g, r = cv2.split(light_img)
    light_img = cv2.merge((r, g, b))

    im = Image.fromarray(light_img)
    imgtk = ImageTk.PhotoImage(image=im)

    # Put it in the display window
    lbl = Label(window, image=imgtk, width=500, height=500)
    lbl.image = imgtk
    lbl.grid(column=0, row=0)


def show_original():
    global lbl
    img = cv2.imread(path)

    # Rearrange the color channel
    b, g, r = cv2.split(img)
    img = cv2.merge((r, g, b))

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)

    # Put it in the display window
    lbl = Label(window, image=imgtk, width=500, height=500)
    lbl.image = imgtk
    lbl.grid(column=0, row=0)


lbl = None

btn = Button(window, text="Upload",bg="orange", fg="blue",command=clicked)
btn.grid(column=0, row=5)

btn_red = Button(window, text="Show Red",bg="orange", fg="Red",command=show_red)
btn_red.grid(column=1, row=1)

btn_green = Button(window, text="Show Green",bg="orange", fg="green",command=show_green)
btn_green.grid(column=1, row=2)

btn_show = Button(window, text="Show Original",bg="orange", fg="black",command=show_original)
btn_show.grid(column=1, row=3)

window.geometry('1000x1000')
window.mainloop()