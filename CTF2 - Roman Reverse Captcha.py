#CTF 2 Roman Reverse Captcha (stages 1 - 3)
#created by Dustin Mobley for Cyber 210

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

    #flag 2 - works %80 of the time, all the time
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
    messages = []
    while True:
        data = sock.recv(1024).decode()
        
        if not data:
            break
        else:
            print(data)
            if data.startswith('#'):
                continue
            else:
                messages.append(data)
                #\n signals end of message
                if '\n' in data:
                    messages_string = ','.join(messages)
                    #print(f'heres the messages_string: {messages_string}')

                    #fish out integers and plus operator
                    ints = re.findall('[0123456789+]',messages_string)

                    #create solution
                    clean_equation = ','.join(ints)
                    cleaner_equation = clean_equation.replace(',','')
                    equation_list = cleaner_equation.split('+')
                    solution = int(equation_list[0]) + int(equation_list[1])

                    #print(f'heres the solution: {solution}')
                    #print(f'My response: {solution}')

                    #send solution
                    sock.sendall((f'{solution}\n').encode())
                    #clear messages for next challenge
                    messages = []
    

if __name__=="__main__":
    main()
