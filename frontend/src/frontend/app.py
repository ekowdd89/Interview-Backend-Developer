from flask import Flask, render_template, request, redirect, url_for
from .http_client import get_products, post_product, get_product, update_product, delete_product
app = Flask(__name__)
app.jinja_env.cache = {}
@app.route("/")
def index():
    products = get_products()
    print(products)
    return render_template("index.html", products=products, title="Product List")
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        post_product({"name": name, "price": price, "quantity": quantity})
        return redirect(url_for('index'))
    return render_template("form.html", title="Create Product")
@app.route("/edit/<int:id>", methods=["GET", "POST", "PUT"])
def edit(id):
    product = get_product(id)
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        update_product({"name": name, "price": price, "quantity": quantity}, id)
        return redirect(url_for('index'))
    return render_template('form.html', title="Edit Product", product=product)
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    delete_product(id)
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)