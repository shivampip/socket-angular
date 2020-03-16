import socketio

sio = socketio.Client()


@sio.on("connect")
def connect():
    print("I'm Connected")
    sio.emit("session_request", {"session_id": "shivampip"})


@sio.on("disconnect")
def disconnect():
    print("I'm Disconnected")


@sio.on("session_confirm")
def session_confirmed(data):
    print("Session is confirmed")


@sio.on("response")
def response(data):
    print("Bot:- "+str(data))


sio.connect("http://153.92.4.175:5005/socket.io/")

while(True):
    msg = input("You:- ")
    sio.emit("message", {
        "sender_id": "shivampip",
        "session_id": "shivampip",
        "message": msg
    })
