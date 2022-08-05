import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        user = self.headers['x-dw-user']
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Return the user info if the user logged in
        if user == 'true':
            username = self.headers['username']
            email = self.headers['email']
            token = self.headers['x-datawiza-token-aad-access-token']
            html = f'No-code SSO for a Python program by <a href="https://www.datawiza.com">Datawiza</a>.</br>\
                Welcome, ' + username + '!</br>\
                Email: ' + email + '</br>\
                Your Microsoft Azure AD access token: ' + token + '</br>\
                <a href="/ab-logout">Logout</a>'
        else:
            html = f'No-code SSO for a Python program by <a href="https://www.datawiza.com">Datawiza</a>.</br>\
                User not found.</br>\
                You can see <a href="https://github.com/datawiza-inc/Azure-AD-SSO-Python-App">here</a> how to use No-Code Datwiza to authenticate a Python app using Microsoft Azure AD.'

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))

        return

handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
