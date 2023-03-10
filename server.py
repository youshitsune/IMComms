import socket

IP = "0.0.0.0"
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")
    client, address = server.accept()
    while True:
        request = client.recv(4096)
        print(f"[*] Message: {request.decode('utf-8')}")
        client.send(input().encode("utf-8"))
        client.send(b"ACK")

if __name__ == "__main__":
    main()
    
