import logging
from chat import chat
from chat import utils
from log import server_log
from select import select

logger = logging.getLogger('chat.server')


def mainloop():
    waiting_counter = 0
    clients = []
    clients_info = {}

    logger.debug('App started')

    parser = chat.create_parser()
    namespace = parser.parse_args()

    sock = chat.get_server_socket(namespace.addr, namespace.port)
    server_addr = sock.getsockname()
    start_info = f'Server started at {server_addr[0]}:{server_addr[1]}'
    print(start_info)
    logger.info(start_info)

    while True:
        messages = []

        try:
            client, client_addr = sock.accept()
        except OSError as e:
            pass
        else:
            info = f'Client connected from {client_addr[0]}:{client_addr[1]}'
            print(info)
            logger.info(info)
            client_info = {'name': '', 'addr': client_addr, 'in_messages': []}
            clients.append(client)
            clients_info[client] = client_info
        finally:
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], 0)
            except Exception as e:
                pass

            for s_client in r:
                try:
                    data_in = chat.get_data(s_client)
                except ConnectionResetError as e:
                    logger.error(e)

                if clients_info[s_client]['name'] == '':
                    if data_in['action'] == 'presence' and data_in['user']['account_name'] != '':
                        clients_info[s_client]['name'] = data_in['user']['account_name']
                        utils.RESPONSE['response'], utils.RESPONSE['alert'] = utils.SERVER_RESP[0]
                        print(f'{data_in["time"]} - {data_in["user"]["account_name"]}: {data_in["user"]["status"]}')
                    else:
                        utils.RESPONSE['response'], utils.RESPONSE['alert'] = utils.SERVER_RESP[1]

                if clients_info[s_client]['name'] != '' and data_in['action'] == 'msg':
                    data_in['from'] = clients_info[s_client]["name"]
                    print(f'{data_in["time"]} - {data_in["from"]}: {data_in["message"]}')
                    utils.RESPONSE['response'], utils.RESPONSE['alert'] = utils.SERVER_RESP[0]

                    messages.append(data_in)

                    if data_in["message"] == 'exit':
                        utils.RESPONSE['response'], utils.RESPONSE['alert'] = utils.SERVER_RESP[2]

                clients_info[s_client]['data_out'] = utils.RESPONSE

            for s_client in clients:
                clients_info[s_client]['in_messages'].extend(messages)

            for s_client in w:
                if 'data_out' in clients_info[s_client]:
                    data_out = clients_info[s_client]['data_out']
                    data_out['messages'] = clients_info[s_client]['in_messages']

                    try:
                        chat.send_data(s_client, data_out)
                        clients_info[s_client].pop('data_out')
                        clients_info[s_client]['in_messages'].clear()
                    except ConnectionResetError as e:
                        logger.error(e)
                        clients.remove(s_client)
                        clients_info.pop(s_client)

                    if data_out['response'] != '200':
                        clients.remove(s_client)
                        clients_info.pop(s_client)

        if len(clients) == 0:
            waiting_counter += 1

        if waiting_counter > 1200:
            break

    sock.close()

    logger.debug('App ending')


if __name__ == '__main__':
    mainloop()