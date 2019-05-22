const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const fileSchema = new Schema({
	user: {
		type: Schema.Types.ObjectId,
		ref: 'user'
	},
	file: {
		type: String,
		required: true
	}
});

module.exports = mongoose.model('file', fileSchema);
