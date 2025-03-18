import pathlib
import textwrap

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

import os
api_key1 = os.environ.get("API_KEY")
api_key2 = os.environ.get("RAPID_API_KEY")



global final
final = []
text = ''
def get_text(problem):
    global text 
    text = problem


    genai.configure(api_key = api_key1)

    model = genai.GenerativeModel('gemini-pro')
    text1 = ' Give me only job names with no description'

    response = model.generate_content(text + text1,stream = True)
   

    output = []
    l = []
    l_new = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l_new1 = []
    for chunk in response:
        output = chunk.text
        l.extend(output.split('*'))

    l_new = [s.strip('\n') for s in l]
    l1 = [s.strip('\n*') for s in l_new]
    l2 = [s.strip('-') for s in l1]
    l3 = [s.strip('-\n') for s in l2]
    l4 = [s.split("\n-") for s in l3]



    for i in l4:
        if(i == ''):
            continue
        else: l_new1.extend(i) 

    # final = []
    import requests

    url = "https://jobs-api14.p.rapidapi.com/list"

    for i in l_new1:
        querystring = {"query":i,"location":"India","distance":"10","language":"en_GB","remoteOnly":"false","datePosted":"month","employmentTypes":"fulltime;parttime;intern;contractor","index":"0"}

        headers = {
            "X-RapidAPI-Key": api_key2,
            "X-RapidAPI-Host": "jobs-api14.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        
        
        output = response.json()
        
        
        for i in range(len(output['jobs'])):
            job = []
            job.append(output['jobs'][i]['title'])
            job.append(output['jobs'][i]['company'])
            
            job.append(output['jobs'][i]['location'])
            job.append(output['jobs'][i]['employmentType'])
           
            final.append(job)

def send():
    return final   