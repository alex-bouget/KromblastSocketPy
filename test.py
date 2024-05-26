from kb_socket import DefaultKbSocket
from time import sleep

socket = DefaultKbSocket("127.0.0.1", 9434, "sync")
print(socket.execute("document.write('Hello, World!')"))
socket.navigate("https://www.google.com")

sleep(5)
socket.stop()
