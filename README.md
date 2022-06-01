# Versella⚡️
Versella is a Python based **CLI** used to do version check on various types of repositories and update them if version is lower.

## How to Install?
* Installing Versella is realy easy and simple, just folow three steps and you are ready to use **Versella**
1. Clone/Download the repo
2. Cd into the repo through the terinal
3. Then write ``` pip3 install --editable .```
4. You are ready to use **Versella**, go through the Usage rules to understand the CLI tool properly.

## How to use?
Versella majorly have three main features right now

1. Version Check
* The tool checks the versions of all the repo given to it in a file and denotes which repo is in lower version an which is in higher.
```python
Versella -i {location} {abstract}
```
#### Example
```python
Versella -i /Users/gokul/Desktop/Untitled.csv axios@0.23.0
```
* ```-i``` denotes the input option for versella 
* Here the location must be of the file which consists of the repo details
* The input file must have two headers which is ```name``` & ```repo```
* The abstract section consists of the current axios for which version is to be checked

2. Update Repos
* The tool provides a feature where all the rep which are under given version number will be forked to the users account, such that the user can directly make changes from the GitHub GUI app and create a PR

```python
Versella -u -i {location} {abstract} -t {token}
```

#### Example
```python
Versella -u -i /Users/gokul/Desktop/Untitled.csv axios@0.23.0 -t xxxxxxxxxxxxxxxxxxxxxxxxx
```
* Location and abstract is the same as mentioned above
* Here ```-u``` denotes the updation requirement to versella
* On using ```-u``` Versella will fork the Repositories which are in lower versions to users account such that user can directly make changes through GitHub GUI and create a PR
* ```-t``` inorder to fork the repo **Versella** needs to identify the foking user, thus the user need to pass the ```OAuth``` token og GitHub to versella
#### [OAuth?](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
* Go to Github GUI and then: ```Settings > Developer Settings > Personal Token > Generate Token```

3. Get Repositories 
* Versell have a subordinatory tool system called ```VersellaX``` which is used to automate GitHub Actions.
* Right now **VersellaX** ca be used to fetch all the repos of user with various details regarding it.
* This feature helps user to find various forms of repo on which updates are to be made.

```python
Versellax -u {username} -t {token} -l {example location}
```
#### Example
```python
Versellax -u gokulnair2001 -t xxxxxxxxxxxxxxxxx -l /Users/gokul/Desktop/Untitled.csv
```
* ```-u``` denotes the username of the user
* ```-t``` denotes the user OAuth token
* ```-l``` example location for versella to save the results

## Snapshots
1. Version Check

<img width="815" alt="1" src="https://user-images.githubusercontent.com/56252259/171429350-be8ae5d8-53af-45b7-9607-4cc16c0fe444.png">

2. Update

<img width="815" alt="2" src="https://user-images.githubusercontent.com/56252259/171430348-eb48d2a8-ffcb-468a-bc20-eee1c3ca058f.png">

3. Get Repositories

<img width="815" alt="3" src="https://user-images.githubusercontent.com/56252259/171431581-c80b0b9a-e3d3-4bbb-af56-5d42d06e5583.png">



## VersellaX
## Warnings
## How to contribute?
## Developer
