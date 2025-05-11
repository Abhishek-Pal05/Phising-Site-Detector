import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Suspicious top-level domains
suspicious_tlds = ['.xyz', '.top', '.club', '.buzz', '.tk', '.ml']

def check_url(url):
    results = {}

    # Normalize URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    # Check if domain is IP address
    results['IP Address Used'] = bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))

    # Check for @ symbol
    results['@ Symbol Present'] = '@' in url

    # Count of dots
    results['Dot Count'] = url.count('.')

    # Length of URL
    results['URL Length'] = len(url)
    results['Too Long'] = len(url) > 75

    # Suspicious TLD
    results['Suspicious TLD'] = any(tld in domain for tld in suspicious_tlds)

    # Hyphen presence
    results['Hyphen in Domain'] = '-' in domain

    # HTTPS check
    https_used = check_https(url)
    results['HTTPS Enabled'] = https_used if https_used is not None else "Site not reachable"

    return results

def check_https(url):
    if not url.startswith('http'):
        url = 'http://' + url

    try:
        response = requests.get(url, timeout=5)
        return response.url.startswith("https://")
    except requests.exceptions.SSLError:
        return False
    except requests.exceptions.RequestException:
        return None

def analyze_html_content(url):
    suspicious_keywords = ['password', 'credit card', 'ssn', 'verify', 'login', 'confirm']
    keyword_found = []

    if not url.startswith('http'):
        url = 'http://' + url

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for form elements
        forms = soup.find_all('form')
        form_count = len(forms)

        # Check for suspicious keywords in text
        text = soup.get_text().lower()
        for keyword in suspicious_keywords:
            if keyword in text:
                keyword_found.append(keyword)

        return {
            'Forms Detected': form_count,
            'Suspicious Keywords Found': keyword_found
        }

    except Exception as e:
        return {
            'Forms Detected': 'Error fetching page',
            'Suspicious Keywords Found': str(e)
        }

# --- MAIN PROGRAM ---

if __name__ == "__main__":
    url = input("🔗 Enter a URL to analyze: ")

    print("\n🔍 URL Structure & SSL Check:\n")
    result = check_url(url)
    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n🧬 HTML Analysis:\n")
    html_results = analyze_html_content(url)
    for key, value in html_results.items():
        print(f"{key}: {value}")
