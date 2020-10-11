print("WEB INSPECTOR")
print("POWERED BY-TECHNOLAB")
print("DEVELOPED BY - R.K MUHAMMAD AMHER")


print("ALL RIGHT RESERVED")

print("-----------------------                    ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |          ")
print("           |                     |___________           ")


print("TECHNOLAB PRODUCTION")






















import requests
x = input("enter the url:")

url = x

response = requests.get(url=url)
print("these are response methods")
print(dir(response))

print("CONTENT:")
print(response.content)

print("HEADERS:")
print(response.headers)

print("URL:")
print(response.url)

print("DOC:")
print(response.__doc__)

print("APPARENT ENCODING:")
print(response.apparent_encoding)

print("COOKIES:")
print(response.cookies)

print("ELAPSED:")
print(response.elapsed)

print("HISTORY")
print(response.history)

print("LINKS:")
print(response.links)


print("RAW:")
print(response.raw)

print("ANNOTIONS:")
print(response.__annotations__)

print("STATUS CODE")
print(response.status_code)

print("REASON:")
print(response.reason)

print("TEXT")
print(response.text)


print("PERMANENT REDIRECT")
print(response.is_permanent_redirect)


print("IS REDIRECT:")
print(response.is_redirect)

print("LINKS:")
print(response.links)

print("ENCODING:")
print(response.encoding)

print("CLASS:")
print(response.__class__)

print("module")
print(response.__module__)

print("REQUEST HEADERS")
print(response.request.headers)












