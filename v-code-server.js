const fs = require("fs");
const express = require("express");
const cors = require("cors");
const { json } = require("express");

const app = express();
const port = 3000;
const host = "0.0.0.0";

var array;
var p_out = "";

app.use(function (req, res, next) {
  const allowedOrigins = ["http://127.0.0.1:5173"];
  const origin = req.headers.origin;

  if (allowedOrigins.includes(origin)) {
    res.setHeader("Access-Control-Allow-Origin", origin);
  }
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept, Authorization"
  );
  res.header("Access-Control-Allow-Credentials", true);
  res.header(
    "Access-Control-Allow-Methods",
    "GET,DELETE, UPDATE,POST,PUT"
  );

  next();
});

app.use(json());

app.get("/", (req, res) => {
  fs.readFile("Problems.txt", function (err, data) {
    if (err) throw err;
    array = data.toString().split("\n");
  });
  res.send(array);
});

app.post("/", function (req, res) {
  fs.writeFileSync("/tmp/Code.py", "");
  fs.writeFileSync("/tmp/Code.py", req.body.code);

  const { spawn } = require("child_process");

  var process_1 = spawn("python", ["Code.py"]);
  process_1.stdout.on("data", function (data) {
    p_out = data.toString();
  });

  process_1.stderr.on("data", function (data) {
    try {
      res.json({ error: data.toString() });
      process_1.exitCode = 0;
    } catch (error) {}
  });

  var process_2 = spawn("python", ["Add_lines.py"]);
  process_2.stdout.on("data", function (data) {
    try {
      fs.writeFileSync("/tmp/Code.py", "");
      fs.writeFileSync("/tmp/Code.py", data.toString());
      var process_3 = spawn("python", ["Code.py"]);
      process_3.stdout.on("data", function (data) {
        res.json({ result: data.toString(), out: p_out });
        process_3.exitCode = 0;
      });
    } catch (error) {}
  });
});

app.listen(port, host ,(error) => {
  if (!error)
    console.log(
      "Server is Successfully Running, and App is listening on port " + port
    );
  else console.log("Error occurred, server can't start", error);
});
