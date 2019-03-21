const express = require("express");
const mongoose = require("mongoose");

const compile = require("./routes/api/compile");
const zip = require("./routes/api/zip");
const generate = require("./routes/api/generate");

const app = express();

//Database config goes here

//Database connection goes here

app.get("/", (req, res) => {
  res.send("Hello World");
});

//Compile, generate and zip routes
app.use("/api/compile", compile);
app.use("/api/zip", zip);
app.use("/api/generate", generate);

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server running on port ${port}`));
