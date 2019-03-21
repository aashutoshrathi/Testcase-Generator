const express = require("express");

const router = express.Router();

// @route api/compile
// @desc For now test route
// @access Public
router.get("/", (req, res) => {
  res.send("Compile Works");
});

module.exports = router;
