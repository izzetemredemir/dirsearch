import requests

headers = {
    'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

wordlist = 'dict.txt'

def dirsearch(url):
    f = open(wordlist, "r")
    for dict in f:

        scan_url = url + dict.strip()
        #print url
        res = requests.get(url=scan_url,headers=headers,timeout=2)
        status = res.status_code
        if status ==200 :
            print ("[%d]\t %s" %(status,scan_url))
    f.close()

dirsearch("http://www.haber18.com/")



