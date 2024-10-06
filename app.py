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

# Sample recommendation model function
def recommend_ingredients(restaurant_name):
    loaded_model = load_model('ing_recommendation.h5')

    # Encode the restaurant name
    encoded_restaurant = restaurant_encoder.transform([restaurant_name])

    # Make a prediction
    predictions = loaded_model.predict(np.array([encoded_restaurant]))

    # Get the top 5 predicted products
    top_5_products = np.argsort(predictions[0])[-5:][::-1]
    top_5_product_names = product_encoder.inverse_transform(top_5_products)
    top_5_probabilities = predictions[0][top_5_products]

    return list(top_5_product_names), list(top_5_probabilities)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    restaurant_name = request.form.get('restaurant_name')
    print(restaurant_name)
    restaurant_name = restaurant_name.lower()
    ingredients, prob = recommend_ingredients(restaurant_name)
    return jsonify(ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
