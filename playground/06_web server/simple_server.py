
# script sets up a simple HTTP server using the BaseHTTPServer module in Python. The server listens on port 5001 and responds to GET requests by returning a basic HTML page


from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(self.Page.encode())

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('localhost', 5001)
    server = HTTPServer(serverAddress, RequestHandler)
    print(f"Server started on port {serverAddress[1]}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")