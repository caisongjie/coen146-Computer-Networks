
import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  port = int(sys.argv[1])
except (IndexError, ValueError):
  usage()




def decrypt(ciphertext, key):
  # pretend this function is already implemented
  return ciphertext




def secure_recv(udp_socket, chunk_size):
  (data, addr) = udp_socket.recvfrom(chunk_size)

  # add pseudocode here
  # feel free to modify the parameters of the function if need be

  #wait for the public key A from the source
  #generate private key b
  #compute public key B using B = p ** b % g
  #send public key B
  #compute shared key using K = A**b
  #wait for the encrypted message
  #decrypt the message using shared key
  return (data, addr)





def listen(port, chunk_size=1024):
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp_socket.bind( ("", port) )

  term_string = "quit"
  terminated = False

  while not terminated:
    (data, addr) = secure_recv(udp_socket, chunk_size)
    msg = data.decode().strip()
    ip = addr[0]
    port = addr[1]
    if msg == "quit":
      terminated = True
    else:
      sys.stdout.write("{}: {}\n".format(ip, msg))

  udp_socket.close()


if __name__ == "__main__":
  listen(port)



