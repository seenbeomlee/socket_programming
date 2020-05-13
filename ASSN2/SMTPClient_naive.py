import ssl
from socket import *
import base64

username = 'nm160@postech.ac.kr' #'your_postech_id@postech.ac.kr'
password = '' #'your_password'             # IMPORTANT NOTE!!!!!!!!!!: PLEASE REMOVE THIS FIELD WHEN YOU SUBMIT!!!!!

subject = 'Computer Network Assignment2 - Email Client'
from_ = 'nm160@postech.ac.kr'
to_ = 'nm160@postech.ac.kr'
content = 'It is so hard for me!!!'

# Message to send
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.office365.com'
port = 587

# 1. Establish a TCP connection with a mail server [2pt]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
# 2. Dialogue with the mail server using the SMTP protocol. [2pt]
recv = clientSocket.recv(1024).decode()
print("reply: " + recv)

ehloCommand = 'EHLO SB\r\n'
clientSocket.send(ehloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("reply: " + recv1)
# 3. Login using SMTP authentication using your postech account. [5pt]
# HINT: Send STARTTLS
starCommand = 'STARTTLS \r\n'
clientSocket.send(starCommand.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("reply:" + recv2)

# HINT: Wrap socket using ssl.PROTOCOL_SSLv23
wrappedsocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

# HINT: Use base64.b64encode for the username and password
'''
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = 'AUTH PLAIN '.encode()+base64_str+'\r\n'.encode()
print('**********CHECK**********1')
'''

# HINT: Send EHLO
ehloCommand2 = 'EHLO SB\r\n'
wrappedsocket.send(ehloCommand2.encode())
recv3 = wrappedsocket.recv(1024)
recv3 = recv3.decode()
print("reply: " + recv3)
#print('**********CHECK**********2')
###################################
authMsg = 'AUTH LOGIN\r\n'

wrappedsocket.send(authMsg.encode())
recv4 = wrappedsocket.recv(1024)
recv4 = recv4.decode()
print("reply: " + recv4)
#print('**********CHECK**********3')

user64 = base64.b64encode(username.encode('utf-8'))
pass64 = base64.b64encode(password.encode('utf-8'))
wrappedsocket.send(user64+'\r\n'.encode())
recv5 = wrappedsocket.recv(1024)
recv5 = recv5.decode()
print("reply: " + recv5)
#print('**********CHECK**********4')

wrappedsocket.send(pass64+'\r\n'.encode())
recv6 = wrappedsocket.recv(1024)
recv6 = recv6.decode()
print("reply: " + recv6)
#print('**********CHECK**********5')

heloCommand = 'helo SB\r\n'
wrappedsocket.send(heloCommand.encode())
recv_h = wrappedsocket.recv(1024)
recv_h = recv_h.decode()
print("reply: " + recv_h)

# 4. Send a e-mail to your POSTECH mailbox. [5pt]
mailFrom = 'MAIL FROM:<'+from_+'>\r\n'
wrappedsocket.send(mailFrom.encode())
recv7 = wrappedsocket.recv(1024)
recv7 = recv7.decode()
print("reply: " + recv7)

rcptTo = 'RCPT TO:<'+to_+'>\r\n'
wrappedsocket.send(rcptTo.encode())
recv8 = wrappedsocket.recv(1024)
recv8 = recv8.decode()
print("reply: " + recv8)

data = 'DATA\r\n'
wrappedsocket.send(data.encode())
recv9 = wrappedsocket.recv(1024)
recv9 = recv9.decode()
print("reply: " + recv9)
##
subject = "Subject: " + subject +"\r\n\r\n"
wrappedsocket.send(subject.encode())
mailbody = content + '\r\n'
wrappedsocket.send(mailbody.encode())
wrappedsocket.send(endmsg.encode())
recv_e = wrappedsocket.recv(1024)
recv_e = recv_e.decode()
print("reply: " + recv_e)
##
quit = "QUIT\r\n"
wrappedsocket.send(quit.encode())
recv_q = wrappedsocket.recv(1024)
recv_q = recv_q.decode()
print("reply: " + recv_q)
# 5. Destroy the TCP connection [2pt]
wrappedsocket.close()