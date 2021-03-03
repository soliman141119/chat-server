# import all the required modules 
from PIL import ImageTk,Image
import  PIL
import urllib.request

import socket 
import threading 
from tkinter import *
from tkinter import font 
from tkinter import ttk  
from datetime import datetime
port = 5050
host = socket.gethostbyname(socket.gethostname()) 
add = (host, port) 
FORMAT = "utf-8"
 
client = socket.socket(socket.AF_INET, 
					socket.SOCK_STREAM) 
client.connect(add) 
 
class GUI: 
	# constructor method 
	def __init__(self): 
		
		# chat window which is currently hidden 
		self.Window = Tk() 
		self.Window.withdraw() 
		
		# login window 
		self.login = Toplevel() 
		# set the title 
		self.login.title("Login")
		self.login.resizable(width = False, 
							height = False) 
		self.login.configure(width = 400, 
							height = 200,bg = "white") 
  
		self.imu=PIL.Image.open('user3.png')
		self.imu.thumbnail((90,40))
		self.imu=ImageTk.PhotoImage(self.imu)
		self.us = Label(self.login, 
					text = "Please ",height=40, 
					image=self.imu, 
					font = "Helvetica 14 bold",bg='white',bd=0) 
		
		self.us.place( relwidth = 0.1,relheight = 0.15, 
							relx=0.01,
							rely = 0.03) 
		# create a Label 
		self.pls = Label(self.login, 
					text = "login", 
					justify = CENTER, 
					font = "Helvetica 12 bold",bg='white',fg='black') 
		
		self.pls.place(relheight = 0.15, 
					relx = 0.3, 
					rely = 0.03) 
		# create a Label 
		self.labelName = Label(self.login, 
							text = "Name: ", 
							font = "Helvetica 12 bold",bg='white',fg='black') 
		
		self.labelName.place(relwidth = 0.2,
							 relheight = 0.18, 
							  
							rely = 0.3) 
		
		# create a entry box for 
		# tyoing the message 
		self.entryName = Entry(self.login, 
							font = "Helvetica 14",bg='#ADD8E6') 
		
		self.entryName.place(relwidth = 0.6, 
							relheight = 0.18, 
							relx = 0.3, 
							rely = 0.3) 
		
		# set the focus of the curser 
		self.entryName.focus() 
		self.imi=PIL.Image.open('e1.png')
		self.imi.thumbnail((90,40))
		self.imi=ImageTk.PhotoImage(self.imi)
		# create a Continue Button 
		# along with action 
		self.go = Button(self.login,
						image=self.imi,
						text = "CONTINUE", 
						font = "Helvetica 11 bold",bd=0,
						command = lambda: self.goAhead(self.entryName.get()),bg='white') 
		
		self.go.place(relx = 0.75, 
					rely = 0.5) 
		self.Window.mainloop() 
  # end login window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# start chatroom window
	def goAhead(self, name): 
		self.login.destroy() 
		self.layout(name) 
		
		# the thread to receive messages 
		rcv = threading.Thread(target=self.receive) 
		rcv.start() 

	# The main layout of the chat 
	def layout(self,name): 
		
		self.name = name 
		# to show chat window 
		self.Window.deiconify() 
		self.Window.title("CHATROOM") 
		self.Window.resizable(width = False, 
							height = False) 
		self.Window.configure(width = 470, 
							height = 550, 
							bg = "black")
		
		self.imua=PIL.Image.open('user4.png')
		self.imua.thumbnail((90,20))
		self.imua=ImageTk.PhotoImage(self.imua)
		
		self.labelHead = Label(self.Window, 
							bg = "white", 
							fg = "Purple", 
							image=self.imua , 
							font = "Helvetica 13 bold"
							 )
		self.labelHead.place(relwidth =0.09)
		self.labelHead1 = Label(self.Window, 
							bg = "white", 
							fg = "Purple",
							text = self.name , 
							font = "Helvetica 13 bold"
							 )
		self.labelHead1.place(relx=0.1,relwidth =0.9)
  
  #>>>>>>>>>>>>>>>>>>>>>>
  # frame image
		self.labelimag= LabelFrame(self.Window,
							 text="Iamge",
							 fg='white',
							 bg = "black", 
							 height = 400,
							 width=195)
		self.labelimag.place(x = 260 ,y=50)
		self.lblimg=Label(self.labelimag,height = 60,
							bg='black',
							width=50)
		self.lblimg.place(relwidth =1,relheight=0.8)
		self.enulr=Entry(self.labelimag, 
							bg = "#ADD8E6", 
							fg = 'black', 
							font = "Helvetica 10") 

		self.enulr.place(relwidth = 1, 
							relheight = 0.08, 
							rely = 0.8, 
							relx = 0) 
		self.enulr.focus()
  
	   
		self.imdl=PIL.Image.open('dl.png')
		self.imdl.thumbnail((90,40))
		self.imdl=ImageTk.PhotoImage(self.imdl)
		self.bttonMsg = Button(self.labelimag, 
								text = "change", 
								font = "Helvetica 10 bold",
								image=self.imdl,
								width = 20, 
								bg = "white",command=lambda: self.DownloadImage(self.enulr.get()))
		self.bttonMsg.place(relwidth = 1, 
							relheight = 0.098, 
							rely = 0.9, 
							relx = 0)
  # end frame image
  
		self.line = Label(self.Window, width = 450, bg = "Purple") 

		self.line.place(relwidth = 1, rely = 0.05, relheight = 0.02) 

		self.textCons = Text(self.Window, width = 20, height = 2, 
							bg = "black", fg = "green", 
							font = "Helvetica 8", padx = 5, pady = 5) 
		
		self.textCons.place(relheight = 0.745, 
							relwidth = 0.545, 
							rely = 0.08) 
			
		
		self.labelBottom = Label(self.Window, 
								bg = "white", 
								height = 80) 
		
		self.labelBottom.place(relwidth = 1, 
							rely = 0.925) 
		
		self.entryMsg = Entry(self.labelBottom, 
							bg = "#ADD8E6", 
							fg = "black", 
							font = "Helvetica 13") 
		
		# place the given widget 
		# into the gui window 
		self.entryMsg.place(relwidth = 0.555, 
							relheight = 0.02, 
							rely = 0.008, 
							relx = 0.011) 

		self.entryMsg.focus() 
  
		self.im=PIL.Image.open('e2.png')
		self.im.thumbnail((90,40))
		self.im=ImageTk.PhotoImage(self.im)
		# create a Send Button 
		self.buttonMsg = Button(self.labelBottom, 
								image=self.im, 
								font = "Helvetica 10 bold", 
								width=12, height=5,
								bg = "white",bd=0,
								command = lambda : self.sendButton(self.entryMsg.get())) 
		
		self.buttonMsg.place(relx = 0.7, 
							 
							relheight = 0.03, 
							relwidth = 0.16) 
		#
		self.textCons.config(cursor = "arrow") 
		#
		# create a scroll bar 
		scrollbar = Scrollbar(self.textCons) 
		#
		# place the scroll bar 
		# into the gui window 
		scrollbar.place(relheight = 1, relx = 0.974)
		scrollbar.config(command = self.textCons.yview)
		self.textCons.config(state = DISABLED) 

	# function to basically start the thread for sending messages 
	def sendButton(self, msg): 
		self.textCons.config(state = DISABLED) 
		self.msg=msg 
		self.entryMsg.delete(0, END) 
		snd= threading.Thread(target = self.sendMessage) 
		snd.start() 

	# function to receive messages 
	def receive(self): 
		while True: 
			try: 
				message = client.recv(1024).decode(FORMAT) 
				
				# if the messages from the server is NAME send the client's name 
				if message == 'NAME': 
					client.send(self.name.encode(FORMAT)) 
				else: 
					# insert messages to text box 
					self.textCons.config(state = NORMAL) 
					self.now = datetime.now()
					current_time = self.now.strftime("(%D-%H:%M)")
					self.textCons.insert(END, 
										current_time+"\n") 
					self.textCons.insert(END, 
										message+"\n\n\n") 
 
					self.textCons.config(state = DISABLED) 
					self.textCons.see(END) 
			except: 
				# an error will be printed on the command line or console if there's an error 
				print("An error occured!") 
				client.close() 
				break
		
	# function to send messages 
	def sendMessage(self): 
		self.textCons.config(state=DISABLED) 
		while True: 
			message = (f"{self.name}: {self.msg}") 
			client.send(message.encode(FORMAT))	 
			break	
	#function to download image 
	def DownloadImage(self,x):
		if(x!=''):
			urllib.request.urlretrieve(x,'url.jpg')
		 
		self.img2=PIL.Image.open('url.jpg')
		self.img2.thumbnail((350,600))
		self.img2=PIL.ImageTk.PhotoImage(self.img2)
		self.lblimg.configure(image=self.img2)
		self.lblimg.image=self.img2
# create a GUI class object 
g = GUI() 
