# Laksegate
Laksegate gruppen er gruppen der arbejder med laks, lever af laks, og spiser laks.

# Git work flow 

## Cloning repository
* Get invite from owner (jonas1012)
* Go to repository in Github and press <> Code
* Copy https://github.com/jonas1012/Laksegate.git
* Go to terminal in VS code: `git clone https://github.com/jonas1012/Laksegate.git`

## Updating repository with changes
* Make whatever changes.
* Check status of changes: `git status`
* Add all changes to be saved to staging: `git add .`
* Save changes with message: `git commit -m "message"`
* Create a new branch for changes: `git checkout -b test-branch`
* Push changes to location: `git push origin test-branch`
* Once pushed, go the branch and make a pull request

## Pulling updates from repository
* Go to repository: `cd path/to/repository`
* Go to main branch: `git checkout main`
* Check newest updates: `git fetch origin`
* Pull the changes: `git pull origin main` 


