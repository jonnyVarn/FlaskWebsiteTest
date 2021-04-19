from flask import Flask

app = Flask(__name__)

@app.route("/") # dekorativ stuff gör om  / är beroende på vilken route /api /bilder etc går också att använda.
def home():
    return "Hej välkommen till min coola hemsida <h1>jag skriver någon header </h1> <h2> br no work?</h2>"

app.run(host='0.0.0.0', port=80)
#host, port, debug, options

