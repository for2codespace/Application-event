from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.proxy_request()

    def do_POST(self):
        self.proxy_request()

    def proxy_request(self):
        target_host = 'localhost'
        if self.headers.get('Host').startswith('backend'):
            target_port = 5000
            print("request forwarded to 5000 port")
        else:
            target_port = 3000
            print("request forwarded to 3000 port")

        conn = http.client.HTTPConnection(target_host, target_port)
        conn.request(self.command, self.path, headers=dict(self.headers))
        response = conn.getresponse()

        self.send_response(response.status)
        for header, value in response.getheaders():
            self.send_header(header, value)
        self.end_headers()

        self.wfile.write(response.read())
        

def run_proxy_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, ProxyHandler)
    print("Proxy server running on port 80")
    httpd.serve_forever()

if __name__ == '__main__':
    run_proxy_server()
