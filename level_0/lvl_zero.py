from requests import post

url = 'http://158.69.76.135/level0.php'

# POST action

failures = 0
success = 0

for i in range(1024):
    r = post(url, data={'id': '1531', 'holdthedoor': 'Submit'})
    if r.status_code != 200:
        failures += 1
    else:
        success += 1

print("Successes → {}\nFailures → {}".format(success, failures))
