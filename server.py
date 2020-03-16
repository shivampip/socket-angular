from aiohttp import web
import socketio
import json

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()


# @cross_origin(app)
sio.attach(app)


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.on("connect")
def client_connect(sid, data):
    print("New client connected")
    print("Socket ID: "+sid)


@sio.on("disconnect")
def client_disconnect(sid):
    print("Client disconnected")
    print("Socket ID: "+sid)


@sio.on('message')
async def print_message(sid, message):
    msg = message['data']
    print("User:- "+msg)
    await sio.emit("response", {'data': msg.upper()})

# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)
