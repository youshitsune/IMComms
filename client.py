import socket

target_host = "127.0.0.1"
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
while True:
    msg = input("Message: ")
    client.send(msg.encode('utf-8'))
    response = client.recv(4096)
    print(f"[*] Message: {response.decode('utf-8')}")

client.close()
