const express = require('express');
const { runScript } = require('../../helper');
const router = express.Router();

// @route api/compile
// @desc For now test route
// @access Public
router.get('/', (req, res) => {
	const subprocess = runScript();
	subprocess.stdout.on('data', data => {
		console.log(data.toString());
	});
	subprocess.stderr.on('data', data => {
		console.log(data.toString());
	});
	res.send('Compiled files succesfully ...');
});

module.exports = router;
