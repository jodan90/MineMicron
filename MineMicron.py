import mcrcon

rcon_host = '127.0.0.1' 
rcon_port = 25575  
rcon_password = 'your_password_here'  

def send_rcon_command(command):
    try:
        with mcrcon.MCRcon(rcon_host, rcon_password, rcon_port) as rcon:
            response = rcon.command(command)
            print(f"서버 응답: {response}")
            return response
    except Exception as e:
        print(f"RCON 연결에 실패했습니다: {e}")

