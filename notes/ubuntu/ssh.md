# Basic guide to SSH

SSH stands for [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) protocol and comes in several implementations.
The most common one and also the one installed by default in Ubuntu is [OpenSSH](https://www.openssh.com/).
The most important commands defined by OpenSSH are the following
 - `ssh` to log in the remote machine
 - `scp` to (securely) copy files to/from the remote machine
 - `ssh-agent` the agent stores the keys
 - `ssh-add` adds new keys to the agent
 - `ssh-keygen` generates new keys

## Generate new keys

- use `key-gen`
- algorithm flags
- comment flag
- naming convention for keys
- passphrase

## Add key to agent

- run agent in background
- `ssh-add` to add key
- change passphrase

## Best practise to store multiple keys

Have a `.ssh/config` file containing 

```bash
# Some comment on name1
Host friendly-name1
    HostName       long.and.cumbersome.server.name1
    IdentityFile   ~/.ssh/private_ssh_file1
    User           username-on-remote-machine1

# Some comment on name2
Host friendly-name2
    HostName       long.and.cumbersome.server.name2
    IdentityFile   ~/.ssh/private_ssh_file2
    User           username-on-remote-machine2
```

Then use e.g. `ssh friendly-name1` to log in into the first machine.  
This is my setup for aspire and github:

```bash
# Aspire2A NSCC super computing
Host aspire
    HostName aspire2antu.nscc.sg
    IdentityFile ~/.ssh/id_rsa_aspire
    User <my username>

# GITHUB
Host github.com
   HostName github.com
   PreferredAuthentications publickey
   IdentityFile ~/.ssh/id_rsa_github
```

## Tests and checks

- `ls -al ~/.ssh`
- `ssh -T friendly-name1`

