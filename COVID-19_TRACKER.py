#Import Tkinter 
import tkinter as tk
#Import messagebox
from tkinter import messagebox
#Import ttk to style the application
from tkinter import ttk
#Import reportlab to create the PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#Import qrcode to generate QR
import qrcode

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
        
        #Initialize class attributes
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(expand=True, fill=tk.BOTH)
        
        self.personal_info_frame = ttk.Frame(self.notebook)
        self.emergency_frame = ttk.Frame(self.notebook)
        self.questions_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.personal_info_frame, text="Personal Info")
        self.notebook.add(self.emergency_frame, text="Emergency Contact")
        self.notebook.add(self.questions_frame, text="Health Questions")

        self.create_personal_info_tab()
        self.create_emergency_contact_tab()
        self.create_questions_tab()

#Create the Personal Info tab
    def create_personal_info_tab(self):
        #Styling the Personal Info tab's
        personal_info_frame = ttk.Frame(self.personal_info_frame, borderwidth=2, relief=tk.GROOVE)
        personal_info_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        #Create the Personal Info tab's label
        label_1 = tk.Button(personal_info_frame, text="Personal Information", bg="light blue", fg="black", font=("Times", 25))
        label_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        #Create a label and an entry widget for the user's first name
        first_name_label = tk.Label(personal_info_frame, text="FIRST NAME", fg="black", font=("Times", 14))
        first_name_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.first_name_entry = tk.Entry(personal_info_frame, width=30)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the user's last name
        last_name_label = tk.Label(personal_info_frame, text="LAST NAME", fg="black", font=("Times", 14))
        last_name_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.last_name_entry = tk.Entry(personal_info_frame, width=30)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the user's email
        email_label = tk.Label(personal_info_frame, text="EMAIL", fg="black", font=("Times", 14))
        email_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.email_entry = tk.Entry(personal_info_frame, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the user's phone number
        number_label = tk.Label(personal_info_frame, text="PHONE NUMBER", fg="black", font=("Times", 14))
        number_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)

        self.number_entry = tk.Entry(personal_info_frame, width=30)
        self.number_entry.grid(row=4, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the user's address
        address_label = tk.Label(personal_info_frame, text="ADDRESS", fg="black", font=("Times", 14))
        address_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

        address1_label = tk.Label(personal_info_frame, text="STREET ADDRESS", fg="black", font=("Times", 11))
        address1_label.grid(row=6, column=1, sticky=tk.N, padx=10, pady=5)

        self.address1_label = tk.Entry(personal_info_frame, width=30)
        self.address1_label.grid(row=5, column=1, padx=10, pady=5)

        address2_label = tk.Label(personal_info_frame, text="STREET ADDRESS LINE 2", fg="black", font=("Times", 11))
        address2_label.grid(row=8, column=0, sticky=tk.N, padx=10, pady=5)

        self.address2_label = tk.Entry(personal_info_frame, width=30)
        self.address2_label.grid(row=7, column=0, padx=10, pady=5)

        address3_label = tk.Label(personal_info_frame, text="CITY", fg="black", font=("Times", 11))
        address3_label.grid(row=8, column=1, sticky=tk.N, padx=10, pady=5)

        self.address3_label = tk.Entry(personal_info_frame, width=30)
        self.address3_label.grid(row=7, column=1, padx=10, pady=5)

        address4_label = tk.Label(personal_info_frame, text="STATE/PROVINCE", fg="black", font=("Times", 11))
        address4_label.grid(row=10, column=0, sticky=tk.N, padx=10, pady=5)

        self.address4_label = tk.Entry(personal_info_frame, width=30)
        self.address4_label.grid(row=9, column=0, padx=10, pady=5)
        
        address5_label = tk.Label(personal_info_frame, text="POSTAL/ZIPCODE", fg="black", font=("Times", 11))
        address5_label.grid(row=10, column=1, sticky=tk.N, padx=10, pady=5)

        self.address5_label = tk.Entry(personal_info_frame, width=30)
        self.address5_label.grid(row=9, column=1, padx=10, pady=5)

        #Adding a next button to proceed on the Emergency Contact tab
        next_button = tk.Button(personal_info_frame, text="Next", bg="light blue", fg="black", font=("Times", 14), command=self.show_create_emergency_contact_tab)
        next_button.grid(row=17, column=0, columnspan=2, padx=10, pady=10)

    #Create the Emergency Contact tab
    def show_create_emergency_contact_tab(self):
        self.notebook.select(self.emergency_frame)

    #Styling the Emergency Contact tab
    def create_emergency_contact_tab(self):
        emergency_frame = ttk.Frame(self.emergency_frame, borderwidth=2, relief=tk.GROOVE)
        emergency_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        #Create the Emergency Contact tab's label
        label_2 = tk.Button(emergency_frame, text="Emergency Contact", bg="light blue", fg="black", font=("Times", 25))
        label_2.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        #Create a label and an entry widget for the emergency contact's name
        emergency_name_label = tk.Label(emergency_frame, text="NAME", fg="black", font=("Times", 14))
        emergency_name_label.grid(row=12, column=0, sticky=tk.W, padx=10, pady=5)
        self.emergency_name_entry = tk.Entry(emergency_frame, width=30)
        self.emergency_name_entry.grid(row=12, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the emergency contact's number
        emergency_number_label = tk.Label(emergency_frame, text="PHONE NUMBER", fg="black", font=("Times", 14))
        emergency_number_label.grid(row=13, column=0, sticky=tk.W, padx=10, pady=5)
        self.emergency_number_entry = tk.Entry(emergency_frame, width=30)
        self.emergency_number_entry.grid(row=13, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the emergency contact's email
        emergency_email_label = tk.Label(emergency_frame, text="EMAIL", fg="black", font=("Times", 14))
        emergency_email_label.grid(row=14, column=0, sticky=tk.W, padx=10, pady=5)
        self.emergency_email_entry = tk.Entry(emergency_frame, width=30)
        self.emergency_email_entry.grid(row=14, column=1, padx=10, pady=5)

        #Create a label and an entry widget for the emergency contact's relationship to the user
        relationship_label = tk.Label(emergency_frame, text="RELATIONSHIP", fg="black", font=("Times", 14))
        relationship_label.grid(row=15, column=0, sticky=tk.W, padx=10, pady=5)
        self.relationship_entry = tk.Entry(emergency_frame, width=30)
        self.relationship_entry.grid(row=15, column=1, padx=10, pady=5)

        #Adding a next button to proceed on the Health Questions tab
        next_button = tk.Button(emergency_frame, text="Next", bg="light blue", fg="black", font=("Times", 14), command=self.show_questions_tab)
        next_button.grid(row=16, column=0, columnspan=2, padx=10, pady=10)

    #Create the Health Questions tab
    def show_questions_tab(self):
        self.notebook.select(self.questions_frame)

    def create_questions_tab(self):
        #Styling the Health Questions tab
        questions_frame = ttk.Frame(self.questions_frame,borderwidth=2, relief=tk.GROOVE)
        questions_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        #Create the Health Questions tab's label
        label_3 = tk.Button(questions_frame, text="Health Questions", bg="light blue", fg="black", font=("Times", 18))
        label_3.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        #Question 1
        question1_label = tk.Label(questions_frame, text="1. Have you been vaccinated for COVID-19?", fg="black", font=("Times", 12))
        question1_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        #Options for Question 1
        question1_options = [
            "Not Yet",
            "1st Dose",
            "2nd Dose (Fully Vaccinated)",
            "1st Booster Shot",
            "2nd Booster Shot"
        ]
        self.question1_var = tk.StringVar()
        self.question1_var.set("Not Yet")
        question1_dropdown = ttk.Combobox(questions_frame, textvariable=self.question1_var, values=question1_options, font=("Times", 10))
        question1_dropdown.grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky=tk.W)

        #Question 2
        question2_label = tk.Label(questions_frame, text="2. Are you experiencing any symptoms in the past 7 days such as:", fg="black", font=("Times", 12))
        question2_label.grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
        #Options for Question 2
        question2_options = [
            "Fever",
            "Cough",
            "Colds",
            "Muscle/body pains",
            "Sore throat",
            "Diarrhea",
            "Headache",
            "Shortness of breath",
            "Difficulty of breathing",
            "Loss of taste",
            "Loss of smell",
            "None of the above"
        ]
        self.question2_vars = [tk.IntVar() for _ in range(len(question2_options))]
        for i, option in enumerate(question2_options):
            tk.Checkbutton(questions_frame, text=option, variable=self.question2_vars[i], font=("Times", 10)).grid(row=4 + i, column=0, columnspan=2, padx=5, pady=2, sticky=tk.W)

        #Question 3
        question3_label = tk.Label(questions_frame, text="3. Have you had exposure to a probable or confirmed case in the last 14 days?", fg="black", font=("Times", 12))
        question3_label.grid(row=17, column=0, sticky=tk.W, padx=10, pady=5)
        #Options for Question 3
        question3_options = [
            "Yes",
            "No",
            "Uncertain"
        ]
        self.question3_var = tk.StringVar()
        self.question3_var.set("No")
        question3_options_dropdown = ttk.Combobox(questions_frame, textvariable=self.question3_var, values=question3_options, font=("Times", 10))
        question3_options_dropdown.grid(row=18, column=0, columnspan=2, padx=5, pady=2, sticky=tk.W)

        #Question 4
        question4_label = tk.Label(questions_frame, text="4. Have you had contact with somebody with symptoms in the past 7 days?", fg="black", font=("Times", 12))
        question4_label.grid(row=19, column=0, sticky=tk.W, padx=10, pady=5)
        #Options for Question 4
        question4_options = [
            "Yes",
            "No",
        ]
        self.question4_var = tk.StringVar()
        self.question4_var.set("No")
        question4_dropdown = ttk.Combobox(questions_frame, textvariable=self.question4_var, values=question4_options, font=("Times", 10))
        question4_dropdown.grid(row=20, column=0, columnspan=2, padx=5, pady=2, sticky=tk.W)

        #Question 5
        question5_label = tk.Label(questions_frame, text="5. Have you been tested for Covid-19 in the last 14 days?", fg="black", font=("Times", 12))
        question5_label.grid(row=21, column=0, sticky=tk.W, padx=10, pady=5)
        #Options for Question 5
        question5_options = [
            "No",
            "Yes-Positive",
            "Yes-Negative",
            "Yes-Pending"
        ]
        self.question5_var = tk.StringVar()
        self.question5_var.set("No")
        question5_dropdown = ttk.Combobox(questions_frame, textvariable=self.question5_var, values=question5_options, font=("Times", 10))
        question5_dropdown.grid(row=22, column=0, columnspan=2, padx=5, pady=2, sticky=tk.W)

        #Adding a Submit button to submit all informations
        submit_button = tk.Button(questions_frame, text="Submit", bg="light blue", fg="black", font=("Times", 14), command=self.submit_info)
        submit_button.grid(row=23, column=0, columnspan=2, padx=10, pady=10)

    #The information section
    def submit_info(self):
        personal_info = {
            "First Name": self.first_name_entry.get(),
            "Last Name": self.last_name_entry.get(),
            "Email": self.email_entry.get(),
            "Phone Number": self.number_entry.get(),
            "Street Address": self.address1_label.get(),
            "Street Address Line 2": self.address2_label.get(),
            "City": self.address3_label.get(),
            "State/Province": self.address4_label.get(),
            "Postal/Zipcode": self.address5_label.get(),
        }

        emergency_contact = {
            "Name": self.emergency_name_entry.get(),
            "Phone Number": self.emergency_number_entry.get(),
            "Email": self.emergency_email_entry.get(),
            "Relationship": self.relationship_entry.get(),
        }

        health_questions = {
            "Vaccination Status": self.question1_var.get(),
            "Symptoms": [option for i, option in enumerate([
                "Fever", "Cough", "Colds", "Muscle/body pains", "Sore throat",
                "Diarrhea", "Headache", "Shortness of breath", "Difficulty of breathing",
                "Loss of taste", "Loss of smell", "None of the above"
            ]) if self.question2_vars[i].get()],
            "Exposure to Confirmed Case": self.question3_var.get(),
            "Contact with Symptomatic Individual": self.question4_var.get(),
            "Covid-19 Testing": self.question5_var.get(),
        }

        # Combine all information
        all_info = {
            "Personal Information": personal_info,
            "Emergency Contact": emergency_contact,
            "Health Questions": health_questions,
        }

        #Message box to show all of the information being provided by the user
        message = "Thank you for submitting your information.\n\n"
        for section, data in all_info.items():
            message += f"{section}:\n"
            for key, value in data.items():
                message += f"{key}: {value}\n"
            message += "\n"

        # Include the privacy message in the message box
        message += "\nPrivacy Message:\n"
        message += "Your privacy is important to us. All the information shared for COVID-19 contact tracing will remain confidential and will be used solely for public health purposes."
        
        messagebox.showinfo("Your response has been submitted!", message)

        # Generate PDF and QR code
        self.create_pdf(all_info)
        self.generate_qr_code(message)

    #To generate PDF file copy with all of the information given by the user
    def create_pdf(self, data):
        canva = canvas.Canvas("covid_contact_tracing_data.pdf", pagesize=letter)
        canva.setFont("Helvetica", 11)

        # Calculate the middle of the page
        middle_x = letter[0] / 2
        top_margin_y = letter[1] - 36  # A little below the top margin (36 points)

        # Include the "Message Covid-19 Tracker" at the middle top
        canva.setFont("Helvetica-Bold", 20)
        canva.drawCentredString(middle_x, top_margin_y, "COVID CONTACT TRACING")

        current_y = top_margin_y - 40  # Adjust the current y-coordinate to move down after writing the header

        for section, section_data in data.items(): 
            canva.setFont("Helvetica-Bold", 14)
            canva.drawString(50, current_y, section)
            current_y -= 20
            for key, value in section_data.items():
                canva.setFont("Helvetica", 12)
                canva.drawString(50, current_y, f"{key}: {value}")
                current_y -= 20
            current_y -= 10

        # Include the privacy message in the PDF
        canva.setFont("Helvetica-Bold", 12)
        canva.drawString(50, current_y - 30, "Privacy Message")
        canva.setFont("Helvetica", 10)
        canva.drawString(50, current_y - 50, "Your privacy is important to us.All the information shared for COVID-19 contact tracing will remain")
        canva.setFont("Helvetica", 10)
        canva.drawString(50, current_y - 70, "confidential and will be used solely for public health purposes.")
        canva.setFont("Helvetica-Bold", 12)
        canva.drawString(50, current_y - 100, "Thank you for submitting your information.")

        canva.save()
    #To generate QR Code of the text file copy with all of the information given by the user
    def generate_qr_code(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("covid_contact_tracing_qr.png")


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = CovidContactTracingApp()
    app.run()