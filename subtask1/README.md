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
