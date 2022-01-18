from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

import warnings
warnings.filterwarnings("ignore")

import os
os.getcwd()

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# # Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# # Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# # Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# # Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# # Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# # JPL Space Images Featured Image
# ## Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# ## Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# ## Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# ## Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# ## Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# # Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df
df.to_html()

# # Mars Weather
# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')

# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ## Hemispheres
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Parse the html with soup
html = browser.html
main_page_soup = soup(html, 'html.parser')

# Find the number of pictures to scan
pics_count = len(main_page_soup.select("div.item"))

# for loop over the link of each sample picture
for i in range(pics_count):

    # Create an empty dict to hold the search results
    results = {}
    
    # Find link to picture and open it
    link_image = main_page_soup.select("div.description a")[i].get('href')
    browser.visit(f'https://astrogeology.usgs.gov{link_image}')  
    
    # Parse the new html page with soup
    html = browser.html
    sample_image_soup = soup(html, 'html.parser')
    
    # Get the full image link
    img_url = sample_image_soup.select_one("div.downloads ul li a").get('href')

    # Get the full image title
    img_title = sample_image_soup.select_one("h2.title").get_text()

    # Add extracts to the results dict
    results = {
        'img_url': img_url,
        'title': img_title}

    # Append results dict to hemisphere image urls list
    hemisphere_image_urls.append(results)

# for loop over the link of each sample picture
for i in range(pics_count):
    # Create an empty dict to hold the search results
    results = {}
    # Find link to picture and open it
    link_image = main_page_soup.select("div.description a")[i].get('href')
    browser.visit(f'https://astrogeology.usgs.gov{link_image}')

    # Parse the new html page with soup
    html = browser.html
    sample_image_soup = soup(html, 'html.parser')

    # Get the full image link
    img_url = sample_image_soup.select_one("div.downloads ul li a").get('href')
    
    # Get the full image title
    img_title = sample_image_soup.select_one("h2.title").get_text()
    
    # Add extracts to the results dict
    results = {
        'img_url': img_url,
        'title': img_title}

imgs_links= browser.find_by_css("a.product-item h3")
for x in range(len(imgs_links)):
    hemisphere={}
    
    #Find elements going to click link. 
    browser.find_by_css("a.product-item h3")[x].click()
    
    #Find sample image link
    sample_img= browser.find_link_by_text("Sample").first
    hemisphere['img_url']=sample_img['href']
    
    # Get hemisphere Title 
    hemisphere['title']=browser.find_by_css("h2.title").text
    
    # Add Objects to hemisphere_image_urls list
    hemisphere_image_urls.append(hemisphere)
    
    # Return to main page
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

browser.quit()
