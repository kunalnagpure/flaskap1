from flask import Flask, request, json

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.post('https://httpbin.org/post', json={'id': 1, 'name': 'Kunal'})

    print("Status code: ", response.status_code)
    print("Printing Entire Post Request")
    print(response.json())


with open('response', 'w') as json_file:
    json.dump(response, json_file)



@app.route("/Kunal")
def Kunal():
    return "Hello, Kunal"


if __name__ == "__main__":
    app.run(debug=True)