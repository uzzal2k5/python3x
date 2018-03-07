import certifi
import socket
import ssl

s = ssl.wrap_socket(socket.socket(), server_side=1, certfile=certifi.where())
s.connect('172.17.0.4', 443)