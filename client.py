import socketio

sio = socketio.Client()


@sio.on("connect")
def connect():
    print("I'm Connected")


@sio.on("disconnect")
def disconnect():
    print("I'm Disconnected")


@sio.on("response")
def response(data):
    msg = data['data']
    print("Bot:- "+str(msg))


sio.connect("http://localhost:8080")

while(True):
    msg = input("You:- ")
    sio.emit("message", {"data": msg})
