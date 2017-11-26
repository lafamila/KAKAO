from flask import Flask, request, session
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def main():
    return "Hello, World!"

# #send message��� �̸����� ������ emit�ߴٸ� �װ� �޾Ƽ� �Ʒ��� �Լ��� �����ϰڴ�
# @socketio.on('send message')
# def handle_sent_message(data):  #�Ű����� data�� �Ѱܹ��� �ڷ��̴�. �� Ÿ���� json���� �����ϰ� �ؾ���
#     print(data.get("message"))
#     print("done")
#     emit("received message", {"message" : "you : "+data.get("message")}, room=session["room"])  #received message��� �̸����� ���� json������Ʈ�� ������. ���� �̰� ���̽� dictionary Ÿ���̴�.
#     #�� ���·δ� json array�� �� ������.
#     print("emit room number :" + data.get("room"))
#
# @socketio.on('join')
# def join(data):  #�Ű����� data�� �Ѱܹ��� �ڷ��̴�. �� Ÿ���� json���� �����ϰ� �ؾ���
#     room = data.get("room")
#     session["room"] = room
#     print(room)


if __name__ == '__main__':
    socketio.run(app)