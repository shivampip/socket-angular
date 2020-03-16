import { Component, OnInit } from "@angular/core";
import { HiSocketService } from "./hi-socket.service";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent implements OnInit {
  title = "angu";

  constructor(private webSocket: HiSocketService) {}

  ngOnInit(): void {
    this.webSocket.listen("response").subscribe(data => {
      console.log("Response received");
      console.log(data);
    });
    this.webSocket.listen("connect").subscribe(data => {
      console.log("I am Connected to Socket server");
      this.webSocket.emit("message", { data: "Hello World" });
    });
  }
}
