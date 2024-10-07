from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle


with open('restaurant_encoder.pkl', 'rb') as f:
    restaurant_encoder = pickle.load(f)

with open('product_encoder.pkl', 'rb') as f:
    product_encoder = pickle.load(f)

app = Flask(__name__)

def recommend_ingredients(restaurant_name):
    loaded_model = load_model('ing_recommendation.h5')
    encoded_restaurant = restaurant_encoder.transform([restaurant_name])
    predictions = loaded_model.predict(np.array([encoded_restaurant]))
    top_5_products = np.argsort(predictions[0])[-10:][::-1]
    top_5_product_names = product_encoder.inverse_transform(top_5_products)
    top_5_probabilities = predictions[0][top_5_products]
    return list(top_5_product_names), list(top_5_probabilities)

import sqlite3

def get_matched_products(sqlite_db_path, table_name, restaurant_name):
    restaurant_name = restaurant_name.lower()
    conn = sqlite3.connect(sqlite_db_path)
    try:
        cur = conn.cursor()
        query = f"""
            SELECT MatchedProduct FROM {table_name}
            WHERE Restaurant = ?
        """
        cur.execute(query, (restaurant_name,))
        matched_products = cur.fetchall()
        matched = [product[0] for product in matched_products] if matched_products else []
        print(matched)
        return matched
    finally:
        conn.close()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        restaurant_name = request.form.get('restaurant_name')
        print(restaurant_name)
        restaurant_name = restaurant_name.lower()
        matching_type = request.form.get('matching_type')
        print("<<<<<<<<<<<<<<<<<<<<<<<<<", matching_type)
        if matching_type == 'fuzzy':
            print("In Fuzzy")
            sqlite_db_path = "fuzzy_db.db"
            table_name = "fuzzy_matching"
            ingredients = get_matched_products(sqlite_db_path, table_name, restaurant_name)
            return jsonify(ingredients=ingredients)
        ingredients, prob = recommend_ingredients(restaurant_name)
        return jsonify(ingredients=ingredients)
    except Exception as e:
        return jsonify(ingredients=["Internal Error Occured", e])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
