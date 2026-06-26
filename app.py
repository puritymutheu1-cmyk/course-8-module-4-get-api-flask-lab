

from flask import Flask, jsonify, request
from data.products import PRODUCTS

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Product Catalog API!",
        "version": "1.0.0",
        "endpoints": {
            "all_products":        "GET /products",
            "filter_by_category":  "GET /products?category=<category>",
            "single_product":      "GET /products/<id>"
        }
    }), 200


@app.route("/products", methods=["GET"])
def get_products():
    # Read optional 'category' query parameter from the URL
    category_filter = request.args.get("category")

    if category_filter:
        # Normalize to lowercase to ensure consistent matching
        normalized = category_filter.strip().lower()
        filtered = [
            p for p in PRODUCTS
            if p["category"].lower() == normalized
        ]

       
        if not filtered:
            return jsonify({
                "error":    "No products found",
                "category": category_filter
            }), 404

        return jsonify({
            "category": normalized,
            "count":    len(filtered),
            "products": filtered
        }), 200

    
    return jsonify({
        "count":    len(PRODUCTS),
        "products": PRODUCTS
    }), 200


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    # Search the dataset for a product whose id matches
    product = next(
        (p for p in PRODUCTS if p["id"] == product_id),
        None  # Default to None if not found
    )

    # Return 404 with a clear error message if ID is not found
    if product is None:
        return jsonify({
            "error":      "Product not found",
            "product_id": product_id
        }), 404


    return jsonify({"product": product}), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error":   "Route not found",
        "message": "Check the /  endpoint for available routes."
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error":   "Bad request",
        "message": "The request could not be understood by the server."
    }), 400


if __name__ == "__main__":
    app.run(debug=True)