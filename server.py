import socket
import threading
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4321))


class NoDataException(Exception):
    """Raised when the message sent from client is of zero length"""
    pass


while True:
    msg = s.recvfrom(1024)
    print(msg)

    res = 0
    str_res = ""
    is_number = True
    op, fi, se = (" "," "," ")

    try:
        if len(msg) != 0:
            ans = msg[0]
        else:
            raise NoDataException

        op, fi, se = str(ans).split(' ')
    except NoDataException:
        is_number = False
        str_res = "Please send non-empty message"

    except ValueError:
        is_number = False
        str_res = "Please, send message in format *operand* *1st number* *2nd number*"

    if str(op)[2:] == '+':
        res = float(fi) + float(se[:-1])

    if str(op)[2:] == '-':
        res = float(fi) - float(se[:-1])

    if str(op)[2:] == '/':
        try:
            res = float(fi) / float(se[:-1])
        except ZeroDivisionError:
            is_number = False
            str_res = "You cannot divide by zero :)"

    if str(op)[2:] == '*':
        res = float(fi) * float(se[:-1])

    if str(op)[2:] == '<':
        str_res = str(float(fi) < float(se[:-1]))
        is_number = False

    if str(op)[2:] == '>=':
        str_res = str(float(fi) >= float(se[:-1]))
        is_number = False

    if str(op)[2:] == '<=':
        str_res = str(float(fi) <= float(se[:-1]))
        is_number = False

    if str(op)[2:] == '>':
        str_res = str(float(fi) > float(se[:-1]))
        is_number = False

    if is_number:
        str_res = str(res)
    else:
        is_number = False

    s.sendto(str_res.encode(), ("127.0.0.1", int(1234)))
