from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars-app'
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route('/')
def index():
	mars - mongo.db.mars.find_one()
	return render_template('index.html', mars = mars)

# Add the next route and function to our code
## defines the route that Flask will be using.  Scrape will run the function that we create just beneath it.
@app.route('/scrape')
# The next lines allow us to access the database, scrape new data using our scraping.py
## First, we define it with def scrate():
def scrape():
	### We assign a new variable that points to our Mongo database.
	mars = mongo.db.mars
	### Create a new variable to hold the newly scraped data referencing scraping all.
	mars_data = scraping.scrape_all()
	### Now that we've gathered new data, we need to update the database using update_one()
	mars.update_one({}, {'$set': mars_data}, upsert = True)
	### Code we need for Flask is to tell it to run
	return redirect('/', code = 302)

if __name__ == "__main__":
   app.run()