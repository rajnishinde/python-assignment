import flask

app = flask.Flask("__main__")

def get_name():
    # names = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
    names = ['H', ',', 'E', ',', 'L', ',', 'L', ',', 'O', ',', ' ', 'W', ',', 'O', ',', 'R', ',', 'L', ',', 'D']
    a= ""
    for name in names:
        a = a + name
    result = a
    result = result.replace(',', '')
    return result

@app.route("/")
def my_index():
     name= get_name()
     return name
    # name1= "Helllo world"
    # return flask.render_template("index.html",name=name1)

@app.route("/about")
def my_index_1():
    return flask.render_template("index2.html")

app.run(debug=True)
