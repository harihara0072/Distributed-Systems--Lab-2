# Importing the libraries that are used

import socket
from threading import Thread
from tkinter import *
import time
import queue
import threading


#Creating the global variables
host = ''
port = 80
post = "POST /"
http = "HTTP/1.1 \n"
host_name = "Host:" + str(host) +"\n"
user_agent = "User-Agent: Python/3.6 + \n"
content_type = "text/html \n"

#Creating a queue to append the random numbers sent by the clients
q = queue.Queue()

#creating the lock to lock the shared memory so that only on client uses
lock = threading.Lock()
print_lock = threading.Lock()

#Creating the socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((host, port))

#making the server waiting for the clients
skt.listen(5)

#Creating the Tkinter GUI window
display = Tk()
display.title("Server")
display.geometry("500x500")
text = Text(display, height=30, width=60)

#printing that the server is waiting for clients
text.insert(INSERT, "Waiting for connections")

global count
count = 0


#The method used to make all the client threads wait and returns true only to the client that has sent the number
def wait_threads():
    global t
    lock.acquire()
    k = q.get()
    t = int(k)
    lock.release()
    time.sleep(k)
    return True


#Method used to print messages on the GUI provided by the client threads
def print_message(mess):
    print_lock.acquire()
    text.insert(INSERT, "\n" + mess)
    print_lock.release()

#The method which is used to run multi threaded clients. This will be the targer method for each client thread
def client_thread(client, c_ip, c_skt):
    try:
        global t
        get_username_str = "GET /Username HTTP/1.1 \n Host: 127.0.0.1 " + "\n UserAgent: Python/3.6"
        print(get_username_str)

        #requesting the client to send its username
        client.send(bytes(get_username_str, 'utf-8'))

        #receiving the response from the client
        username_header_bytes = client.recv(1024)
        username_header = username_header_bytes.decode('utf-8')
        print(username_header)

        #receiving the username from the client
        username_bytes = client.recv(1024)
        username = username_bytes.decode('utf-8')
        print(username)


        #Displaying that the server is connected to the client
        print("Connected to client: " + username)
        text.insert(INSERT, "\n Connected to client: " + username)

        #server keeps on receiving the random numbers from the client
        while True:
            rand_number_header_bytes = client.recv(1024)
            rand_number_header = rand_number_header_bytes.decode('utf-8')
            print("this is received" + rand_number_header)
            rand_after_post = rand_number_header.split('POST /')[1]
            random_number = rand_after_post.split('HTTP/1.1')[0]
            print(random_number)

            #Checking if the user clicked the exit button on the client GUI
            if random_number == "quit":
                client.close()
                break
            else:
                q.put(int(random_number))
                res = wait_threads()
                if (res == True):
                    time.sleep(t)
                    str1 = "Server waited for " + random_number + " sec for client " + username
                    print_message(str1)
                    response_header = post + str1 + http + host_name + user_agent + content_type + "Content-length: " + str(
                        len(bytes(str1, 'utf-8'))) + "\n"
                    print(response_header)
                    client.send(bytes(response_header, 'utf-8'))
    except:
        print("Server is closed")


#This is the Main method which will accept the clients and create threads
def main():
    global count
    print("Waiting for Connection")
    try:
        while True:
            client, (client_ip, client_socket) = skt.accept()
            t = Thread(target=client_thread, args=(client, client_ip, client_socket))
            t.start()
    except:
        print("Server is stopped")


#This method will be called once the exit button on the server is clicked
def close_connection():
    skt.close()
    display.quit()

#Creating the exit button on the server
button = Button(display, text="exit", command=close_connection)

def initial():
    text.pack()
    button.pack()
    th = Thread(target=main)
    th.start()
    display.mainloop()

if __name__ == '__main__':
    initial()




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
