
from datetime import datetime
import socket
import threading 
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
clients, names = [], []
server = socket.socket(socket.AF_INET, 
					socket.SOCK_STREAM) 
server.bind(ADDRESS) 
def startChat(): 
	print("server is working on " + SERVER) 
 
	server.listen() 
	
	while True:
		conn, addr = server.accept()
		conn.send("NAME".encode(FORMAT))   
		name = conn.recv(1024).decode(FORMAT) 
		names.append(name) 
		clients.append(conn) 
		print(f"Name is :{name}")
		now = datetime.now()
		current_time = now.strftime("(%D-%H:%M\n)")
		# broadcast message 
		broadcastMessage(f"      {name} has joined the chat!".encode(FORMAT)) 
		#conn.send('Connection successful!'.encode(FORMAT)) 
		# Start the handling thread 
		thread = threading.Thread(target = handle, 
								args = (conn, addr)) 
		thread.start() 
		# no. of clients connected 
		# to the server 
		print(f"active connections {threading.activeCount()-1}") 

# method to handle the 
# incoming messages 
def handle(conn, addr): 
	
	print(f"new connection {addr}") 
	connected = True
	
	while connected: 
		# recieve message 
		message = conn.recv(1024) 
		
		# broadcast message 
		broadcastMessage(message) 
	
	# close the connection 
	conn.close() 

# method for broadcasting 
# messages to the each clients 
def broadcastMessage(message): 
	for client in clients: 
		client.send(message) 

# call the method to 
# begin the communication 
startChat() 
