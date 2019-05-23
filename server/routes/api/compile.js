const express = require('express')

const router = express.Router()

const { authenticated } = require('../../helpers/authentication')

// @route api/compile
// @desc For now test route
// @access Public
router.get('/', authenticated, (req, res) => {
  const { spawnSync } = require('child_process')
  const pythonScript = spawnSync('python3', ['tc_generator/tc_gen.py', '4'])

  if (pythonScript.status === 0) {
    // no error, so exit code is 0
    pythonScript.stdout.toString('utf8') // .stdout is generally  a binary buffer
  } else {
    console.log(pythonScript.stderr.toString('utf-8'))
  }
  res.redirect('/api/zip')
})
module.exports = router
