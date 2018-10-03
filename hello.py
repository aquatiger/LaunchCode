import flask

helloapp = flask.Flask(__name__)

@helloapp.route("/")
def index():
   return """
<html><head><title>Hello</title></head>
<body>
<h1>Hello from Flask!</h1>
</body></html>"""

if __name__ == "__main__":
    helloapp.run()