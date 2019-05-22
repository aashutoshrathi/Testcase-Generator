
const express = require('express');

const router = express.Router();
const { authenticated } = require('../../helpers/authentication');
// @route api/zip
// @desc For now test route
// @access Public

router.get('/', authenticated, (req, res) => {
	var path = './test-cases.zip';
	res.writeHead(200, { 'content-type': 'application/zip' });
	var filestream = fs.createReadStream(path);
	filestream.on('error', function(error) {
		console.log(error);
	});
	filestream.pipe(res);
});

module.exports = router
