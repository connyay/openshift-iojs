'use strict';
var http = require('http');
var env = process.env;
var port = env.OPENSHIFT_IOJS_PORT || 1337;
var ip = env.OPENSHIFT_IOJS_IP || '127.0.0.1';

http.createServer(function(req, res) {
    var body = 'Welcome to io.js on OpenShift!\n\n' +
        'Everything seems to be in order.\n' +
        'Running io.js ' + process.version;

    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.end(body);
}).listen(port, ip);
