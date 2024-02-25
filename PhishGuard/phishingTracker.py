import sys
import re 
from urllib.parse import urlparse


def email_phishing_tracker(email_content):
    is_malicious = False
    
    word_list = ["please", "link", "please click", "please provide", "please enter", "following link", "reset your password", "reset password", "credentials", "immediately", "hurry up", "hurry", "as early as possible", "as soon as possible"]
    
    # Word list check
    for words in word_list:
        if words in email_content.lower():
            is_malicious = True 
            return is_malicious
        
    # URL checks 
    urls_present = url_extractor(email_content)
    for each_url in urls_present:
        if not is_legitimate_url(each_url):
            is_malicious = True
            break
    
    return is_malicious


def url_extractor(email_content):
    url_pattern = re.compile(r'\b(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]')
    matches = url_pattern.findall(email_content)
    urls = []
    for match in matches:
        urls.append(match)
    return urls


def is_legitimate_url(url_link):
    parsed_url_components = urlparse(url_link)
    
    # Checking scheme of the URL (https, http, ftp)
    if parsed_url_components.scheme in ['http', 'ftp']:
        return False
    
    # Checking the domain and subdomains 
    if parsed_url_components.netloc.endswith((".net", ".org", ".com")):
        return True
    else:
        return False	


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py 'email_content'")
        sys.exit(1)

    email_content = sys.argv[1]

    if email_phishing_tracker(email_content):
        print("Phishing Warning ahead !!")
    else:
        print("Safe to move ahead !!")
