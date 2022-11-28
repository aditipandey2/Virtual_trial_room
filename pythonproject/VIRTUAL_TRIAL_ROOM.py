import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk

main_frame = cv2.imread("D:\\pythonproject\\Original_Image.jpg")
hsv = cv2.cvtColor(main_frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([ 80, 50, 50 ])
upper_blue = np.array([ 150, 255, 255 ])

mask_white = cv2.inRange(hsv, lower_blue, upper_blue)
mask_black = cv2.bitwise_not(mask_white)

W, L = mask_black.shape
mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
mask_black_3CH[ :, :, 0 ] = mask_black
mask_black_3CH[ :, :, 1 ] = mask_black
mask_black_3CH[ :, :, 2 ] = mask_black

W, L = mask_white.shape
mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
mask_white_3CH[ :, :, 0 ] = mask_white
mask_white_3CH[ :, :, 1 ] = mask_white
mask_white_3CH[ :, :, 2 ] = mask_white

dst3 = cv2.bitwise_and(mask_black_3CH, main_frame)
dst3_wh = cv2.bitwise_or(mask_white_3CH, dst3)

def F1():
    cv2.imshow('Orignal_Image', main_frame)
    design = cv2.imread("D:\\pythonproject\\Trial_TShirt1.jpg")
    design = cv2.resize(design, mask_black.shape[ 1::-1 ])
    cv2.imshow('Trial_TShirt1', design)

    design_mask_mixed = cv2.bitwise_or(mask_black_3CH, design)

    final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed, dst3_wh)
    cv2.imshow('Final_Image', final_mask_black_3CH)

    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.destroyAllWindows()


def F2():
    cv2.imshow('Orignal_Image', main_frame)
    design = cv2.imread("D:\\pythonproject\\Trial_TShirt2.jpg")
    design = cv2.resize(design, mask_black.shape[ 1::-1 ])
    cv2.imshow('Trial_TShirt2', design)

    design_mask_mixed = cv2.bitwise_or(mask_black_3CH, design)

    final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed, dst3_wh)
    cv2.imshow('Final_Image', final_mask_black_3CH)

    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.destroyAllWindows()


master = Tk()
myText = StringVar();
mylabel = Label(master, text=" Welcome to Virtual Trial Room!!\n\n Choose any one T-Shirt", font="Times 20 bold italic",
                padx=20, pady=15, bg="yellow", fg="blue")
mylabel.pack()

b1 = Button(master, text="Image1- Black and White design", font="Helvetica 15 bold", padx=15, pady=10, command=F1,
            bg="white", fg="black")
b1.pack()
b2 = Button(master, text="Image2- Red design", font="Helvetica 15 bold", padx=15, pady=10, command=F2, bg="white",
            fg="black")
b2.pack()

close = Label(master, text="Press 'q' to close the Image.", font="Times 10 bold italic", padx=10, pady=10, bg="yellow",
              fg="black")
close.pack()

master.mainloop()