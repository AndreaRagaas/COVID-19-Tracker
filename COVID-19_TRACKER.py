#Import Tkinter 
import tkinter as tk

#Create the Application's class
class CovidContactTracingApp:
    def __init__(self):
        #Create a new window
        self.window = tk.Tk()
        #Adjust the windows size
        self.window.geometry("400x400")
        #Create a window title
        self.window.title("Covid Contact Tracing App")
        #Change the windows background color
        self.window.configure(background="light blue")        