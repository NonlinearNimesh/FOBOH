# HOBOF Recommendation System
An automated solution for getting the recommendation of ingredients/products that the restaurants, bars, pubs, etc. of Sydney CBD 2000 will use.

## Table of Contents
- [Project Overview](#overview)
- [Implementation Flow](#Implementaion)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Tech stack](#technologies-used)
- [Contact](#contact)

## Overview
* The task of helping Ari, a sales rep at Hobof Foods Distributors, make smarter product suggestions for venues in Sydney CBD can be broken down into four key steps:
  * Web Scraping of Menus: The goal is to extract dish names, ingredients, and menu data from restaurants, cafes, and bars in Sydney CBD. This involves using web scraping tools like BeautifulSoup for parsing HTML and Selenium for dynamic content.
  * Ingredient Extraction: Once the menus are scraped, the next step is to extract ingredients using natural language processing (NLP) tools like spaCy or nltk. The process involves cleaning the data and detecting ingredients, potentially requiring custom rules or regex patterns to handle variations and aliases (e.g., "eggplant" vs. "aubergine").
  * Matching Ingredients to Products: The extracted ingredients need to be matched with products from the "PremierQualityFoodsBrochure2021.pdf" catalogue. Using tools like PyPDF2 to extract PDF content, fuzzy matching algorithms (such as RapidFuzz) will map menu ingredients to catalogue products, accounting for name variations and spelling differences.
  * Sales Suggestions: The final step is providing Ari with product recommendations via a user interface. By entering a venue name, the system will match dishes and ingredients with products and suggest the best matches using a database of scraped menus and catalogues. Over time, suggestions can improve through machine learning or rule-based recommendations, and the interface can be built using Flask or FastAPI, integrated with conversational AI tools for a more natural experience.
 
## Implementation
![Alt text](./static/HOBOF-WorkFLowdrawio.jpg)

## Data
Data that is being used in order to complete this project can be accessed here
```bash
   https://drive.google.com/file/d/1PYQdGHW3b1g47GrPeZOxR7-Iw3kpoqnv/view?usp=drive_link
   ```

## Installation
* Cloning the repository
```bash
   git clone https://github.com/username/project-name.git
   ```
* Docker image build 
```bash
   docker build -t IMAGE_NAME:Version .
   ```
* Once the docker image is created, Put it in the docker-compose.yml file.
```bash
   docker-compose up -d
   ```
* This will start the web app on 5000 port.
* PS : if you don't want to build a docker image, you can just run docker-compose command it will generate it automatically and start the container on 5000 port

## Usage
This web application helps restaurants receive smarter product suggestions by analyzing their menu and matching ingredients with product catalogs.

### Prerequisites
- Dockers

### Access the Web App
1. Visit http://123.345.23.1:5000/. (dummy)
2. If running locally, navigate to the project directory and start the server:
   ```bash
   python app.py
   ```
3. Once the server is running, go to `http://127.0.0.1:5000` in your browser.

### How to Use
1. Enter the restaurant name into the input field on the homepage.
2. Choose between "AI-based" or "Fuzzy matching" ingredient recommendations using the radio buttons.
3. Click the "Submit" button to get product suggestions.
4. Review the results, which show Product that Ari can pitch to the input restaurants.
### Example:
![Alt text](./static/fuzzy-result.png)
![Alt text](./static/ai-results.png)

### Use Case
* Sales reps can find matching products in the catalog for specific dishes offered by restaurants.

## Tech Stack
- Python (Flask, BeautifulSoup, Pandas, numpy, tensorflow, keras, tranformers, selenium, NLP, NLTK, Spacy, fuzzy matching, pdfplumber etc.)
- JavaScript (Frontend scripting)
- HTML & CSS (Frontend design)
- CSV
- Dockers
- GCP


## Contact
[Nimesh Kumar](https://github.com/NonlinerNimesh) - imnimeshkumar@outlook.com
