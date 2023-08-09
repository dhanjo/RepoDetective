import requests
from datetime import date
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings()
print("\n")
print("[+] Scanning for public repositories...")
print("\n")
file_json = "Json_Data_"+date.today().strftime('%m_%d_%Y')+".json"

headers = {"Authorization": "Bearer "}


url = "http://api.github.com/orgs/{organization}/repos"


response = requests.get(url, headers=headers, verify=False)


#requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Check the response status code
if response.status_code != 200:
    raise Exception("Failed to fetch repositories: {}".format(response.content))

# Parse the JSON response
repos = response.json()

with open(file_json, "w") as j:
        j.write(str(repos))

# Handle pagination
while "next" in response.links:
    response = requests.get(response.links["next"]["url"], headers=headers, verify=False)
    repos += response.json()

# Filter repositories by private ones
public_repos = [repo for repo in repos if not repo["private"]]

if public_repos == []:
        print("[+] No Public Repository Discovered")

else:
        print("[+] Following are the Public Repos")
        print("\n")
# Print the repositories
        for repo in public_repos:
                print("- " + repo["html_url"])
