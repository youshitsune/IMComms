import threading
import socket
import rsa
import os

if os.path.exists("private_key.pem") and os.path.exists("public_key.pem"):
    pub_key = rsa.PublicKey.load_pkcs1(open("public_key.pem", "rb").read())
    priv_key = rsa.PrivateKey.load_pkcs1(open("private_key.pem", "rb").read())

else:
    pub_key, priv_key = rsa.newkeys(4096)
pub_con = None

target_host = "127.0.0.1"
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(pub_key.save_pkcs1("PEM"))
pub_con = rsa.PublicKey.load_pkcs1(client.recv(4096))

def send_msg(client):
    while True:
        msg = input("You: ")
        client.send(rsa.encrypt(msg.encode("utf-8"), pub_con))

def recv_msg(client):
    while True:
        print(f"Contact: {rsa.decrypt(client.recv(4096), priv_key).decode('utf-8')}")

threading.Thread(target=send_msg, args=(client,)).start()
threading.Thread(target=recv_msg, args=(client, )).start()

