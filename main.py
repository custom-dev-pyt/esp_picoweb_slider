import picoweb


app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("POST form:<br>")
    yield from resp.awrite("<form action='/' method='POST'>"
        "<input type='range' min='0' max='100' name='value' /> "
        "<input type='submit' value='submit' />")
    if req.method == "POST":
        data = yield from req.read_form_data()
        print(req.form['name_of_slider'])
        
    
import ulogging as logging
logging.basicConfig(level=logging.INFO)

app.run(debug=True, host=esp_addr[0])
