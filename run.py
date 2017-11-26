from flask import Flask, request, session
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def main():
    return "Hello, World!"

# #send message라는 이름으로 나한테 emit했다면 그걸 받아서 아래의 함수를 실행하겠다
# @socketio.on('send message')
# def handle_sent_message(data):  #매개변수 data가 넘겨받은 자료이다. 이 타입은 json으로 가정하고 해야함
#     print(data.get("message"))
#     print("done")
#     emit("received message", {"message" : "you : "+data.get("message")}, room=session["room"])  #received message라는 이름으로 뒤의 json오브젝트를 보낸다. 현재 이건 파이썬 dictionary 타입이다.
#     #이 상태로는 json array를 못 보낸다.
#     print("emit room number :" + data.get("room"))
#
# @socketio.on('join')
# def join(data):  #매개변수 data가 넘겨받은 자료이다. 이 타입은 json으로 가정하고 해야함
#     room = data.get("room")
#     session["room"] = room
#     print(room)


if __name__ == '__main__':
    socketio.run(app)