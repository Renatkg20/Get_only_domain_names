def domain_name(url):
  return url.split("//")[-1].split("www.")[-1].split(".")[0]
    

print(domain_name("https://google.us.com"))

with open("url.names.txt", "r") as file:
  
     for a, i in enumerate(file.readlines(), start = 1):
         print(a, domain_name(i).capitalize())
 
