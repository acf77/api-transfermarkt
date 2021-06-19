import http.client

conn = http.client.HTTPSConnection("transfermarket.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "9ad361157cmshe2f75a0ffb08f0fp1c88aajsn9ea462f600d8",
    'x-rapidapi-host': "transfermarket.p.rapidapi.com"
    }

conn.request("GET", "/players/get-profile?id=74842", headers=headers)

res = conn.getresponse()
data = res.read()

decodedData = data.decode("utf-8")

with open('api-transfermarket-output.csv', 'w+') as csv:
    csv.write(decodedData)





