var app = require("express");
var server = require("http").Server(app);
var io = require("socket.io")(server);

io.on("connection", socket => {
	console.log("A user is connected");
	socket.emit("response", "This is test response which is successful");
});

server.listen(8080, () => {
	console.log("Socket.io server is running on 8080");
});
