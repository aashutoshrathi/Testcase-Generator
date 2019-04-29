const { spawn } = require('child_process');
const path = require('path');

module.exports = {
	runScript: function runScript() {
		console.log(path.join(__dirname, '../tc_generator/tc_gen.py'));
		return spawn('python3', [path.join(__dirname, '../tc_generator/tc_gen.py'), '4']);
	}
};
