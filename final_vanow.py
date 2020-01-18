import time

from tkinter import *
from tkinter import messagebox
from datetime import datetime
from twilio.rest import Client


class Application:
    def __init__(self):
        def read_file():
            try:
                infile = open("config.txt", "r")
                line = infile.readline()
                for i in range(0, 4):
                    if (i == 0):
                        accountSID = line.rstrip()
                        line = infile.readline()
                    elif (i == 1):
                        authToken = line.rstrip()
                        line = infile.readline()
                    elif (i == 2):
                        twilioNum = line.rstrip()
                        line = infile.readline()
                    elif (i == 3):
                        sendNum = line.rstrip()
            except IOError:
                print("File Not Found!")

            return accountSID, authToken, twilioNum, sendNum

        def get_duration():
            try:
                dur = self.waitEntry.get()
                dt = datetime.strptime(dur, "%H%M%S")
            except  ValueError:
                messagebox.showinfo('Error', 'Invalid Entry! Try Again')

            hours = dt.hour
            minutes = dt.minute
            seconds = dt.second

            total = ((hours * 86400) + (minutes * 60) + seconds)
            # print(total)
            return total


        def send():
            message = self.reminderEntry.get()
            dur = get_duration()

            time.sleep(dur)
            message = client.messages.create(body=message, from_=twilioNum, to=sendNum)
            messagebox.showinfo('Congratulations', 'Message Sent!')


        #def tick():



        # Window Creation
        self.main_window = Tk()
        self.main_window.geometry("400x100")

        # frames
        self.frame0 = Frame(self.main_window)
        self.frame1 = Frame(self.main_window)
        self.frame2 = Frame(self.main_window)
        self.frame3 = Frame(self.main_window)

        # Top Frame
        self.value = StringVar()
        self.clock = Label(self.frame0,
                           textvariable=self.value)
        self.value.set('Text Reminder')

        # Bottom Frame
        self.reminder = Label(self.frame1,
                              text='Enter Your Message: ')
        self.reminderEntry = Entry(self.frame1, width=30)

        self.wait = Label(self.frame2,
                          text='How long to wait HHMMSS: ')
        self.waitEntry = Entry(self.frame2,
                               width=6)

        self.quitButton = Button(self.frame3,
                                 text='Quit',
                                 command=self.main_window.destroy)
        self.sendButton = Button(self.frame3,
                                 text='Send',
                                 command=send)

        # Pack
        self.clock.pack(side='top')

        self.reminder.pack(side='left')
        self.reminderEntry.pack(side='right')
        self.wait.pack(side='left')
        self.waitEntry.pack(side='right')
        self.quitButton.pack(side='left')
        self.sendButton.pack(side='right')

        self.frame0.pack(side='top')
        self.frame1.pack(side='top')
        self.frame2.pack(side='top')
        self.frame3.pack(side='top' )

        #Set Up
        accountSID, authToken, twilioNum, sendNum = read_file()
        client = Client(accountSID, authToken)

        mainloop()


app = Application()