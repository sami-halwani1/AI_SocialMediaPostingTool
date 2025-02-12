from openai import OpenAI
import json
import csv
from datetime import datetime
import os
import re

"""
Author: Majeks Software LLC
Developer: Sami Halwani
Project Name: SEO Blogger
Description: The Purpose of this application is to create an automated Facebook and Instagram Posting tool using the OpenAI API. 

"""

class AI_Poster():
    def __init__(self): #initialize openAI API client
      self.apiKey = os.getenv("API_KEY")
      # print(self.apiKey)
      self.client = OpenAI(api_key=self.apiKey)    
      self.now = datetime.now().strftime("%m-%d-%Y")

if __name__ == "__main__":
    pass