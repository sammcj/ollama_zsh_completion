import requests
from html.parser import HTMLParser

class ScrapeOllamaLibraries(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and any(attr[0] == 'href' for attr in attrs):
            href_value = [attr[1] for attr in attrs if attr[0] == 'href'][0]
            if '/library/' in href_value:
                processed_link = href_value.replace('/library/', '')
                self.links.append(processed_link)

url = "https://ollama.com/library"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    parser = ScrapeOllamaLibraries()
    parser.feed(html_content)
    result = '\n'.join(parser.links) 
    print(result)
else:
    print(f"Failed to fetch model list from ollama.com [HTTP Status {response.status_code}]")
