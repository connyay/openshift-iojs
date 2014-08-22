var http = require('http');
var env = process.env;
var port = env.OPENSHIFT_NODEDIY_PORT || 1337;
var ip = env.OPENSHIFT_NODEDIY_IP || '127.0.0.1';

http.createServer(function(req, res) {
    var body = 'Welcome to Node DIY!\n\n' +
        'Everything seems to be in order.\n' +
        'Running Node.js ' + process.version;

    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.end(body);
}).listen(port, ip);
