## Useful resource on starting git bash
  https://github.com/git-guides \
  https://www.atlassian.com/git/tutorials/git-bash \
  https://git-scm.com/docs \
  https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line 
  
  **! you first have to install git to your machine!**
  * For MacOS and Linux: Unix based commands are built-in
  * For Windows: use git bash prompt instead of Windows Prompt

## Basic commands
### Navigate folders
* `pwd`: present working directory; can check which dir git session is making changes to
* `ls`: lists all the files in the wd
* `cd`: change directories; can set a new wd to the GitHub folder
  + `cd ..` goes up one folder

### Clone/push to /pull from remote repositories
* `git clone YOUR_GITHUB_URL_GOES_HERE`
* `git add SUBDIRECTORY/YOUR_FILE_NAME`: stage files; do not make any changes
* `git commit -m "commit description"`: make changes to local repository
  + `git commit --amend`: instead of creating a new commit, staged changes will be added to the previous commit
* `git push -u origin master`: push to master branch
* `git pull`: download changes made from remote repository and merge with your file
