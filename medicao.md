Nos meus testes locais, o protocolo TCP (19.9 ms) foi mais rápido que o UDP (45.8 ms).
Teoricamente, o UDP é mais veloz por não ter a sobrecarga de garantir a entrega ou a ordem dos pacotes.
No entanto, o TCP levou vantagem neste cenário específico devido à forma como a comunicação ocorreu no script.
O TCP precisou estabelecer a conexão (handshake) apenas uma vez, reutilizando esse canal aberto para as 100 mensagens.
Já o UDP precisou processar o endereço de destino e empacotar cada pacote individualmente (via `sendto`) 100 vezes seguidas.