# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:06:32 2024

@author: jcp
"""

def scrape_presidential_speech(speech_id):
    import requests
    from bs4 import BeautifulSoup

    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    
    base_url = "https://www.pa.go.kr/research/contents/speech/index.jsp?spMode=view&catid=c_pa02062&artid={}"
    url = base_url.format(speech_id)
    
    # Create a session with retry logic
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        r = session.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching speech {speech_id}: {e}")
        return ""  # Return empty string if there's an error

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        president_text = soup.find("td", class_="content")
        if president_text:
            return president_text.get_text(strip=True)
        else:
            return ""  # If speech is not found, return empty string
    else:
        print(f"Error fetching speech {speech_id}: Status code {r.status_code}")
        return ""  # If page cannot be fetched, return empty string

def save_to_excel(speeches, filename="speeches.xlsx"):
    import pandas as pd
    df = pd.DataFrame({"연설문": speeches})
    df.to_excel(filename, index=False)