import socket
import threading

# Dictionary to store client names and their corresponding sockets
clients = {}

welcom= """


██╗░░░░░░█████╗░██████╗░██╗██╗░░░░░  ░██████╗░░█████╗░██╗░░░██╗
██║░░░░░██╔══██╗██╔══██╗██║██║░░░░░  ██╔════╝░██╔══██╗╚██╗░██╔╝
██║░░░░░███████║██║░░██║██║██║░░░░░  ██║░░██╗░███████║░╚████╔╝░
██║░░░░░██╔══██║██║░░██║██║██║░░░░░  ██║░░╚██╗██╔══██║░░╚██╔╝░░
███████╗██║░░██║██████╔╝██║███████╗  ╚██████╔╝██║░░██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░



Press 1 to get chat history
"""


histor="\n"

def handle_client(client_socket):
    # Send a welcome message to the client
    global histor
    client_socket.send(welcom.encode("utf-8"))


    client_socket.send("Currently Online Users: \n".encode("utf-8"))
    for nam in clients.keys():
        client_socket.send(nam.encode("utf-8"))



    client_socket.send("\n Welcome to the chat! Please enter your name:".encode("utf-8"))
    client_name = client_socket.recv(1024).decode("utf-8")
    clients[client_name] = client_socket
    
    print(f"{client_name} connected.")

    while True:
        try:
            # Receive message from the client
            # client_socket.send(f"\n{client_name[:-1]} ==> ".encode("utf-8"))
            message = client_socket.recv(1024).decode("utf-8")
            
            
            if(message[:-1]=="1"):
                client_socket.send(f"\n:::::::::::::::HISTORY ::::::::::::::\n  {histor} \n\n".encode("utf-8"))
            
            else : 
                histor+= f"{client_name[:-1]} ==> {message}"
                
            
            if not message:
                break

            # Broadcast the message to all other clients
            for name, socket in clients.items():
                if socket != client_socket:
                    socket.send(f"{client_name[:-1]} ==> {message}".encode("utf-8"))

        except Exception as e:
            print(f"Error handling client {client_name}: {e}")
            break

    # Remove the client from the dictionary
    del clients[client_name]
    client_socket.close()
    print(f"{client_name} disconnected.")

def main():
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
