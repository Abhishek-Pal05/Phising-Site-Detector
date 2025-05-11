#  URL & Phishing Detector

A Python-based tool to analyze and evaluate a URL for potential phishing threats and suspicious behavior. This script performs structural checks on the URL, verifies HTTPS usage, and analyzes the HTML content for phishing indicators like login forms and sensitive keywords.

---

##  Features

- ✅ Detects usage of IP address instead of domain
- ✅ Checks for presence of `@` symbol (often used in phishing)
- ✅ Counts dots and evaluates if the URL is abnormally long
- ✅ Flags suspicious top-level domains (TLDs) like `.xyz`, `.tk`, `.club`
- ✅ Detects hyphens in domain (often used to spoof legitimate websites)
- ✅ Verifies if HTTPS is enabled
- ✅ Analyzes HTML content for:
  - Forms (`<form>` tags)
  - Phishing-related keywords like `password`, `credit card`, `login`, etc.

---

##  Requirements

- Python 3.6+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


## How It Works
1. The script takes a user-input URL.
2. Performs URL structure checks (length, TLD, hyphens, IP usage, @ symbol, etc.).
3. Checks if HTTPS is used or not.
4. Fetches and parses the HTML content of the URL.
5. Detects any <form> elements and looks for suspicious keywords like password, login, credit card, etc.
6. Prints the results in a readable format for easy inspection.

## Contributing
Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

## Disclaimer
This tool is for educational and research purposes only. It is not a substitute for professional security solutions. Always verify URLs through official security resources.

