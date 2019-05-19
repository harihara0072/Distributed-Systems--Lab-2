# Distributed-Systems--Lab-2

### Language used : 
Python 3.7 

### Libraries used: 
Tkinter
Threading 
Socket 


### Server.py 
1. Created a socket in the server by giving the host name and port number 
2. Server will be continuously listening for the clients 
3. Once a client is connected then the server sends a HTTP GET request to the client asking for the username 
4. Once we get the response from the client then it will create a new thread. 
5. The server will receive the random integer from the client 
6. Then the server will insert those random integers into the queue.
6. Server will then pop the elements from the queue and it will make all the client handling threads to wait for the time that is equal to the number that is popped from the queue and respond to the client that has sent that number saying that the server has stopped for the time it has specified. 
7. Sever will keep on doing this until client stops sending the number. 

### Client.py: 
1. The client will connect to the server socket by using server hostname and port number. 
2. Then the client will receive the HTTP GET request for the username and client will respond to it. 
3. Then a random integer between 3 and 10 will be generated and send it to client using HTTP POST method. 
4. The client will wait for the server to respond and once it receives the response then it will print the response from the server along with the time that it has waited for the server to respond.
5. Client will keep doing this until the user clicks the exit button.

### Code running structure: 
python server.py 
python client.py(3 times for 3 clients) 
