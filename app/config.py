from os import environ

HTTP_PROVIDER_URL = environ.get("HTTP_PROVIDER_URL")
WS_PROVIDER_URL = environ.get("WS_PROVIDER_URL")

ALLOWED_ORIGIN_SUFFIXES = ('localhost', 'bitox.io', 'www.bitox.io', 'backend.bitox.io')
ED_CONTRACT_ADDR = '0xb5adb233f28c86cef693451b67e1f2d41da97d21'
with open('bitox.abi.json') as f:
    import json
    ED_CONTRACT_ABI = json.load(f)
ED_WS_SERVERS = [
  "ws://backend.bitox.io:8080/socket.io/?EIO=3&transport=websocket",
]

POSTGRES_HOST = "postgres"
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")

FRONTEND_CONFIG_FILE="https://www.bitox.io/config/main.json"
