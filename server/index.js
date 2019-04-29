const express = require('express');
const mongoose = require('mongoose');
const helmet = require('helmet');
const cors = require('cors');

const compile = require('./routes/api/compile');
const zip = require('./routes/api/zip');
const generate = require('./routes/api/generate');
const upload = require('express-fileupload');
const app = express();
var fs = require('fs');

//Database config goes here
const db = require('./config/keys').mongoURI;

//Database connection goes here
app.use(cors());
app.use(helmet());

mongoose
	.connect(db, { useNewUrlParser: true })
	.then(() => console.log('Database connected'))
	.catch(err => console.log(err));

app.use(upload());
app.use(express.static('public'));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
	res.render('pages/landing');
});

app.get('/upload-file', function(req, res) {
	res.render('pages/index');
});
app.post('/api/upload', function(req, res) {
	console.log(req.files);
	var file = req.files.upfile;
	if (file) {
		var filename = file.name;
		var timestamp = new Date().getTime();
		var uploadpath = __dirname + '/uploads/' + timestamp + '-' + filename;
		var dir = __dirname + '/uploads'; //added a check wheteher the directory exists or not
		if (!fs.existsSync(dir)) {
			fs.mkdirSync(dir);
		}
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
