const celery = require('celery-node');

const brokerUrl = 'redis://redis:6379/0';
const backend = 'redis://';

const client = celery.createClient(brokerUrl, backend);

module.exports = client;