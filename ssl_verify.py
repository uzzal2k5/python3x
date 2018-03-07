import socket, ssl, pprint

host = '172.17.0.4'
port = '443'


def socket_connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(sock,
                               ca_certs='/etc/ssl/ssl_certs/ssl_web.crt',
                               cert_reqs=ssl.CERT_REQUIRED
                               )
    ssl_sock.connect(host, port)
    print(repr(ssl_sock.getpeername()))
    pprint.pprint(ssl_sock.getpeercert())
    print(pprint.pformat(ssl_sock.getpeercert()))
    ssl_sock.write("""GET / HTTP/1.0\r
    Host: """+host+"""\r\n\r\n""")
    data =ssl_sock.read()
    ssl_sock.close()


socket_connect(host, port)

