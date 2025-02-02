from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

[{"name":"BCPr6N","marks":73},{"name":"t0","marks":85},{"name":"LSbx8","marks":41},{"name":"kEA5x6Xl","marks":31},{"name":"oQ2BHjCfPY","marks":90},{"name":"6KodD","marks":28},{"name":"s2tJuMoQ","marks":21},{"name":"OkjEqh","marks":49},{"name":"AHE9nAWQ2","marks":94},{"name":"H","marks":58},{"name":"5U","marks":13},{"name":"6zuhtKZCqa","marks":76},{"name":"0G8s60eDa","marks":96},{"name":"CB","marks":22},{"name":"3f2vWfVOp","marks":82},{"name":"8Rpd","marks":71},{"name":"UsojywJwE","marks":15},{"name":"KBaXWWbFp","marks":42},{"name":"K","marks":1},{"name":"b3IoyfGrf","marks":94},{"name":"w1FtK","marks":94},{"name":"Z5JKdo","marks":59},{"name":"Au2zl","marks":90},{"name":"Rtlx9","marks":20},{"name":"YUusM","marks":76},{"name":"b2eNAhj0E","marks":37},{"name":"MEG","marks":87},{"name":"Y9sMWAbQ","marks":6},{"name":"qYhgxY8K6I","marks":6},{"name":"SsLe8uNMe","marks":23},{"name":"q7rMOk","marks":38},{"name":"XA17","marks":40},{"name":"QmJkZdWl","marks":5},{"name":"nEx2vHU2","marks":36},{"name":"NJ","marks":95},{"name":"rPUrrIscs","marks":79},{"name":"7xstxMYG0","marks":41},{"name":"hrcS","marks":69},{"name":"tkRWL7vtvx","marks":47},{"name":"eP","marks":25},{"name":"R7s","marks":18},{"name":"8DeaJZp","marks":13},{"name":"u8gMjAdYOS","marks":41},{"name":"mKR0SYWOcs","marks":33},{"name":"Zw8","marks":22},{"name":"ThMHDpMIDo","marks":40},{"name":"GQ","marks":86},{"name":"oUaSkl8x","marks":26},{"name":"kwWIl","marks":76},{"name":"PSxfZHb","marks":10},{"name":"xudQUOyE","marks":68},{"name":"2tZvK","marks":90},{"name":"U5Ds","marks":98},{"name":"lo7dluAV","marks":7},{"name":"p","marks":51},{"name":"TlmcHV7lR","marks":74},{"name":"1stulwf","marks":40},{"name":"MB","marks":25},{"name":"J564k9","marks":97},{"name":"j6G3WmvN","marks":81},{"name":"gqLl","marks":43},{"name":"nTWi","marks":27},{"name":"fDbtp2Hl1U","marks":48},{"name":"ZaZ8I7bOt","marks":47},{"name":"jSeucmA","marks":70},{"name":"R","marks":6},{"name":"6ECu","marks":34},{"name":"nxV36","marks":19},{"name":"XeKkv","marks":74},{"name":"5LSevwud","marks":53},{"name":"iHS1fVxqe","marks":67},{"name":"pe6q5","marks":83},{"name":"VQ0aE","marks":80},{"name":"D","marks":50},{"name":"fCLCOxBP","marks":7},{"name":"m46","marks":79},{"name":"OCaUy5I","marks":5},{"name":"SVZHZe","marks":20},{"name":"o","marks":32},{"name":"HRGm9209V","marks":44},{"name":"QxGdv","marks":3},{"name":"2eEJv0Z","marks":16},{"name":"numY","marks":77},{"name":"AfYEjHyF","marks":78},{"name":"4rixy","marks":94},{"name":"L","marks":89},{"name":"Uaa","marks":25},{"name":"ENCuXV","marks":18},{"name":"gvS7H1c","marks":93},{"name":"s1jJsHSxfO","marks":48},{"name":"Pbzqvq","marks":57},{"name":"P88zYo","marks":77},{"name":"n3RCJArWBn","marks":6},{"name":"UwwJQn8P","marks":44},{"name":"N","marks":28},{"name":"cc6","marks":51},{"name":"54sw4","marks":29},{"name":"Bd","marks":67},{"name":"sxi0YHe","marks":76},{"name":"NYhaLmF","marks":51}]

def find_marks_by_names(names):
    marks = []
    for name in names:
        found = False
        for student in students:
            if student["name"] == name:
                marks.append(student["marks"])
                found = True
                break
        if not found:
            marks.append(None)  # If student not found, append None
    return marks

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get list of names from the query string
    if not names:
        return jsonify({"error": "No names provided"}), 400

    marks_result = find_marks_by_names(names)
    
    return jsonify({"marks": marks_result})

if __name__ == '__main__':
    app.run(debug=True)
