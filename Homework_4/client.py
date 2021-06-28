import chat
import utils

if __name__ == '__main__':
    client_name = input('input name: ')

    parser = chat.create_parser()
    namespace = parser.parse_args()

    sock = chat.get_client_socket(namespace.addr, namespace.port)

    serv_addr = sock.getpeername()
    print(f'Connected to server: {serv_addr[0]}:{serv_addr[1]}')

    utils.PRESENCE['user']['account_name'] = client_name
    chat.send_data(sock, utils.PRESENCE)

    while True:
        data = chat.get_data(sock)

        if data['response'] != '200':
            break

        msg = input('Input "exit" for quite): ')
        utils.MESSAGE['message'] = msg
        chat.send_data(sock, utils.MESSAGE)

    sock.close()