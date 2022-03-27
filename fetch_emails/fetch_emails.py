# Script for 'fetch_emails' program in Python
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
The program takes as input an URL and prints the list of emails addresses contained in it.
"""

import re
import urllib.request

# The function 'emails_list' takes as input an URL and returns the list of emails addresses contained in it:
def emails_list(urlname):

  # Opens urlname and store its content, in utf-8 format, in the string data
  # Does so by passing a fake user agent to the website to avoid the possible error message:
  # 'urllib.error.HTTPError: HTTP Error 403: Forbidden'
  header = {'User-Agent': 'Chrome'}
  url = urllib.request.Request(url=urlname, headers=header)
  data = urllib.request.urlopen(url).read().decode('utf-8')

  # Finds in data the email-type strings including '(at)' or '@' and not finishing by 'html'
  # Discards possible repetitions with set() and orders the results with sorted()
  emails1 = re.findall(r'[\w.-]+\(at\)[\w.-]+\.(?!html)[a-zA-Z]+', data)
  emails2 = re.findall(r'[\w.-]+@[\w.-]+\.(?!html)[a-zA-Z]+', data)
  emails = emails1 + emails2
  return sorted(set(emails))

# The function 'main' takes as input an URL and returns the list of email addresses found in it:
def main():
  urlname = input("Enter URL where to look for email addresses: ")
  emails = emails_list(urlname)
  print('')
  if emails:
    print('The email addresses in', '"' + urlname + '"', 'are:\n')
    for email in emails:
      print('-', email)
  else:
    print('No email address found in', '"' + urlname + '".')

if __name__ == '__main__':
  main()
