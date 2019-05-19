
#Name: Hari Hara Kummi Nakashatrala
import socket
import random
import time
from tkinter import *
from tkinter import StringVar
import datetime
from threading import Thread

#server host and port number
host = '127.0.0.1'
port = 80
#socket properties defined with inbuilt methods
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#creating TK inter
display = Tk()
display.title("Client")
display.geometry("500x300")
text = Text(display, height=15, width=45)




#declaring the global variables
post = "POST /"
http = "HTTP/1.1 \n"
#mentioned about all the HTTP formats in the requests between client and server
#HTTP formats decsribed here as per the problem statement
host_name = "Host:" + str(host) +"\n"
user_agent = "User-Agent: Python/3.6 + \n"
content_type = "text/html \n"

#function to generate random numbers between 3 to 10 and send to server
def random_generator():
    try:
        #sending random nunber post to the server
        random_number = random.randint(3, 10)
        random_number_str = str(random_number)
        random_number_header = post + random_number_str + http + host_name + user_agent + content_type + str(len(bytes(random_number_str, 'utf-8')))
        skt.send(bytes(random_number_header, 'utf-8'))
        start_time = time.time()


        #waiting for the response from the server
        server_response_bytes = skt.recv(1024)
        end_time = time.time()

        #after a while we get the response from client send the response message to the client
        server_response = server_response_bytes.decode('utf-8')
        print(server_response)
        response_after_post = server_response.split('POST /')[1]
        response = response_after_post.split('HTTP/1.1')[0]

        #print the responses in the tkinter window
        text.insert(INSERT, "\n"+ response + "( Time waited : " + str(end_time-start_time) + " sec)")
        print(random_number)
        print(end_time-start_time)
        print(datetime.datetime.now())
        val = int(random_number_str) * 100

        #evaluvate the random numbers and stop the processes based on it
        temp = "true"
        display.after(val, random_generator)
    except:
        text.insert(INSERT,"disconnected from the server" )
        print("disconnected from the server")

#this function helps to close the client window in the tkinter gui
def close_connection():
    q = "quit"
    #send all the quitting ,essage to the server
    quit_mess = post + q + http + host_name + user_agent + content_type + str(len(bytes(q, 'utf-8')))
    print(quit_mess)
    #send the close messages to the server
    skt.send(bytes(quit_mess, 'utf-8'))
    skt.close()
    display.quit()

#client connecting to server
try:
    skt.connect((host, port))

except:
    print("Unable to connect to the server on given port")


def main():
    text.insert(INSERT, "Connected to the server")
    #appends username to the client server
    username_header_bytes = skt.recv(1024)
    username_header = username_header_bytes.decode('utf-8')
    #print(username_header)
    after_rec = username_header.split('GET /')[1]
    username_request = after_rec.split('HTTP/1.1')[0]
    if username_request == "Username ":
        #Sending username header to the server
        my_name = str(skt.getsockname()[1])
        my_name_bytes = bytes(my_name, 'utf-8')
        username_sending_header = "HTTP/1.1 200 OK \n Content-type: text/html \n Content-length: " + str(len(my_name_bytes)) + "\n "
        #print(username_sending_header)
        skt.send(bytes(username_sending_header, 'utf-8'))
        #sending username to server
        time.sleep(0.1)
        skt.send(bytes(my_name, 'utf-8'))
    #initialise buttons in the window
    teeeemp = "true"
    random_generator()

button = Button(display, text="exit", command=close_connection)


def initialize():
    t = Thread(target=main)
    t.start()
    text.pack()
    button.pack()
    display.mainloop()



if __name__ == '__main__':
    initialize()


###################################################################
#References:
#https://docs.python.org/2/library/socket.html
#https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server
#http://blog.wachowicz.eu/?p=256
#https://www.thoughtco.com/building-a-simple-web-server-2813571
#https://elearn.uta.edu/bbcswebdav/pid-7205400-dt-content-rid-132005341_2/courses/2185-COMPUTER-NETWORKS-54684-003/Programming%20Assignment%201_reference_Python.pdf
#https://stackoverflow.com/questions/32168871/tkinter-with-multiple-threads
#https://stackoverflow.com/questions/42222425/python-sockets-multiple-messages-on-same-connection
#https://www.programcreek.com/python/example/105552/tkinter.Message
#https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
#https://scorython.wordpress.com/2016/06/27/multithreading-with-tkinter/
#https://docs.python.org/3/tutorial/classes.html
#https://stackoverflow.com/questions/46788776/update-tkinter-widget-from-main-thread-after-worker-thread-completes
#https://stackoverflow.com/questions/3567238/threaded-tkinter-script-crashes-when-creating-the-second-toplevel-widget
#https://stackoverflow.com/questions/10556479/running-a-tkinter-form-in-a-separate-thread/10556698#10556698
#https://bugs.python.org/issue11077
#https://github.com/dojafoja/GUI-python-server/blob/master/server.py
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
#https://www.geeksforgeeks.org/python-gui-tkinter/
#https://stackoverflow.com/questions/9342757/tkinter-executing-functions-over-time
#https://stackoverflow.com/questions/9776718/how-do-i-stop-tkinter-after-function
#https://stackoverflow.com/questions/49432915/how-to-break-out-of-an-infinite-loop-with-a-tkinter-button
#https://stackoverflow.com/questions/49742217/python-socket-threading-tkinter-how-to-know-the-message-sender
###################################################################

