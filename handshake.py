RESPONSE = '''
HTTP/1.1 101 Switching Protocols
Connection:Upgrade
Server: tang websocket server
Upgrade:WebSocket
Date:
Access-Control-Allow-Credentials:true
Access-Control-Allow-Headers:content-type
Sec-WebSocket-Accept:
'''

class HandShake:
    receive = None
    request = None

    def parse_msg(self, msg):
        l = msg.split("\r\n")
        request = {'method': l[0]}
        for line in l[1:]:
            if line:
                [name, value] = line.split(':', 1)
                request[name.strip()] = value.strip()

        self.request = request
        return self





