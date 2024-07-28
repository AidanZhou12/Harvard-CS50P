import requests
import sys
import json

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()
    q = o["bpi"]
    e = q["USD"]
    i = e["rate"]
    i = i.replace(",", "")
    i = str(i)
    if len(sys.argv) >= 2:
        amount = float(i) * float(sys.argv[1])
        print(f"${amount:,.4f}")
    else:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit("Command-line argument is not a number")
except ValueError:
    sys.exit("Command-line argument is not a number")
