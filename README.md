# Geek-Text

### Download repository on GitHub.com to our machine
git clone <Geek-Text repository link>

### Change into the `repo` directory
cd Geek-Text

### Geek-Text has two branches - master and development (all changes will be made here)
git branch -a

### Checkout remote branch like development
git checkout development

### Look at all your local branches and see the one you are working on with *
git branch

### Create a new branch to store any new changes
git branch <branch-name>

### Switch to that branch (line of development)
git checkout <branch-name>

### Make changes

### Stage the changed files
git add file1.md file2.md

### Take a snapshot of the staging area (anything that's been added)
git commit -m "my snapshot"

### Push changes to github
git push --set-upstream origin my-branch
