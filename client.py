import socket

# client program

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 1234))
print("\nCalculator App. Type '\quit' to exit. "
      "Send equation in format *operand* *1st number* *2nd number*")
while True:

    m = input("Enter equation to solve: ")
    res = s.sendto(m.encode(), ("127.0.0.1", 4321))



    ret = s.recvfrom(1024)
    output = str(ret[0])[2:-1]

    if output[len(output) - 1] == '0' and output[len(output) - 2] == '.':
        output = output[:-2]
    print("Answer: " + output)

