import socket
import re

def main():
    hostname = 'cyber210.network'
    port = 8002

    def netcat(hostname, port):
        #AF_INET for internet address, SOCK_STREAM for TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hostname, port))
        
        #get initial message from robot army
        response = sock.recv(1024)
        print(response)
        
        #send auth message (4 * 4\n256 * 256\n2048 * 2048\n)
        message = b'16\n65536\n4194304\n'
        
        print(f'{message}\n')
        sock.sendall(message)

        num = range(6)
        for num in num:
            data = sock.recv(1024)
            print(data)

        norm_data = data.decode()
        norm_data = norm_data.strip('\n')
        print(f'{norm_data}')
        num_list = re.findall('[0-9]+\S',norm_data)
        #print(num_list)

        int_num0 = int(num_list[0])
        int_num1 = int(num_list[1])
        sum_0_and_1 = int_num0 + int_num1
        #print(sum_0_and_1)

        int_num2 = int(num_list[2])
        int_num3 = int(num_list[3])
        sum_2_and_3 = int_num2 + int_num3
        #print(sum_2_and_3)

        int_num4 = int(num_list[4])
        int_num5 = int(num_list[5])
        sum_4_and_5 = int_num4 + int_num5
        #print(sum_4_and_5)

        re_auth = f'{sum_0_and_1}\n{sum_2_and_3}\n{sum_4_and_5}\n'
        #print(re_auth.encode())
        sock.sendall(re_auth.encode())

        #new_info = sock.recv(1024)
        #print(new_info)

        #re_auth = input(f'enter input')
        #encoded_re_auth = re_auth.encode()
        #sock.sendall(encoded_re_auth)

        #final_message = sock.recv(4094)
        #print(final_message)

        num = range(13)
        empty_list = []
        for num in num:
            data = sock.recv(1024)
            print(data)
            de_data = data.decode()
            empty_list.append(de_data.strip('\n'))

        print(empty_list)
        edit_list = empty_list.pop(0)
        cat_list = ' '.join(empty_list)
        comb = re.findall('[0-9+]',cat_list)
        combined_comb = ' '.join(comb)
        print(comb)
        print(combined_comb)

        #while True:
            #data = sock.recv(1024)
            #if (not data):
                
                #break
            #else:
                #print(data)
                #continue

        
            #receive flag
        #response2 = sock.recv(4096)
        #print(response2.decode())

        #response3 = sock.recv(4096)
        #print(response3.decode())

        #response4 = sock.recv(4096)
        #print(response4.decode())

            


    netcat(hostname, port)

if __name__=="__main__":
    main()
