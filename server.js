const http = require('http');
const fs = require('fs');
const { exec } = require('child_process');
const port = 3000;
let ebayData = null;

// Function to run the API integration script
function runApiIntegration(query) {
    return new Promise((resolve, reject) => {
        exec(`node apiIntegration.mjs ${query}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing API integration script: ${error.message}`);
                return reject(error);
            }
            if (stderr) {
                console.error(`API integration script stderr: ${stderr}`);
                return reject(new Error(stderr));
            }
            console.log(`API integration script stdout: ${stdout}`);
            resolve();
        });
    });
}

// Create HTTP server
const app = http.createServer((req, res) => {
    console.log(`Received request: ${req.method} ${req.url}`);

    if (req.method === 'POST' && req.url === '/data') {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
        req.on('end', () => {
            try {
                ebayData = JSON.parse(body);
                console.log("Data received:", ebayData);
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ message: 'Data received' }));
            } catch (error) {
                console.error("Error parsing JSON data:", error);
                res.writeHead(400, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ message: 'Invalid JSON data' }));
            }
        });
    } else if (req.method === 'GET' && req.url === '/') {
        fs.readFile('index.html', (error, data) => {
            if (error) {
                res.writeHead(404);
                res.write('File not found');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.write(data);
            }
            res.end();
        });
    } else if (req.method === 'GET' && req.url.startsWith('/listings.html')) {
        const query = new URL(req.url, `http://${req.headers.host}`).searchParams.get('query');
        if (query) {
            runApiIntegration(query)
                .then(() => {
                    fs.readFile('listings.html', (error, data) => {
                        if (error) {
                            res.writeHead(404);
                            res.write('File not found');
                        } else {
                            res.writeHead(200, { 'Content-Type': 'text/html' });
                            res.write(data);
                        }
                        res.end();
                    });
                })
                .catch(error => {
                    console.error('Error running API integration:', error);
                    res.writeHead(500);
                    res.write('Internal Server Error');
                    res.end();
                });
        } else {
            res.writeHead(400);
            res.write('Bad Request');
            res.end();
        }
    } else if (req.method === 'GET' && req.url === '/data') {
        console.log('Sending data to client:', ebayData);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(ebayData || {}));
    } else {
        res.writeHead(404);
        res.end();
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
