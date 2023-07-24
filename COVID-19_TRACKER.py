#Import Tkinter 
import tkinter as tk
#Import messagebox
from tkinter import messagebox
#Import ttk to style the application
from tkinter import ttk

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

        #Getting the consent of the user first if they will allow to share their personal informations
        consent = messagebox.askyesno("Consent Required", "By proceeding, you consent to provide your personal information for COVID-19 contact tracing. Do you agree?")
        if not consent:
            # If the user declines consent, exit the application
            return