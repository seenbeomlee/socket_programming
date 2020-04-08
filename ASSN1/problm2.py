import sys, time
from socket import *
# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # in second

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
# myCode Here
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
# myCode Here
clientsocket.settimeout(1)
# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
	ptime += 1
	# Format the message to be sent
	data = "Ping " + str(ptime) + " " + time.asctime()
    
	try:
	# Sent time
		RTTb = time.time()
	# Send the UDP packet with the ping message
		# myCode Here
		clientsocket.sendto(data.encode(), (host, port))
	# Receive the server response
		# myCode Here
		message, address = clientsocket.recvfrom(2048)
	# Received time
		RTTa = time.time()
	# Display the server response as an output
		# myCode Here
		print("Reply from " + address[0] + ": " + message.decode())
	# Round trip time is the difference between sent and received time
		print("RTT: " + str(RTTa - RTTb))
	except:
		# Server does not response
	# Assume the packet is lost
		print ("Request timed out.")
		continue

# Close the client socket
# myCode Here
clientsocket.close()

