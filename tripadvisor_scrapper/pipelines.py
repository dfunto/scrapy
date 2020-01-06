# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import pkgutil

from google.cloud import storage
from google.oauth2 import service_account
from datetime import datetime

class GCPItemPipeline(object):

    def open_spider(self, spider):
        self.locations = []

    def process_item(self, item, spider):
        self.locations.append(dict(item))
        return item
    
    def close_spider(self, spider):
        gcp_project = spider.settings["GCP_PROJECT"]
        gcp_auth_path = spider.settings["GCP_JSON_AUTH_PATH"]
        gcp_bucket = spider.settings["GCP_BUCKET"]
        gcp_folder = spider.settings["GCP_FOLDER"]
        gcp_file = spider.settings["GCP_FILENAME"]

        # Login to google cloud and obtain client
        json_string = pkgutil.get_data("tripadvisor_scrapper", gcp_auth_path)
        info = json.loads(json_string)
        cred = service_account.Credentials.from_service_account_info(info)
        client = storage.Client(project=gcp_project,credentials=cred)

        # Set bucket and file
        bucket = client.get_bucket(gcp_bucket)
        blob = bucket.blob( 
            "{0}{1}_{2}.txt".format(
                gcp_folder, 
                gcp_file, 
                datetime.now().strftime("%Y%m%d%H%M%S")
            )
        )

        # Output json
        output_str = json.dumps(self.locations,ensure_ascii=False)

        # Write to gcp (default encoding=utf8)
        if output_str != "":
            blob.upload_from_string(output_str,content_type="text/plain")
        