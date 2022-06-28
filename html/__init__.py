import check50
from bs4 import BeautifulSoup

@check50.check()
def exists():
    """main.py exists."""
    check50.exists("index.html")

def parse_html(file):
  with open(file) as f:
    #read File
    content = f.read()
    #parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    #print Title tag
    print(soup.title)

@check50.check(exists)
def check_links():
  if len(soup.find_all('a')) < 2:
    raise check50.Mismatch("Expected at least 2 hyperlinks", f"Actual found {len(soup.find_all('a'))} hyperlink", help=help)
 
