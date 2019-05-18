const express = require('express')

const router = express.Router()

// @route api/generate
// @desc For now test route
// @access Public
router.get('/', (req, res) => {
  res.send('Generate Works')
})

module.exports = router
