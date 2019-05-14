const express = require('express');

const router = express.Router();

const { authenticated } = require('../../helpers/authentication');

// @route api/generate
// @desc For now test route
// @access Public
router.get('/', authenticated, (req, res) => {
	res.send('Generate Works');
});

module.exports = router;
