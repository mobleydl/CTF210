import socket
import re

def main():
    hostname = 'cyber210.network'
    port = 8002

    
    #AF_INET for internet address, SOCK_STREAM for TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    
    #get initial message from robot army
    response = sock.recv(1024).decode()
    print(response)
    
    #flag 1
    message = (f'16\n65536\n4194304\n').encode()
    sock.sendall(message)

    #flag 2
    num = range(6)
    for num in num:
        data = sock.recv(1024).decode()
        print(data)

    num_list = re.findall('[0-9]+\S',data)
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
    
    #flag 3
    num_list2 = []

    while True:
        data = sock.recv(1024).decode()
        num_list2.append(data)
        if data:
            print(data)
            #server outputs FIN flag once this is wrapped up, so else statement doesn't matter
        else:
            edit_list = num_list2.pop(0)
            cat_list = ' '.join(num_list2)
            comb = re.findall('[0-9+]',cat_list)
            print(comb)
            combined_comb = ' '.join(comb)
            split = combined_comb.split('+')

            x = split[0]
            x = x.replace(" ","")
            y = split[1]
            y = y.replace(" ","")

            combined = int(x) + int(y)
            comb_ready = (f'{combined}\n').encode()
            print(f'this is combined {comb_ready}')
            sock.send(comb_ready)

            #no response received
            response2 = sock.recv(1024).decode()
            print(response2)
            break  


    

if __name__=="__main__":
    main()
