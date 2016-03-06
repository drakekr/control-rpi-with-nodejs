var express = require('express'), http = require('http');
var app = express(), server = http.createServer(app);

function run_cmd(cmd, args) {
  var spawn = require('child_process').spawn;
  var child = spawn(cmd, args);
}

app.get('/', function(req, res) {
  var page = "<!DOCTYPE html>\n"
  page += "<html lang='ko' class=''>\n"
  page += "<head>\n"
  page += "  <meta charset='utf-8'>\n";
  page += "  <title>CLCD Printer</title>\n";
  page += "</head>\n";
  page += "<body>\n";
  page += "  <form action='/print'>\n";
  page += "First Line: <input type='text' name='first'><br />\n";
  page += "Second Line: <input type='text' name='second'><br />\n";
  page += "<input type='submit' value='Print'>\n"
  page += "</body>"
  res.send(page);
});

app.get('/print', function(req, res) {
  run_cmd("python3", ["/home/pi/py3/write.py", req.query['first'] + "\n" + req.query['second'], "on"]);
  res.send("Check Your Character LCD");
});

server.listen(8000, function() {
  console.log("Express Server Listening on port " + server.address().port);
});
