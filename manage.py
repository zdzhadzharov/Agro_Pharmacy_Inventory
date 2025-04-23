from flask import Flask, render_template, request, redirect
from app import add_product, get_all_products_with_id, delete_product, update_product

app = Flask(__name__)

@app.route("/")
def index():
    products = get_all_products_with_id()
    return render_template("index.html", products=products)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    category = request.form["category"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    add_product(name, category, quantity, price)
    return redirect("/")

@app.route("/delete/<product_id>")
def delete(product_id):
    delete_product(product_id)
    return redirect("/")

@app.route("/update/<product_id>", methods=["POST"])
def update(product_id):
    updates = {
        "name": request.form["name"],
        "category": request.form["category"],
        "quantity": int(request.form["quantity"]),
        "price": float(request.form["price"]),
    }
    update_product(product_id, updates)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
