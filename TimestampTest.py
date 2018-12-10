from requests import get
from datetime import datetime

r = get(url="https://www.stackoverflow.com", headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"})

print(datetime.strptime((r.headers["Date"][:-4]), "%a, %d %b %Y %H:%M:%S"))
