import google
import math
import sys
import json
import urllib

def googlesearch(searchfor):
    qu = urllib.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % qu
    response = urllib.urlopen(url)
    results = response.read()
    results = json.loads(results)
    data = results['responseData']
    return data

args = sys.argv[1:]
m = 45000000000
if len(args) != 2:
    print "need two words as arguments"
    exit(0)
fx = int(googlesearch(args[0])['cursor']['estimatedResultCount'])
fy = int(googlesearch(args[1])['cursor']['estimatedResultCount'])
fxy = int(googlesearch(args[0]+" "+args[1])['cursor']['estimatedResultCount'])
ngdnumerator = max(math.log10(fx),math.log10(fy))-math.log10(fxy)
ngddenominator = math.log10(m)-min(math.log10(fx),math.log10(fy))
ngd = ngdnumerator/ngddenominator
print ngd
