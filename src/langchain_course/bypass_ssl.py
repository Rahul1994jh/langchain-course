import os
import ssl
import urllib3
import warnings

# 1. Clear environment variables before any clients boot up
os.environ['REQUESTS_CA_BUNDLE'] = ''
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['SSL_CERT_FILE'] = ''
os.environ["LANGSMITH_DISABLE_RUN_COMPRESSION"] = "true"  # Mutes background log warnings

# 2. Disable SSL warnings and certificate verification globally
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
ssl._create_default_https_context = ssl._create_unverified_context

# 3. Monkey patch requests library to strip SSL checks
import requests

original_request = requests.Session.request

def patched_request(self, method, url, **kwargs):
    kwargs['verify'] = False
    return original_request(self, method, url, **kwargs)

requests.Session.request = patched_request

original_get = requests.get
original_post = requests.post

def patched_get(*args, **kwargs):
    kwargs['verify'] = False
    return original_get(*args, **kwargs)

def patched_post(*args, **kwargs):
    kwargs['verify'] = False
    return original_post(*args, **kwargs)

requests.get = patched_get
requests.post = patched_post
