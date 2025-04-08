from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
    <head>
        <title>
            TCP/IP PROTOCOLS
        </title>
    </head>
    <body bgcolor="pink">
      <center>  <font size="500">TCP/IP PROTOCOLS LIST</font></center><br>
      <center>1.Application Layer HTTP,FTP,SSH,Telnet,DNS<br><br>
      2.Transport Layer TCP,UDP<br><BR>
      3.Internet Layer IP,Routing Protocols(RIP,OSDP)<BR><BR>
      4.Link Layer Ethernet(MAC)<br><br></center>
      <center><font color="white"> Name: Avanthika.B<br><br>Register.No: 212224040039<br></font></center>
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()