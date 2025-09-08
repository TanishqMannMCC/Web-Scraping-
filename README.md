Indian City Population Analysis
This project is an end-to-end data analysis workflow that focuses on the population of Indian cities. The process includes web scraping, data preprocessing, and data visualization.

Project Steps
The project was divided into three main stages:

1. Data Scraping
Goal: To extract population data for Indian cities from the years 2001 and 2011.

Source: Data was scraped from the Wikipedia page titled "List of cities in India by population."

Tool: The city_scraper.py script was used to fetch the HTML content, parse it using BeautifulSoup, and extract relevant data from the tables.

Output: The raw, scraped data was saved into a CSV file.

2. Data Preprocessing
Goal: To clean the scraped data and prepare it for analysis.

Tool: The preprocessing.py script performed the following steps:

It loaded the raw CSV file.

It handled missing values by removing rows with incomplete data.

It converted population columns from strings to numerical data types.

It calculated a new column, Growth Rate (%), by comparing the 2011 and 2001 population figures.

Output: The cleaned and processed data was saved to india_cities_preprocessed.csv.

3. Data Visualization
Goal: To create an interactive dashboard for visualizing key population trends.

Tool: The preprocessed data was imported into Power BI.

Output: The Indian City Population Dashboard.pbix file was created, which contains a dashboard with various charts and graphs to show population change, growth rate, and other insights across different cities and states.

Files
city_scraper.py: Python script for scraping data.

preprocessing.py: Python script for data cleaning and transformation.

india_cities_preprocessed.csv: The final preprocessed data file used for the dashboard.

Indian City Population Dashboard.pbix: The Power BI dashboard file.

README.md: This file.
