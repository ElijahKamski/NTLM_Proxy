import socket
from threading import Thread
from ntlm_auth.ntlm import NtlmContext
from urllib.parse import urlparse

def handle_client(client_socket):
    request_data = client_socket.recv(4096)
    if not request_data:
        client_socket.close()
        return

    request_data_str = request_data.decode('utf-8')
    first_line = request_data_str.split('\r\n')[0]
    target_url = first_line.split(' ')[1]

    target_parsed = urlparse(target_url)
    target_host = target_parsed.hostname
    target_port = target_parsed.port if target_parsed.port else 80

    ntlm_context = NtlmContext("some", "admin", "pass")
    print("I'm going in proxy authorization")

    if 'Proxy-Authorization: NTLM' not in request_data_str:
        response = "HTTP/1.1 407 Proxy Authentication Required\r\nProxy-Authenticate: NTLM\r\n\r\n"
        client_socket.sendall(response.encode())
        client_socket.close()
        return

    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.connect((target_host, target_port))

    while True:
        if 'Proxy-Authorization: NTLM' in request_data_str:
            print("I'm in proxy authorization")
            server_data = b''
            try:
                server_challenge, negotiate_flags = ntlm_context.parse_challenge_message(request_data)
                authenticate_message = ntlm_context.create_authenticate_message(server_challenge)
                print(authenticate_message)
                proxy_socket.sendall(authenticate_message)
                server_data = proxy_socket.recv(4096)
            except Exception as e:
                print(str(e))

            if server_data:
                client_socket.sendall(server_data)
                break

        proxy_socket.sendall(request_data)
        server_data = proxy_socket.recv(4096)
        if not server_data:
            break

        client_socket.sendall(server_data)
        request_data = client_socket.recv(4096)

    client_socket.close()
    proxy_socket.close()

def start_proxy_server():
    proxy_host = "127.0.0.1"  # Замените PROXY_HOST на адрес, на котором будет запущен прокси-сервер
    proxy_port = 1254  # Замените PROXY_PORT на порт, на котором будет запущен прокси-сервер

    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind((proxy_host, proxy_port))
    proxy_socket.listen(5)

    print(f"Proxy server is running on {proxy_host}:{proxy_port}")

    while True:
        client_socket, client_address = proxy_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        client_thread = Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_proxy_server()
