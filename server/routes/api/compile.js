<<<<<<< HEAD
const express = require("express");

=======
const express = require('express');
const { runScript } = require('../../helper');
>>>>>>> a1904480f60750b0802a5e66bff12a214f68857a
const router = express.Router();

// @route api/compile
// @desc For now test route
// @access Public
<<<<<<< HEAD
router.get("/", (req, res) => {
  res.send("Compile Works");
=======
router.get('/', (req, res) => {
	const subprocess = runScript();
	subprocess.stdout.on('data', data => {
		console.log(data.toString());
	});
	subprocess.stderr.on('data', data => {
		console.log(data.toString());
	});
	res.send('Compiled files succesfully ...');
>>>>>>> a1904480f60750b0802a5e66bff12a214f68857a
});

module.exports = router;
