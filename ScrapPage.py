import urllib
import urllib.request
from io import BytesIO
import gzip
import re

def GetPageContent(url):
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0")
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Accept-Language", "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3")
        response = urllib.request.urlopen(req)
        r = None
        if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            r = f.read()
        else:
            r = response.read()
        return r
    except:
        return ""


def WriteToFile(htmlContent, filePath):
    if (type(htmlContent) is str):
        print("yes")
        with open(filePath, "w") as file:
            file.write(htmlContent)
    if  (type(htmlContent) is bytes):
        print("yes byte")
        with open(filePath, "wb") as file:
            file.write(htmlContent)
    return("Done")


def url_Formattage(url):
    regex_url=re.findall(r'openjur' , url)
    regex_adomy=re.findall(r'admody' , url)
    regex_caselaw=re.findall(r'caselaw' , url)
    #if ((regex_url) or (regex_adomy) or (regex_caselaw) ):
    print("yes")
    nouveau = url.replace("https://translate.google.com/translate?hl=fr&sl=de&u=" , '')
    nouveau=nouveau.replace("https://translate.google.com/translate?hl=fr&sl=en&u=" , '')
    nouveau=nouveau.replace("&prev=search&pto=aue" , '')
    return(nouveau)
    #else:
       #return(url)
    