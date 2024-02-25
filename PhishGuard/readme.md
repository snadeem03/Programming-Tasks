## Problem Statement : Phishing Detection in Email Content

### Background:
 Phishing attacks are deceptive attempts by malicious actors to acquire sensitive information, such as usernames, passwords, and credit card details, by disguising as trustworthy entities in electronic communications. Emails containing suspicious links, urgent requests, or misleading content are common tactics employed in phishing campaigns.

### Objective:
 Develop a Python script to detect potential phishing emails by analyzing the content for specific keywords and verifying the legitimacy of embedded URLs.


### Requirements:
 
 * Keyword analysis : Identify and flag emails containing suspicious keywords/phrases commonly associated with phishing attempts.Keywords to be checked include phrases like "please", "link", "reset password", "credentials", "immediately", etc.

 * URL verification : Extract URLs embedded within the email content.Evaluate the legitimacy
   of each URL based on the following criteria:

  * Scheme (e.g., HTTP, FTP) - Legitimate URLs should use HTTPS.
  * Domain and subdomains - Legitimate domains should typically end with ".net", ".org", com".

### Functionality:
 1. Email Content analysis : 
  * The script should analyze the provided email content for suspicious keywords from a predefined list.
  * If any of the keywords are found, mark the email as potentially malicious.

 2. URL Extraction:
  * Extract URLs present within the email content using regular expression matching.
  * Store the extracted URLs for further verification.

 3. URL Legitimacy checks:
  * Verify each extracted URL's legitimacy by examining its scheme and domain/subdomains.
  * Flag URLs that do not meet the specified criteria as potentially malicious.

 4. Output:
  * Display a warning message if the script detects potential phishing indicators in the email content or URLs.
  * Otherwise, indicate that the email appears to be safe.

### Implementation:
 * Utilize Python libraries such as re for regular expression matching and urllib.parse for URL parsing.
 * Define functions for keyword analysis, URL extraction, and URL legitimacy checks to modularize the code.
 * Implement a main execution block to demonstrate the script's functionality using sample email content.

### Sample Output:
 * If the script detects suspicious keywords or illegitimate URLs in the provided email content, it should display a warning message indicating potential phishing activity.
 * otherwise, it should display a message confirming that the email appears to be safe to proceed.