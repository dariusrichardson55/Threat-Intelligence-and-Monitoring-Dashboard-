import requests
import pandas as pd
import json
from datetime import datetime


# API Key and Endpoint
API_KEY = 'c7eb7d939ebb4483a221354cdc41f55804d0c1b04493c9f4fa008ceeba7bc9cc'
OTX_URL = 'https://otx.alienvault.com/api/v1/pulses/subscribed'


# Headers for API Authorization
HEADERS = {
    'X-OTX-API-KEY': API_KEY
}

# Fetch Threat Data from AlienVault
def fetch_threat_data():
    response = requests.get(OTX_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print("Error fetching data:", response.status_code)
        return None

# Process and Save Data to CSV
def process_threat_data(data):
    threat_list = []
    for item in data:
        for indicator in item.get('indicators', []):
            threat_list.append({
                'Pulse_Name': item['name'],
                'Indicator': indicator['indicator'],
                'Type': indicator['type'],
                'Created': item['created'],
                'TLP': item['tlp']
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(threat_list)
    df.to_csv('threat_intelligence.csv', index=False)
    print(f"Saved {len(df)} indicators to threat_intelligence.csv")

if __name__ == '__main__':
    print("Fetching Threat Data from AlienVault OTX...")
    threat_data = fetch_threat_data()
    if threat_data:
        process_threat_data(threat_data)
