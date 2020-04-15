from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    url_str = 'www.baidu.com'
    my_list = [1,3,5,7,9]
    return render_template('index.html',url_str=url_str,my_list=my_list)
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    return 'order_id %s' %order_id

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5120)
