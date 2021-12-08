'use strict';

var config = require('./config.webgme'),
    validateConfig = require('webgme/config/validator');

// Add/overwrite any additional settings here
const mongoHost = process.env.MONGO_HOST || '127.0.0.1';
config.mongo.uri = `mongodb://${mongoHost}:27017/webgme_dcrypps`;
config.plugin.allowServerExecution = true;

config.seedProjects.defaultProject = 'PetSeed';

config.requirejsPaths['jointjs'] = './node_modules/jointjs/dist/joint.min';


validateConfig(config);
module.exports = config;
