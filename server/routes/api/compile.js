const express = require('express');

const router = express.Router();

// @route api/compile
// @desc For now test route
// @access Public
router.get('/', (req, res) => {
	const { spawnSync } = require('child_process');
	const pythonScript = spawnSync('python3', ['tc_generator/tc_gen.py', '4']);
	console.log(pythonScript.stderr.toString('utf-8'));
	if (0 == pythonScript.status) {
		// no error, so exit code is 0
		const pythonOutput = pythonScript.stdout.toString('utf8'); // .stdout is generally  a binary buffer
	}
	res.send('Compiling ...');
});

module.exports = router;
