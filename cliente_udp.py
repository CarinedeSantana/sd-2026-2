# cliente_udp.py — CASA da Aula 2: eco em UDP (cliente)
import socket

HOST, PORT = "127.0.0.1", 5001
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # SOCK_DGRAM = UDP
s.settimeout(5)                                        # UDP pode perder: use tempo-limite

mensagem = "oi via UDP"

try:
    # TODO 1: envie 'mensagem' (em bytes) para (HOST, PORT) com s.sendto(...)
    s.sendto(mensagem.encode('utf-8'), (HOST, PORT))
    print(f"[cliente] enviado: {mensagem}", flush=True)

    # TODO 2: receba a resposta com s.recvfrom(1024) e imprima o texto recebido
    dado, endereco = s.recvfrom(1024)
    print(f"[cliente] recebi de volta: {dado.decode('utf-8')} de {endereco}", flush=True)

except socket.timeout:
    print("[cliente] Tempo limite esgotado! O servidor demorou a responder ou o pacote se perdeu.")
finally:
    s.close()