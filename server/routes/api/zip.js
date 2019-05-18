const express = require('express')

const router = express.Router()

// @route api/zip
// @desc For now test route
// @access Public
router.get('/', (req, res) => {
  res.send('Zip Works')
})

module.exports = router
