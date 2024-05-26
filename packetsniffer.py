import socket
import struct
import textwrap



def main():
    connection = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.ntohs(3))
    while True:
        raw_data,addr = connection.recvfrom(65536)
        dest_mac,src_mac,ether_type,data = unpack_ethernet(raw_data)
        print('\n Ethernet Frame:')
        print('Destination: {} ,Source: {},Protocol: {}'.format(dest_mac,src_mac,ether_type))
def unpack_ethernet(data):
    dest_mac,src_mac,ether_type = struct.unpack('! 6s 6s H',data[:14])
    return get_mcadress(dest_mac),get_mcadress(src_mac),socket.htons(ether_type),data[:14]

def get_mcadress(bytes_adress):
    bytes_str = map('{:02x}'.format,bytes_adress)
    return ':'.join(bytes_str).upper()


if __name__ == '__main__':
    main()