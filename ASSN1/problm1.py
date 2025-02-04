# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

# myCode Here
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
# myCode Here
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
# myCode Here
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
	print('The server is ready to receive')

	# Set up a new connection from the client
	# myCode Here
	connectionSocket, addr = serverSocket.accept()

	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client
		# myCode Here
		message = connectionSocket.recv(1024)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		# myCode Here
		filename = message[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire content of the requested file in a temporary buffer
		outputdata = f.read()
		# Send the HTTP response header line to the connection socket
		# myCode Here
		connectionSocket.send(message[1:])

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		# Send “\r\n” to the connection socket.
		# myCode Here
		connectionSocket.send("\r\n".encode())
		
		# Close the client connection socket
		# myCode Here
		connectionSocket.close()

	except IOError:
			# Send HTTP response message for file not found
			# myCode Here
			msg = "404 Not Found"
			# myCode Here
			connectionSocket.send(msg.encode())
			# Close the client connection socket
			# myCode Here
			connectionSocket.close()

# Close the server socket
# myCode Here
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
