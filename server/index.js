const express = require('express');
const mongoose = require('mongoose');
const helmet = require('helmet');
const cors = require('cors');

const compile = require('./routes/api/compile');
const zip = require('./routes/api/zip');
const generate = require('./routes/api/generate');
const upload = require('express-fileupload');
const bodyParser = require('body-parser');
const bcrypt = require('bcryptjs');
const passport = require('passport');
const localStrategy = require('passport-local').Strategy;
const expressValidator = require('express-validator');
const expressSession = require('express-session');
const cookieParser = require('cookie-parser');

const { authenticated } = require('./helpers/authentication');

const User = require('./models/User');
const File = require('./models/Files');
const app = express();
var fs = require('fs');

//Database config goes here
const db = require('./config/keys').mongoURI;

//Database connection goes here
app.use(cors());
app.use(helmet());

mongoose
	.connect(db, {
		useNewUrlParser: true
	})
	.then(() => console.log('Database connected'))
	.catch(err => console.log(err));

app.use(upload());

// Body Parser

app.use(bodyParser.urlencoded({
	extended: true
}));
app.use(bodyParser.json());

app.use(expressValidator());
app.use(cookieParser());
app.use(
	expressSession({
		secret: 'ilovecoding',
		saveUninitialized: true,
		resave: true,
		cookie: {
			maxAge: 3600 * 1000
		}
	})
);
app.use(passport.initialize());
app.use(passport.session());

app.use(passport.initialize());
app.use(passport.session());

app.use(express.static('public'));
app.set('view engine', 'ejs');

passport.use(
	new localStrategy({
			usernameField: 'email'
		},
		function (email, password, done) {
			User.findOne({
				email: email
			}, function (err, user) {
				if (err) {
					return done(err);
				}
				if (!user) {
					return done(null, false, {
						message: 'Incorrect username.'
					});
				}
				bcrypt.compare(password, user.password, function (err, matched) {
					if (err) {
						return done(err);
					} else if (matched) {
						return done(null, user);
					} else {
						return done(null, false, {
							message: 'incorrect password'
						});
					}
				});
			});
		}
	)
);
passport.serializeUser(function (user, done) {
	return done(null, user.id);
});
passport.deserializeUser(function (id, done) {
	User.findById(id, function (err, user) {
		return done(err, user);
	});
});

app.get('/', (req, res) => {
	res.render('pages/landing');
});
app.get('/upload-file', authenticated, function(req, res) {
	res.render('pages/index');
});
app.post('/api/upload', function (req, res) {
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
		file.mv(uploadpath, function (err) {
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
app.get('/register', function(req, res) {
	if (req.user) {
		res.redirect('/');
	} else {
		res.render('pages/signup', {
			errors: req.session.errors
		});
	}
	//resetting session properties to null
	req.session.errors = null;
});
app.post('/register', function (req, res) {
	req.check('firstName', 'First name is required').notEmpty();
	req.check('lastName', 'Last Name required').notEmpty();
	req.check('email', 'Invalid email address').isEmail();
	req.check('password', 'Password is invalid must be of length 6').isLength({
		min: 6
	});
	req.check('password', 'Passwords are not matching').equals(req.body.confirmPassword);

	let errors = req.validationErrors();
	if (errors) {
		req.session.errors = errors;
		res.redirect('/register');
	} else {
		const newUser = new User({
			firstName: req.body.firstName,
			lastName: req.body.lastName,
			email: req.body.email,
			password: req.body.password
		});
		bcrypt.genSalt(10, (error, salt) => {
			bcrypt.hash(newUser.password, salt, (err, hash) => {
				newUser.password = hash;
				newUser
					.save()
					.then(savedUser => {
						res.redirect('/login');
					})
					.catch(error => console.log(error));
			});
		});
	}
});
app.get('/login', (req, res) => {
	if (req.user) {
		return res.redirect('/');
	} else {
		res.render('pages/login');
	}
});
app.post('/login', (req, res, done) => {
	passport.authenticate('local', {
		failureRedirect: '/login',
		successRedirect: '/'
	})(req, res, done);
});
//get the uploaded files
app.get('/uploaded-files', (req, res) => {
	File.find({
		user: req.user.id
	}).then(files => {
		res.render('pages/files', {
			files: files
		});
	});
});
//get selected file
app.get('/download/:id', (req, res) => {
	var filepath = 'server/uploads/' + req.params.id;
	var filename = req.params.id;
	res.download(filepath, filename);
});
//Compile, generate and zip routes
app.use('/api/compile', compile);
app.use('/api/zip', zip);
app.use('/api/generate', generate);

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server running on port ${port}`));