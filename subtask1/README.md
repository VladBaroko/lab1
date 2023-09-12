# Tasks: Mastering Git

Tasks on knowledge and skills of working with Git (basic commands)

## Subtask 1

1. Initialize a repository

1.1 Create a new directory.

1.2 Initialize a new repository in the created directory.

```bash
$ mkdir lab1
```
```bash
$ cd lab1
```
```bash
$ git init
```

## Subtask 2

2. Create a project with an empty file README.md (or README.rst if you prefer)

2.1 Create a project directory.

2.2 Add README.md

2.3 Commit all changes.

```bash
$ mkdir subtask1 
```
```bash
$ cd subtask1/ 
```
```bash
$ touch README.md
```
```bash
$ git config --global user.name "your_username"
```
```bash
$ git config --global user.email "your_email"
```
```bash
$ git remote add origin git@github.com:VladBaroko/lab1.git
```
```bash
$ ssh-keygen -t ed25519 -C "your@email.com"
```
```bash
$ ssh-add ~/.ssh/id_ed25519
```
```bash
$ cat ~/.ssh/id_ed25519.pub

# Copy the entire output.

# Go to GitHub.

# In the top right corner of any page, click on your profile photo, then click Settings.

# In the user settings sidebar, click SSH and GPG keys.

# Click New SSH key.

# Paste your key into the "Key" field, provide a title, and hit Add SSH key.
```
```bash
$ git add .
```
```bash
$ git commit -m "Init"
```
```bash
$ git push origin main
```

## Subtask 3

3. Create a new branch and modify README.md

3.1 Create a new branch named first_branch and switch to it.

3.2 Modify the README.md: add a list of console commands to solve the 1st subtask.

3.3 Display the state of the working directory and the staging area.

3.4 Commit all changes.

```bash
$ git checkout -b first_branch
```
```bash
$ nano README.md

# one of the best graphical editor 
# Here you can add a list of console commands to solve the 1st subtask.
```
```bash
$ git worktree list
D:/unik/3kurs/PIPka/lab1  c4a4957 [first_branch]
```
```bash
$ git status
On branch first_branch
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

```
```bash
$ git add .

```
```bash
$ git commit -m "modified README.md"
```
```bash
$ git push origin first_branch

```

## Subtask 4

4. Switch back to the master branch and modify README.md

4.1 Switch back to the master branch.

4.2 Modify the README.md: add a list of console commands to solve the 2nd subtask.

4.3 Commit all changes.

4.4 Display the project history

```bash
$ git checkout main

```
```bash
$ nano README.md

```
```bash
$ git add .

```
```bash
$ git commit -m "modified README.md in /lab1/main/"

```
```bash
$ git push origin main

```
```bash
$ git log --all
commit 990114ebe8b003e51f681db1fc4cb6abb573c989 (HEAD -> main, origin/main)
Author: VladBaroko <dk12.brovko@lll.kpi.ua>
Date:   Tue Sep 12 14:41:33 2023 +0300

    modified README.md in /lab1/main/

commit 42ab2245dbe7ad32210357e140ccc44a3287216d (origin/first_branch, first_branch)
Author: VladBaroko <dk12.brovko@lll.kpi.ua>
Date:   Tue Sep 12 14:29:53 2023 +0300

    modified README.md

commit c4a4957f6b6b6d3ded2ef46608b3c639f4dc380b
Author: VladBaroko <dk12.brovko@lll.kpi.ua>
Date:   Tue Sep 12 13:40:03 2023 +0300

    Init

```

## Project history

```bash
$ git log --oneline --decorate
47436e5 (HEAD -> main, origin/main) modified README.md
990114e modified README.md in /lab1/main/
42ab224 (origin/first_branch, first_branch) modified README.md
c4a4957 Init
```
