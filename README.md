# Geek-Text

### 1. Download repository on GitHub.com to our machine
git clone <Geek-Text repository link>

### 2. Change into the `repo` directory
cd Geek-Text

### 3. Geek-Text has two branches - master and development (all changes will be made here)
git branch -a

### 4. Checkout remote branch like development
git checkout development

### 5. Look at all your local branches and see the one you are working on with *
git branch

### 6. Create a new branch to store any new changes
git branch <branch-name>

### 7. Switch to that branch (line of development)
git checkout <branch-name>

### 8. Make changes and see them in VS Code 

### 9. Stage the changed files
git add file1.md file2.md

### 10. Take a snapshot of the staging area (anything that's been added)
git commit -m "my snapshot"

### 11. Push changes to github
git push --set-upstream origin my-branch

### 12. Pull all changes before pushing
git pull
