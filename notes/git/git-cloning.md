# Cloning a git repo

Github offers 2 protocols to share a repo:

1. HTTPS: these repos start with `https://` followed by the repo URL
2. SSH: these starts with `git@github.com:` followed by the repo name

## 1. HTTPS

HTTPS just requires your usual github username and password.
Upon requesting a clone, push or fetch, a window will prompt to insert the your credential.

## 2. SSH

SSH requires the user to set up a public key for github.
This can be done in the user/settings/SSH and GPG keys menu on github:
- first generate a local private/public key for the local machine
- upload the **public** key to github
- enable it

NOTE: the private/public key must be protected by passphrase.
Upon requesting a clone, push or fetch, a window will pop asking for the passphrase.

## COMMANDS

To copy a repo on a your local machine:
1. move to a folder of choice
2. for HTTPS type:
  ```
  git clone https://github.com/t3n0/MostAmazingMakefile.git Pollo
  ```
3. for SSH type:
  ```
  git clone git@github.com:t3n0/MostAmazingMakefile.git Pollo
  ```
This will create a folder called `Pollo` containing the entire repo (all the .git files, not just the last version!).

NOTE: the folder name `Pollo` is optional, default is the repo name.
