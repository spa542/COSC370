# import the socket module
import socket
import sys # In order to terminate the program

"""
Fill in code to create a TCP server socket, assign a port number,
bind the socket to server address and server port,
and listen to at most one connection at a time.
"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 6666))
server_socket.listen(1)

# Server should be up and running listening to the incoming connections
while True:
    print('Ready to serve...')

    """
    Fill in code to set up a new connection from the client.
    """
    connection, address = server_socket.accept()
    print(f'New connection from {address}')
    print('Client accepted...')

    try:
        """
        Fill in code to receive a request message from the client.
        """
        data = connection.recv(6666).decode()
        print('Received data from port 6666...');

        # Extract the path ( which is the second part of HTTP header)
        # of the requested object from the message .
        # assuming message holds the data from the previous line (s) of code
        file_name = data.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '\ ' , we read the path from the second character
        fh = open(file_name[1:])

        # Store the entire content of the requested file in a temporary buffer
        output_data = fh.read()

        """
        Fill in code to send the the HTTP response header line
        ("HTTP/1.1 200 OK \r\n\r\n") to the connection socket.
        """
        connection.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        print('Sent response headers...')

        # Send the content of the requested file to the client
        # Assuming connectionSocket has been created above
        for i in range(0, len(output_data)):
            connection.send(output_data[i].encode())
        connection.send("\r\n".encode())
        print('Sent body...')
        connection.close()
        print('[!] Connection closed');

    except IOError:
        """
        Fill in code to send response message for file not found
        (use "HTTP/1.1 404 Not Found \r\n\r\n"),
        and send 404 Not Found as HTML body.
        Fill in code to close client connection socket.
        """
        connection.send('HTTP/1.1 404 Not Found \r\n\r\n'.encode())
        connection.close()

"""
Fill in code to close server socket .
"""
server_socket.close()
sys.exit() # Terminate the program after sending the corresponding data
