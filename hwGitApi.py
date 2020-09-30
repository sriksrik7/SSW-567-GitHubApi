import requests
import json

def getUserGitHubData(userID):
    # Eg: https://api.github.com/users/<ID>/repos
    url = f"https://api.github.com/users/{userID}/repos"
    response = requests.get(url)
    statusCode = response.status_code

    # Return Forbidden error if status code is 403
    if statusCode == 403:
        return "Forbidden"

    # Return None if status code is not equal to 200
    if statusCode != 200:
        return None

    # Fetch all keyWord's with name in json
    detailsList = []
    for keyWord in response.json():
        detailsList.append(keyWord['name'])

    # Fetch number of commits in each repo
    listofCommits = []
    for repo in detailsList:
        # Eg:     # Eg: https://api.github.com/repos/<ID>/<REPO>/commits
        url = f"https://api.github.com/repos/{userID}/{repo}/commits"
        number = requests.get(url)
        number = len((number.json()))
        listofCommits.append(number)

    # List out all repo details in a list
    listOutput = []
    for name, commits in zip(detailsList, listofCommits):
        result = f"Repository: {name} has {commits} commits"
        listOutput.append(result)

    # return the processed list with repo and commit details
    return listOutput

if __name__ == "__main__":
    userID = input("Please enter GitHub userID: ")
    repoDetails = getUserGitHubData(userID)
    print(repoDetails)
