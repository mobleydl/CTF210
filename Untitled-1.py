import socket

def main():
    hostname = 'cyber210.network'
    port = 8001

    def netcat(hostname, port):
        #AF_INET for internet address, SOCK_STREAM for TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hostname, port))
        
        #get initial weather report
        response = sock.recv(1024)
        print(response)
        
        #send secret message - \n at the end is required
        secret = b'But not at St. Moritz\n'
        print(secret)
        sock.sendall(secret)

        #receive flag and clean it up a bit
        response2 = sock.recv(1024)
        str_resp2 = response2.decode()
        str_resp2.strip('\n')

        print(f'Flag: {str_resp2}')

    netcat(hostname, port)

if __name__=="__main__":
    main()