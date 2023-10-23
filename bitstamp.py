
import json
import ssl
import websocket

def vender():
    pass

def comprar():
    pass

def on_open(ws):
    print("Conexão aberta")

    y = {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
    x = json.dumps(y)

    ws.send(x)

    


def on_message(ws, message):
    message = json.loads(message)
    price = message["data"]["price"]
    print(price)

    if price > 29000:
        vender()
    if price < 28100:
        comprar()
def on_error(ws, error):
    print(f"Erro: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Conexão fechada com código {close_status_code}: {close_msg}")




if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(sslopt={"cert_regs": ssl.CERT_NONE})