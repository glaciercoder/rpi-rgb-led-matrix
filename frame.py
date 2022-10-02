from dis import dis
from re import A
import socket

class Frame:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = '' 

    def update_data(self, angles, distances):
        for angle, distance in zip(angles, distances):
            self.data += 'd{} {}'.format(angle, distance)

    def send_data(self):
        self.sock.sendto(self.data.encode(), ('127.0.0.1', 5005))

    def recv_data(self):
        self.sock.bind(('127.0.0.1', 5005))
        self.data, server_address= self.sock.recvfrom(2048)
        data = self.data.decode().split('d')
        angles = []
        distances = []
        data = data[1:]
        for e in data:
            angle, distance = e.split(' ')
            angles.append(float(angle))
            distances.append((distance))
        return angles, distances