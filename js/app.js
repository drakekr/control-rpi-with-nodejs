var http = require('http');
var server = http.createServer(function (request, response) {
  var date = new Date();
  var utcdate = date.toUTCString();
  var krdate = date.toLocaleString();

  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("Now UTC Time is " + utcdate + "\n");
  response.write("Now Local Time is "+ krdate + "\n");
  response.end("Hello from nodejs running on Rasbian!\n");
});
server.listen(80);
console.log("Server running at http://127.0.0.1:80/");
