import requests

proxy_url = 'https://rfp4ucx.xyz/link/ult2p4p5NFNuL1zu?clash=1:7890'

# Make sure to replace 'your-proxy-server' and 'port' with the actual proxy server address and port number.

# Example request with HTTP proxy
response = requests.get('http://codeforces.com/apiHelp/objects#Problem', proxies={'http': proxy_url})

# You can also use the same proxy for HTTPS requests if your proxy server supports it,
# but in your case, since it doesn't, you shouldn't specify an HTTPS proxy.
# response = requests.get('https://example.com', proxies={'http': proxy_url})

print(response.status_code)
