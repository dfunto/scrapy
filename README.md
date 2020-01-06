# Scrapy - Trip Advisor Ratings To GCP

Web scrapper written for python3 to scrape trip advisor's ratings, addresses and other basic informations.

The output is written to Google Cloud Plataform Storage.

## Parameters

All parameters should be written to /tripadvisor_scrapper/setting.py file.

### TRIP ADVISOR URLS SETTINGS
Use the TARGET_URLS setting to set trip advisor target urls

   TARGET_URLS = [u"url1" , u"url2"]

### GOOGLE CLOUD STORAGE SETTINGS
Use the following settings to authenticate to Google Cloud Plataform

Google Cloud Plataform project to work on

  - GCP_PROJECT

Service Account JSON file for authentication (keep same file path and name)

  - GCP_JSON_AUTH_PATH = "resources/gcp_auth.json"

Target bucket and file, the filename suffix with datetime will added automatticaly

  - GCP_BUCKET

  - GCP_FOLDER

  - GCP_FILENAME
