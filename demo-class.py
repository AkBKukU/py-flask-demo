#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import send_file
from flask import redirect
from flask import make_response

from multiprocessing import Process

class WebClass(object):

    def __init__(self):
        self.app = Flask("The Web: Now with 100% More OOP")

        # Define routes in class to use with flask
        self.app.add_url_rule('/my/cool/site/index.html','1', self.index)
        self.app.add_url_rule('/my/cool/site/data.json','2', self.data)

        # Set headers for server
        self.app.after_request(self.add_header)
    
    def add_header(self,r):
        """
        Force the page cache to be reloaded each time
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    def start(self):
        """ Run Flask in a process thread that is non-blocking """
        self.web_thread = Process(target=self.app.run, kwargs={"host":"0.0.0.0"})
        self.web_thread.start()

    def stop(self):
        """ Send SIGKILL and join thread to end Flask server """
        self.web_thread.terminate()
        self.web_thread.join()


    def index(self):
        """ Simple class function to send HTML to browser """
        return   "<h1>Sup</h1>"
    
    def data(self):
        """ Simple class function to send JSON to browser """
        return  dict({"stuff":1337})

if __name__ == '__main__': 
    web = WebClass()
    web.start()

    input('press ENTER to close...\n')

    web.stop()


