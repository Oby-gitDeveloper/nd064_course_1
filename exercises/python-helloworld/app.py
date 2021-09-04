from flask import Flask
app = Flask(__name__)

@app.route("/status")
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result": "OK- healthy"})
            status=200,
            mimetype='application/json'
    )
    
    app.logger.info('status request successfull') 
    return response       
            
@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code":"0", "data":{"UserCount":140,"UserCountActive":23}})
        status=200,
        mimetype='application/json'
                            
    )
    app.logger.info('metrics request successfull')
    return response 

@app.route("/")
def hello():
    app.logger.info('Main request successful')
    
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
     ##stream logs to a file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
