// util = require("util");
const wasm = Module({ wasmBinaryFile: "http://localhost:8000/easywasm.wasm" });

function to_jstr(str, length) {
  var ptr = wasm.UTF8ToString(str, length);
  return ptr;
}

function to_cstr(str) {
  var ptr = wasm.allocate(
    wasm.intArrayFromString(str),
    "i8",
    wasm.ALLOC_NORMAL
  );
  return ptr;
}

wasm.onRuntimeInitialized = function() {
  var express = require("express");
  var bodyParser = require("body-parser");
  var app = express();
  app.use(bodyParser.urlencoded({ extended: false }));
  var hostName = "0.0.0.0";
  var port = 23333;

  app.all("*", function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
      "Access-Control-Allow-Headers",
      "Origin, X-Requested-With, Content-Type, Accept"
    );
    res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
    res.header("X-Powered-By", " 3.2.1");
    res.header("Content-Type", "application/json;charset=utf-8");
    next();
  });

  app.get("/registered", function(req, res) {
    var username = "";
    var introduction = "";
    var password = 0;
    for (var key in req.query) {
      if (key == "username") {
        username = req.query[key];
      }
      if (key == "introduction") {
        introduction = req.query[key];
      }
    }

    if (
      username.length > 0 &&
      username.length < 0x10 &&
      introduction.length > 0 &&
      introduction.length < 0x8c
    ) {
      password = Math.floor(Math.random() * 0xffffffff);
      wasm._registered(to_cstr(username), password, to_cstr(introduction));
      res.send("succeed.");
    } else {
      res.send("Invalid length!");
    }
  });

  app.get("/profile", function(req, res) {
    var profile = wasm._profile();
    res.send(to_jstr(profile, 0xb0));
  });

  app.get("/login", function(req, res) {
    var username = "";
    var password = 0;
    var result = "";

    for (var key in req.query) {
      if (key == "username") {
        username = req.query[key];
      }
      if (key == "password") {
        password = parseInt(req.query[key]);
      }
    }

    if (
      username.length > 0 &&
      username.length < 0x10 &&
      password <= 0xffffffff
    ) {
      var s = wasm._login(to_cstr(username), password);
      res.send(to_jstr(s, 0x10));
    } else {
      res.send("Invalid length");
    }
  });

  app.listen(port, hostName, function() {
    console.log(`server run at http://${hostName}:${port}`);
  });
};
