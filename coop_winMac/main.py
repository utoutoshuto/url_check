import requests
from bs4 import BeautifulSoup

def check_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else Happened",err)
        return False
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        return False
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return False
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return False

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def main(url):
    links = get_links(url)
    for link in links:
        if check_link(link):
            print(f'Link is valid: {link}')
        else:
            print(f'Link is broken: {link}')

if __name__ == "__main__":
    main('https://yourwebsite.com')  # replace with your website
