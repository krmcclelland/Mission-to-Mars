{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6749f4da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask to render a template, redirecting to another url, and creating a URL.\n",
    "from flask import Flask, render_template, redirect, url_for\n",
    "\n",
    "# PyMongo to interact with our Mongo database.\n",
    "from flask_pymongo import PyMongo\n",
    "\n",
    "# Use the scraping code, we will convert from Jupyter notebook to Python.\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3af6fa62",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b6596b1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f3edc593",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "# Tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.\n",
    "# URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named \"mars_app\".\n",
    "app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars-app'\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a919dd92",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the route for the HTML page\n",
    "@app.route('/')\n",
    "def index():\n",
    "\tmars - mongo.db.mars.find_one()\n",
    "\treturn render_template('index.html', mars = mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b5874978",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add the next route and function to our code\n",
    "## defines the route that Flask will be using.  Scrape will run the function that we create just beneath it.\n",
    "@app.route('/scrape')\n",
    "\n",
    "# The next lines allow us to access the database, scrape new data using our scraping.py\n",
    "## First, we define it with def scrape():\n",
    "def scrape():\n",
    "\t### We assign a new variable that points to our Mongo database.\n",
    "\tmars = mongo.db.mars\n",
    "\t### Create a new variable to hold the newly scraped data referencing scraping all.\n",
    "\tmars_data = scraping.scrape_all()\n",
    "\t### Now that we've gathered new data, we need to update the database using update_one()\n",
    "\tmars.update_one({}, {'$set': mars_data}, upsert = True)\n",
    "\t### Code we need for Flask is to tell it to run\n",
    "\treturn redirect('/', code = 302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22cacb46",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58294150",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
