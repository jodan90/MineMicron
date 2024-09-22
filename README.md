```markdown
# 마인크래프트 서버 자동화 (mcrcon 사용)

이 프로젝트는 `mcrcon` 라이브러리를 사용하여 마인크래프트 서버를 원격으로 자동화하는 방법을 설명합니다. RCON을 통해 서버에 명령어를 전송할 수 있습니다.

## 요구 사항

- Python 3.x
- `mcrcon` 라이브러리 설치:

```bash
pip install mcrcon
```

## 설정 방법

1. `server.properties` 파일을 열고 아래와 같이 RCON을 활성화하세요:

   ```
   enable-rcon=true
   rcon.port=25575  # 기본 포트
   rcon.password=your_password_here  # RCON 비밀번호 설정
   ```

2. 서버를 저장하고 재시작합니다.

## 코드 사용법

```python
import mcrcon

# RCON 서버 설정
rcon_host = '127.0.0.1'  # 서버 IP
rcon_port = 25575  # RCON 포트 (기본: 25575)
rcon_password = 'your_password_here'  # RCON 비밀번호

# RCON 명령어 전송 함수
def send_rcon_command(command):
    try:
        with mcrcon.MCRcon(rcon_host, rcon_password, rcon_port) as rcon:
            response = rcon.command(command)
            print(f"서버 응답: {response}")
            return response
    except Exception as e:
        print(f"RCON 연결 실패: {e}")

# 명령어 예시
send_rcon_command("time set day")  # 시간 변경
send_rcon_command("weather clear")  # 날씨 변경
```

이 코드를 사용하면 RCON을 통해 마인크래프트 서버에 명령어를 보내 자동화할 수 있습니다. RCON 호스트, 포트, 비밀번호를 자신의 서버 설정에 맞게 변경하면 됩니다.

## 실행 방법

Python 스크립트를 다음 명령어로 실행합니다:

```bash
python minecraft_automation.py
```

스크립트 실행 후 서버에 연결되어 설정된 명령어가 실행됩니다.

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)로 공개되어 있습니다.
```
