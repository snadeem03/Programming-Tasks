# checking for phishing

import re 
from urllib.parse import urlparse




#returns true if the email seems to be okay , else return false 
def email_phishing_tracker(email_content):
    is_malicious=False
    
    word_list=["please","link","please click","please provide","please enter","following link","reset your password","reset password","credentials","immediately","hurry up","hurry","as early as possible","as soon as possible"]
    
    # word list check
    for words in word_list:
        if words in email_content.lower():
            is_malicious=True 
            return is_malicious
        
        
    # url checks 
    urls_present=url_extractor(email_content)
    
    for each_url in urls_present :
        if is_legitimate_url(each_url)==False:
            is_malicious=True
            break
    
    return is_malicious
        
        
    

#returns the urls present inside the email-content
def url_extractor(email_content):
    url_pattern = re.compile(r'\b(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]')

    matches = url_pattern.findall(email_content)
    
    urls = []
    for match in matches :
        urls.append(match)
    
    return urls
        
    
    
            
# returns true if the email seems to be legitimate else false
def is_legitimate_url(url_link):
    
    legitimate_url=True
    parsed_url_components=urlparse(url_link)
    
    # checking scheme of the url (https,http,ftp)
    if parsed_url_components.scheme=='http' or parsed_url_components.scheme=='ftp':
        legitimate_url=False
        return legitimate_url
    
    # checking the domain and subdomains 
    if parsed_url_components.netloc.endswith((".net",".org",".com")):
        legitimate_url=True
    else :
        legitimate_url=False
        return legitimate_url	
    
    
    return legitimate_url
        
    

if __name__=='__main__':
    
    email_content="""
Dear Customer,

Your account has been compromised. Please click on the following link to reset your password immediately: 
https://fake-phishing-site.com/reset-password

Thank you,
Legitimate Bank
"""

if (email_phishing_tracker(email_content))==True :
    print("Phishing Warning ahead !!")
else :
    print("Safe to move ahead !!")


    