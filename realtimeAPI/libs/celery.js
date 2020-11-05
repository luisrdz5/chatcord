const celery = require('celery-node');

const server = process.env.REDIS_SERVER || '127.0.0.1';
const brokerUrl = `redis://${server}:6379/0`;
const backend = 'redis://';

const client = celery.createClient(brokerUrl, backend);

module.exports = client;