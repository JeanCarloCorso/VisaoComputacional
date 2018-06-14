# -*- coding: utf-8 -*-
from Tkinter import *
import cv2

class Application:
    def __init__(self, master=None):
        
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Escolha um filtro para sua camera")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()
  
        self.original = Button(self.segundoContainer)
        self.original["text"] = "Normal"
        self.original["font"] = ("Calibri", "8")
        self.original["width"] = 32
        self.original["command"] = self.CameraNormal
        self.original.pack()

        self.original = Button(self.terceiroContainer)
        self.original["text"] = "Bordas"
        self.original["font"] = ("Calibri", "8")
        self.original["width"] = 32
        self.original["command"] = self.CameraBordas
        self.original.pack()

        self.original = Button(self.quartoContainer)
        self.original["text"] = "Preto e Branco"
        self.original["font"] = ("Calibri", "8")
        self.original["width"] = 32
        self.original["command"] = self.CameraOtsu
        self.original.pack()

        self.camera = Button(self.quintoContainer)
        self.camera["text"] = "Tons de Cinza"
        self.camera["font"] = ("Calibri", "8")
        self.camera["width"] = 32
        self.camera["command"] = self.CameraGray
        self.camera.pack()
        
    def CameraBordas(self):
        captura = cv2.VideoCapture(0) 

        while(1):
            ret, frame = captura.read()
            img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            bordas = cv2.Canny(img,70,200)
            cv2.imshow("Bordas", bordas)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
            	break
        captura.release
        cv2.destroyAllWindows()

    def CameraNormal(self):
        captura = cv2.VideoCapture(0) 

        while(1):
        	ret, frame = captura.read()

        	cv2.imshow("Normal", frame)

        	k = cv2.waitKey(30) & 0xff
        	if k == 27:
        		break
        captura.release
        cv2.destroyAllWindows()

    def CameraOtsu(self):
        captura = cv2.VideoCapture(0) 

        while(1):
            ret, frame = captura.read()
            img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            galssiana = cv2.GaussianBlur(img,(11,11),0)
            ret,otsu_suav = cv2.threshold(galssiana,127,255,cv2.THRESH_OTSU)
            
            cv2.imshow("Preto e Branco", otsu_suav)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
            	break
        captura.release
        cv2.destroyAllWindows()

    def CameraGray(self):
        captura = cv2.VideoCapture(0) 

        while(1):
        	ret, frame = captura.read()
        	img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        	cv2.imshow("Tons de Cinza", img)

        	k = cv2.waitKey(30) & 0xff
        	if k == 27:
        		break
        captura.release
        cv2.destroyAllWindows()

root = Tk()
Application(root)
root.mainloop()