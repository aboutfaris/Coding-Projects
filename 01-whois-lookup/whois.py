# Simple WHOIS query/response client. First step in reconnaissance.
import socket

def whois_lookup(domain: str):
  # AF_INET: IPv4 address family. SOCK_STREAM: TCP socket type.
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("whois.iana.org", 43))  # IANA's WHOIS server, port 43
  s.send(f"{domain}\r\n".encode())
  response = s.recv(4096).decode()  # read the WHOIS server's response
  s.close()
  return response

print(whois_lookup("example.com"))
