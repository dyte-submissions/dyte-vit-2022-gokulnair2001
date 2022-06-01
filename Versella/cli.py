import click
import csv
import os
import json
import sys
import requests
import pyfiglet
from github import Github
from urllib.request import urlopen
from urllib.parse import urlparse
from packaging import version
from pathlib import Path

# Global Lists to store results
finalResults = ["version_satisfied"]
fetchedVersions = ["version"]
prList = ["update_pr"]
forkStatus = ['fork_status']

# Version Check and Updater Section
@click.command()
@click.option('--input', '-i', help='File path input', required=True, prompt="Provide input file name\n")
@click.option('--update/--noUpdate', '-u/-nu', help='Updation argument', required=False, default=False)
@click.option('--token', '-t', required=False)
@click.argument('param')
def cli(update, input, param, token):
    '''
    Takes file location and version abstract as parameter
    '''
    print(pyfiglet.figlet_format("Versella"))

    with open(os.path.join(input), 'rU') as file:
        target_doc = csv.reader(file)
        next(target_doc)
        for line in target_doc:
            a = urlparse(line[1])
            getAxios(a.path, param, update, token)
    
    if update:
        sys.stdout.write("Checking for version satisfaction and forking the repo for update........")
    else:
        sys.stdout.write("Version check.....")

    checkVersionSatisfaction(input, not update)

# Get Axios no from Github Repo
def getAxios(url, query, updateReq, token):
   response = urlopen("https://raw.githubusercontent.com"+url+"/main/package.json")
   data_json = json.loads(response.read())
   word = query.split('@')
   rawData = data_json["dependencies"][word[0]]
   finalVersion = rawData.replace('^','')
   fetchedVersions.append(finalVersion)
   if version.parse(word[1]) > version.parse(finalVersion):
       finalResults.append("false")
       if updateReq:
           prList.append("Check Github GUI to edit and create PR")
           forkTheRepo(url, token)
   else:
       finalResults.append("true")
       if updateReq:
           prList.append("NA")
           forkStatus.append("NA")


# Method to update file with version satisfaction results
def checkVersionSatisfaction(location, updateReq):
    with open(os.path.join(location), 'r') as csvinput:
        with open(os.path.join(getNewLocation(location)), 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            count = 0
            for row in csv.reader(csvinput):
                if updateReq:
                    writer.writerow(row+[fetchedVersions[count]]+[finalResults[count].lower()])
                else:
                   writer.writerow(row+[fetchedVersions[count]]+[finalResults[count].lower()]+[forkStatus[count]]+[prList[count]])
                count += 1
        sys.stdout.write('\nVersella⚡️ : Check Versella_Results.csv at the same input location to get the results')

# Method to generate Reslut file path
def getNewLocation(existingPath, name="Versella_Results.csv"):
    path = Path(existingPath)
    newLocation = path.with_name(name)
    return newLocation


# Method to create fork repo which have lower versions 
def forkTheRepo(directoryPath, token):
    path = directoryPath.split('/')
    repoName = path[2]
    owner = path[1]

    print("hhhhhkkk "+ token)
    headers = {
        "Authorization": "token {0}".format(token),
        "Content-Type": "application/json"}   

    r = requests.post("https://api.github.com/repos/"+owner+"/"+repoName+"/forks", headers= headers)

    if not r.ok:
        print("Request Failed: {0}".format(r.text))
        forkStatus.append("Failed")
    else:
        forkStatus.append("Successful")


@click.command()
@click.option('--username','-u', required=True, prompt='User name')
@click.option('--token', '-t', required=True, prompt='Auth token')
@click.option('--location', '-l', help='File location', required=True, prompt="Enter the file location\n")
def find(username, token, location):
    '''
    Provides user a file with all their Repositiories with its languages
    '''
    print(pyfiglet.figlet_format('VersellaX'))
    print("Working⏳......")

    g = Github(username, token)
    repoName = ["Name"]
    repoLang = ["Language"]
    for repo in g.get_user().get_repos():
        repoName.append(repo.name)
        repoLang.append(repo.language)
    with open(os.path.join(getNewLocation(location, 'Repository_Details.csv')), 'w') as csvoutput:
        count = 0
        for _ in repoLang:
            writer = csv.writer(csvoutput)
            writer.writerow([repoName[count]] + [repoLang[count]])
            count += 1