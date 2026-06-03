import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print("\033[0;31mO site não está disponível.\033[m")
else:
    print("\033[0;30;42mO site está disponível!\033[m")
    print(site.read())