import socket

def scan_ports(ip, start_port=1, end_port=1024):
    open_ports = []
    print(f"Iniciando a varredura de portas em {ip} (Portas {start_port}-{end_port})")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  
        
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Porta {port} aberta")
            open_ports.append(port)
        sock.close()
    
    if open_ports:
        print("\nPortas abertas:")
        for port in open_ports:
            print(f"- Porta {port}")
    else:
        print("Nenhuma porta aberta encontrada no intervalo especificado.")
        
    return open_ports

if __name__ == "__main__":
    ip = input("Digite o endereço IP que deseja escanear: ")
    start_port = int(input("Digite a porta inicial (ex: 1): "))
    end_port = int(input("Digite a porta final (ex: 1024): "))
    
    scan_ports(ip, start_port, end_port)
