from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
#from Mission_to_Mars_challenge import hemisphere_image_urls
import scraping

#flask setup
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define route
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
   #return render_template("index.html",hemisphere_image_urls=hemisphere_image_urls)

if __name__ == "__main__":
   app.run()