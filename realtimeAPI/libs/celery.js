const celery = require('celery-node');

const brokerUrl = 'redis://ip172-18-0-123-buhfsr1qckh0008ru550-3000.direct.labs.play-with-docker.com:6379/0';
const backend = 'redis://';

const client = celery.createClient(brokerUrl, backend);

module.exports = client;