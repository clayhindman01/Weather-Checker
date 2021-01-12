#! Python 3.9.1
# Script that will pull the temperature and percipitation chance off bing.

#THIS STILL NEEDS ALOT OF WORK  

import requests
import sys
import bs4

class Weather():

    def __init__(self):
        pass

    # Function that calls the requests library and gets the ulr for the zip code.
    def get_page(self):
        zip_code = ''.join(sys.argv[1:])
        url = "https://weather.com/weather/today/l/" + zip_code
        response = requests.get(url, headers = {
            'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        })

        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        weather = soup.find('span', {'class':'CurrentConditions--tempValue--3KcTQ'})
        print(weather.text)

weather = Weather()
weather.get_page()