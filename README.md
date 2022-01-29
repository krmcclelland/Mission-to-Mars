# Mission-to-Mars Challenge
## Web Scraping with HTML/CSS

## Main Objectives
* Understand the use of the following items: 
  * HTML elements
  * class and id attributes 
  * identify content for web scraping.
* Use BeautifulSoup and Splinter to automate a web browser and perform a web scrape.
* Create a MongoDB database to store scrapped data.
* Create a web application with Flask to display the data from the web scrape.
* Create an HTML/CSS portfolio to showcase projects.
* Use Bootstrap components to polish and customize the portfolio.

## Data Environment Used
* BeautifulSoup4
* Bootstrap
* DateTime 
* Flask
* Flask-PyMongo
* html5lib
* Jupyter Notebook
* MongoDB
* Numpy
* Pandas
* PyMongo
* Splinter
* VS Code
* webdriver-manager

# Web Scraping Mars data from NASA using Jupyter Notebook
BeautifulSoup and Splinter were used to automate a web browser and perform a web scrape.

## Mars Hemisphere data dictionary
![Pic 1](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Mars_Hemisphere_Data_Dictionary.PNG)

# Using MongoDB and Flask to display the data as HTML/CSS
MongoDB database was used to store data from the web scrape, and then a web application was created with Flask to display the data from the web scrape.

The Python code from the scraping file may differ slightly from the Jupyter Notebook Mission to Mars Challenge file.  Some variables needed to be changed to match other files. 

## Final code in the scraping file:
![Pic 2](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Final_Code_In_Scraping_File.PNG)

## Website after scraping:
![Pic 3](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Landing_Page.PNG)

### Scape Button
![Pic 4](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Scape_Button.PNG)

### Latest Mars News
![Pic 5](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Latest_Mars_News.PNG)

### Mars Facts
![Pic 6](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Mars_Facts.PNG)

### Mars Hemisphere
![Pic 7](https://github.com/krmcclelland/Mission-to-Mars/blob/main/Mission_To_Mars_Challenge/images/Mars_Hemisphere.PNG)

# Using Bootstrap 3 to modify the html file
## The webpage is mobile-responsive
Changed everything to col-xs, which is the smallest option.  Everything will scale up from the mobile phones size to the larger desktop sizes. 

## Two additional Bootstrap 3 components are used to style the webpage
* Changed the button color to warning, which is orange to match the header color.
* Added a tooltip that says Click Me!, when the user hoovers over the Scrape button.
* Bonus: Changed the colors of various areas, adjusted some heights, and added a striped table pattern.
