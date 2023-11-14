# Basic guide to properly use SSH

SSH stands for [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) protocol and comes in several implementations.
The most common one and also the one installed by default in Ubuntu is [OpenSSH](https://www.openssh.com/).
The most important commands defined by OpenSSH are the following
 - `ssh`, to log in the remote machine
 - `scp`, to (securely) copy files to/from the remote machine
 - `ssh-agent`, the agent stores the keys
 - `ssh-add`, adds new keys to the agent
 - `ssh-keygen`, generates new keys

