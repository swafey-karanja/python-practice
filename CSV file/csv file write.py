from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1649643937&period2=1681179937&interval=1d&events=history&includeAdjustedClose=true'

def download_csc(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'file.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + '\n')
    fx.close()


download_csc(goog_url)
