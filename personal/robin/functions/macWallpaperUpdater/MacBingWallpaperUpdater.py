#-*-coding:utf-8 -*-
import os
import pycurl
import re
import io

# get html source
html_source = io.StringIO.StringIO()
url = 'https://www.bing.com'
c = pycurl.Curl()
c.setopt_string(c.URL, url)
c.setopt(c.WRITEDATA, html_source)
c.perform()
c.close()

# get image path
body = html_source.getvalue()
img_urls = re.search('g_img=\{url:\s\"(.*)\",id.*', body)
img_path = img_urls.group(1)
img_name = img_path[img_path.rfind('/') + 1:]

# download image to Pictures
download_url = 'www.bing.com' + img_path
local_path = os.environ['HOME'] + '/Pictures/' + img_name
print(local_path)
with open(local_path, 'w') as pic:
    c = pycurl.Curl()
    c.setopt(c.URL, download_url)
    c.setopt(c.WRITEDATA, pic)
    c.perform()
    c.close()

# change wall paper
command = 'osascript -e \"tell application \\\"Finder\\\" to set desktop picture to POSIX file \\\"%s\\\"\"' % local_path
print(command)
os.system(command)