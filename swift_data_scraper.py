import requests
from bs4 import BeautifulSoup
import json

class SwiftDataScraper:
    BASE_URL = "https://www.theswiftcodes.com/swift-code-checker/"
    HEADERS = {}

    def __init__(self):
        self.label_mapping = {
            "Bank / Institution": "bank",
            "Branch Name": "branch",
            "Address": "address",
            "City": "city",
            "Postcode": "postcode",
            "Country": "country",
            "Connection": "connection"
        }

        self.desired_fields = set(self.label_mapping.keys())

    def _get_html(self, swift_code):
        payload = {'swift': swift_code}
        try:
            response = requests.post(self.BASE_URL, headers=self.HEADERS, data=payload)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:
            print(f'An error occurred: {err}')
            return None
        else:
            return response.text

    def _extract_table_data(self, table):
        data = {}
        rows = table.find_all('tr')
        for row in rows:
            key = row.find('th').text.strip()
            if key in self.desired_fields:
                cols = row.find_all('td')
                if cols:
                    value = cols[0].text.strip()
                    data[self.label_mapping[key]] = value
        return data

    def _parse_html(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find("table", {"class": "swift-detail"})
            data = self._extract_table_data(table)
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            data = {}
        return data

    def get_data(self, swift_code):
        html = self._get_html(swift_code)
        if html is not None:
            return self._parse_html(html)
        else:
            return None
