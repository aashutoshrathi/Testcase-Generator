const express = require('express');
const mongoose = require('mongoose');

const compile = require('./routes/api/compile');
const zip = require('./routes/api/zip');
const generate = require('./routes/api/generate');
const upload = require('express-fileupload');
const app = express();

//Database config goes here

//Database connection goes here
app.use(upload());
app.get('/', (req, res) => {
	res.send('Hello World');
});
app.get('/fileupload', function(req, res) {
	console.log(__dirname);
	res.sendFile(__dirname + '/index.html');
});
app.post('/upload', function(req, res) {
	console.log(req.files);
	var file = req.files.upfile;
	if (file) {
		var filename = file.name;
		var uploadpath = __dirname + '/uploads/' + filename;
		file.mv(uploadpath, function(err) {
			if (err) {
				console.log('file upload Failed', filename, err);
				res.send('Error Occured!');
			} else {
				console.log('File Uploaded', filename);
				return res.redirect('/api/compile');
			}
		});
	} else {
		res.send('Sorry please select the file to upload');
	}
});

//Compile, generate and zip routes
app.use('/api/compile', compile);
app.use('/api/zip', zip);
app.use('/api/generate', generate);

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server running on port ${port}`));
