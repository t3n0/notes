# INTRO

git is a distributed version control system (DVCS)
distributed because each user have the entire repository locally on their machine

git stores snapshots of all files
git does not store deltas (differences) of modified files (like other VCS)
this stream of snapshots is at the heart of git branching system
everything is saved locally

every file in a git repository has THREE STATES
 - modified
 - staged
 - committed
the ususal git work flow goes like this:
 - you start a project, a .git directory is created (git clone, git init)
 - you edit some files (modified state)
 - you select some of those modified files to be staged (stage state)
 - you do a commit, git stores a new snapshot in your .git directory (commited state)

--------------------------------------------------------------------------------
CONFIGURATION
--------------------------------------------------------------------------------

After installing git, you should setup the congig file.
This should be done only once on every machine (you can still amend the config later)
The commad is

	$ git config <environment>
	
There are three environments:
           --system, config is in [path]/etc/gitconfig, values apply to every user, need to be admin
           --global, config is in ~/.gitconfig or ~/.config/git/config, values apply only to you (the user), this config affect ALL repositories in your system
 (DEFAULT) --local, config is .git/config (i.e. the repository directory), this affect only the current repository (the folder where you are located)
Priority (high to low) is local > global > system

Set your identity with

	$ git config --global user.name "pollo allo spiedo"
	$ git config --global user.email pollo.allo@spiedo.com

Set your editor

	$ git config --global core.editor emacs/vim/gedit
	
Set master branch name, when creating a new repo with git init, the default name is master

	$ git config --global init.defaultBranch masterofpuppets

View the setting with

	$ git config --list --show-origin

This will show something like

	$ file:/home/tentacolo/.gitconfig user.name=tentacolo             <--global config
	$ file:/home/tentacolo/.gitconfig user.email=tenobaldi@gmail.com  <--
	$ file:.git/config        core.repositoryformatversion=0          <--local config
	$ file:.git/config        core.filemode=true                      <--
	$ file:.git/config        core.bare=false                         <--
	$ file:.git/config        core.logallrefupdates=true              <--

--------------------------------------------------------------------------------
GETTING HELP
--------------------------------------------------------------------------------

Help pages are accessible via the commands
	
	$ git <something> --help
	$ git help <something>
	$ man git-<something>

These three produce the same result.
The following is a concise version

	$ git <something> -h
	
Examples: git config --help, git help config, man git-config, git config -h

--------------------------------------------------------------------------------
STARTING A GIT REPOSITORY
--------------------------------------------------------------------------------

There are two ways to start a project:
 - initialise a new one with git init
 - cloning some repository with git clone

Initialisation

You start a new project by making a new directory.
Move into that directory and type

	$ git init

This will create a .git folder containing the repository skeleton.
From now on, any modification to the content of the folder will be tracked with specific commands and store in the .git repository folder.
On the other hand, if the project folder was not empty (say, you want to start a version control system for an existing project)
you just type git init and then manually add the files you want to track and perform an initial commit

	$ git add <some files>
	$ git add <other files>
	$ git commit -m 'Initial project version'

Cloning existing repository

To initialise a project from another source git provides the command clone.
This command copies the entire repository, not just the current version.
When you clone something all the version of the project will be available locally in your machine.
The command is

	$ git clone <url>

This creates a directory in your current folder. The directory contains the actual project and the .git repository folder.
The name will be given depending on the project url. To initialise the project to a folder with another name, type

	$ git clone <url> myfoldername

Protocols for transferring are:
 - https://
 - git://
 - user@server:path/to/repo.git (to clone repos via SSH)

--------------------------------------------------------------------------------
RECORDING CHANGES IN THE REPOSITORY
--------------------------------------------------------------------------------

Each file in the working directory has two states
 - tracked
 - untracked
Tracked files are what git knows about: unmodified (committed), modified or staged.
Untracked is everything else.
When you clone a repo, all files will be in the unmodified status.
As you work, you will modify some files, selectivwly stage some of them, and then commit.
After this, the cycle repeats.

|```````````````|```````````````````````````````````|
|	Untracked	|			Tracked					|
|				| Unmodified	Modified	Staged	|
|```````````````|```````````````````````````````````|
|	   Add------|---------------------------->		|
|	   			|	Edit---------->					|
|	   			|				 Stage------->		|
|	    <-------|---Remove							|
|	   			|	   <--------------------Commit	|
|...............|...................................|

To check the your project type

	$ git status

This will display something like

	$ On branch master
	$ No commits yet
	$ nothing to commit (create/copy files and use "git add" to track)

We now create a new file, for example a README.txt file and type again git status. The output will be

	$ On branch master
	$ No commits yet
	$ Untracked files:
  	$   (use "git add <file>..." to include in what will be committed)
	$      README.txt
	$ nothing added to commit but untracked files present (use "git add" to track)

git is aware of the new file, but it will not add it to the repo until explicitly told to do so.
To add it we type

	$ git add README.txt

git status again

	$ On branch master
	$ No commits yet
	$ Changes to be committed:
  	$   (use "git rm --cached <file>..." to unstage)
	$     new file:   README.txt

The file is now STAGED. We see this because is under "Changes to be committed".
git add command also adds files recursively from a directory.

If we now modify that file, git status returns

	$ On branch master
	$ No commits yet
	$ Changes to be committed:
  	$   (use "git rm --cached <file>..." to unstage)
	$     new file:   README.txt

	$ Changes not staged for commit:
  	$   (use "git add <file>..." to update what will be committed)
  	$   (use "git restore <file>..." to discard changes in working directory)
	$     modified:   README.txt

The modified README file in under "Changes not staged for commit". The previous version is staged.
The files has two versions: the old one that is staged, the new one is unstaged.
To stage this new version of the README file we use add again

	$ git add README.txt

add is a multipurpose command. It serves as:
 - tracking new files
 - staging modified files
 - resolving merge conflicts

Short status

git status is quite verbose. We can type a short version of it using

	$ git status -s
	$ git status --short
	
this gives an output similar to

	$ git status -s
	 M README
	MM Rakefile
	A  lib/git.rb
	M  lib/simplegit.rb
	?? LICENSE.txt

The letter on the left are M for modified, A for staged and ?? for not tracked.
The two columns refer to the staging area (left) and the working tree area (right).

Ignoring files

The specification to which files are to be ignored by git go into the .gitignore file.
An example of file that we may want to ignore are object files .o and anrchives .a produced during compilation.
Or, binary files produced by our software. Or, temporary files produced by editors ~.
Rules are:
 - empty lines or lines starting with # are ignored
 - usual shell matching expressions work:
    - asterisk * matches zero or all characters, e.g. *.txt
    - [abc] matches only one character (either a b or c), e.g. .[ao]
    - ? match a single character, e.g. pollo-??.py
 - starting / avoids recursivity, e.g. /pollo ignores only the pollo file, not the /pollo subdir
 - ending / enforce recursivity, e.g. pollo/ ignores all files inside the pollo directory
 - negate a pattern with !, e.g. !pollo.a keep track of it (even if all the others *.a are ignored)

An example of .gitignore file is

	# ignore all .a files
	*.a
	# but do track lib.a, even though you're ignoring .a files above
	!lib.a
	# only ignore the TODO file in the current directory, not the /TODO subdir
	/TODO
	# ignore all files in any directory named build
	build/
	# ignore doc/notes.txt, but not doc/server/arch.txt
	doc/*.txt
	# ignore all .pdf files in the doc/ directory and any of its subdirectories
	doc/**/*.pdf

Visit https://github.com/github/gitignore for many examples of .gitignore files for different projects/languages.

View detailed changes

For a more detailed view of the status use
	
	$ git diff

This command shows the differences in lines between STAGED and UNSTAGED files.
If my staged files are up to date (i.e. there have been no modification), git diff will no display anything.

On the contrary, if I want to show differences between the stage area and the last commit, I must type

	$ git diff --staged (or)
	$ git diff --cached

the two command above are synonims.
Last, one can use other tools to display differences. To do so, type the help command

	$ git difftool --tool-help

to see what difftools are available in the system and how to use them.

Commit the changes

Now that the stage area is all set up, we can commit. We simply type

	$ git commit

this will open the default editor and show something like

	# Please enter the commit message for your changes. Lines starting
	# with '#' will be ignored, and an empty message aborts the commit.
	#
	# On branch master
	#
	# Initial commit
	#
	# Changes to be committed:
	#       new file:   CONTRIBUTING.md
	#       new file:   README.txt
	#       new file:   main.py
	#

we must add a descriptive comment to our commit to finilise it. The resulting output is

	$ [master (root-commit) 9a66d36] My very first commit. Bla bla bla.
	$ 3 files changed, 11 insertions(+)
	$ create mode 100644 CONTRIBUTING.md
	$ create mode 100644 README.txt
	$ create mode 100644 main.py

Options to the commit command include

	$ git commit -v, verbose, this shows the differences in the staged files when we open the text editor
	$ git commit -m <my message>, we can type the message directly after the commit command, without entering the editor

Skipping the staging area

Sometimes, to speed things up, you dont want to go through all the steps (modify, add to stage and then commit).
For this, we can call commit with the -a flag.

	$ git commit -a -m 'Add EVERY tracked file and commit'

This will add EVERY already tracked file to the stage, and then commit it.
This is convenient, but pay attention that if we are not careful we can add to stage unwanted files.

Removing files

The command to remove a file is

	$ git rm <filename>

This will actually stage the removal of the file. The output is

	$ rm 'myfile.txt'

git status shows:

	$ On branch master
	$ Changes to be committed:
	$  (use "git restore --staged <file>..." to unstage)
	$    deleted:    myfile.txt

After a git commit call, the file will be removed: this means removed from the stage and from the hard drive.
It's the opposite of add (we create/modify a file, we add, we commit).
If the file to be removed has been modified or is in the staging area (i.e. the file has been changed recently and/or is no yet part of a snapshot),
git rm will fail. To force the removal of a modified/staged file use the flag -f

	$ git rm -f <filename> (forces the removal of modified/staged files)

What if we just want to remove a file from the stage but keep it on the working tree?
For example, we didnt set up properly the .gitignore and now we want to unstage something without removing it from our hard drive.
This can be done by typing

	$ git rm --cached <filename>

The output of git status will be something like

	$ On branch master
	$ Changes to be committed:
	$   (use "git restore --staged <file>..." to unstage)
	$ 	  deleted:    myfile.txt

	$ Untracked files:
	$   (use "git add <file>..." to include in what will be committed)
	$ 	  myfile.txt

myfile.txt has not been removed from the hard drive, but it has been untracked.

Moving and renaming files

Git doesnt store metadata of files. If you move or rename a file, in general git will interprete it as a new file.
However, git is very samrt, and can detect file movement/renaming after that happens.
The command

	$ git mv <file_from> <file_to>

does the job. The output is

	$ On branch master
	$ Changes to be committed:
	$   (use "git restore --staged <file>..." to unstage)
	$ 	  renamed:    README.txt -> README

Git recognises that the file has been renamed.

--------------------------------------------------------------------------------
CHECK COMMIT HISTORY
--------------------------------------------------------------------------------

The command to display the the commits is

	$ git log

git log displays commits in reverse order and can take a number of flags for easier visualisation. These are:

	$ git log -n				shows only the last n commits

	$ git log -p, --patch		shows the detailed differences in commits
	
	$ git log --stat			similar to patch, but less verbose
		--shortstat				short version of stat
	
	$ git log --name-only		Show the list of files modified after the commit information.

	$ git log --name-status		Show the list of files affected with added/modified/deleted information as well.
	
	$ git log --abbrev-commit	Show only the first few characters of the SHA-1 checksum instead of all 40.

	$ git log --relative-date	Display the date in a relative format (for example, “2 weeks ago”) instead of using the full date format.
	
	$ git log --graph			shows the history graph tree with commit branches and merges
	
	$ git log --pretty=<key>	applies some format <key>
								 - oneline, prints everything in one line
								 - short, full, fuller, displays less or more information
								 - format, select what info to print based on some format specifiers
Examples of git log are

	$ git log -2
		commit 8a29923370aab95f538699ef17a9438524816e23 (HEAD -> master)
		Author: tentacolo <tenobaldi@gmail.com>
		Date:   Mon May 24 17:23:02 2021 +0800

		    Rename README file

		commit b00d49685a74ffdc530fa1b1713cc2751dc5b6ac
		Author: tentacolo <tenobaldi@gmail.com>
		Date:   Mon May 24 16:48:27 2021 +0800

		    Remove contribution file


	$ git log --stat -2
		commit 8a29923370aab95f538699ef17a9438524816e23 (HEAD -> master)
		Author: tentacolo <tenobaldi@gmail.com>
		Date:   Mon May 24 17:23:02 2021 +0800

		    Rename README file

		 README.txt => README | 0
		 1 file changed, 0 insertions(+), 0 deletions(-)

		commit b00d49685a74ffdc530fa1b1713cc2751dc5b6ac
		Author: tentacolo <tenobaldi@gmail.com>
		Date:   Mon May 24 16:48:27 2021 +0800

		    Remove contribution file

		 CONTRIBUTING.md | 2 --
		 1 file changed, 2 deletions(-)

	$ git log --pretty=oneline -2
		8a29923370aab95f538699ef17a9438524816e23 (HEAD -> master) Rename README file
		b00d49685a74ffdc530fa1b1713cc2751dc5b6ac Remove contribution file

Format specifiers for --pretty=format are

	%H	Commit hash
	%h	Abbreviated commit hash
	%T	Tree hash
	%t	Abbreviated tree hash
	%P	Parent hashes
	%p	Abbreviated parent hashes
	%an	Author name
	%ae	Author email
	%ad	Author date (format respects the --date=option)
	%ar	Author date, relative
	%cn	Committer name
	%ce	Committer email
	%cd	Committer date
	%cr	Committer date, relative
	%s	Subject

For example

	$ git log -2 --pretty=format:"%h - %an, %ar: %s."
		8a29923 - tentacolo, 18 hours ago: Rename README file.
		b00d496 - tentacolo, 19 hours ago: Remove contribution file.

Parsing git log output

	-<n>				Show only the last n commits

	--since, --after	Limit the commits to those made after the specified date.

	--until, --before	Limit the commits to those made before the specified date.

	--author			Only show commits in which the author entry matches the specified string.

	--committer			Only show commits in which the committer entry matches the specified string.

	--grep				Only show commits with a commit message containing the string

	-S					Only show commits adding or removing code matching the string

Example

	$ git log --pretty="%h - %s" --author='Junio C Hamano' --since="2008-10-01" --before="2008-11-01" --no-merges -- t/

These are the commits modifying test files (/t) in the Git source code history committed by Junio Hamano in the month of October 2008 and are not merge commits.

--------------------------------------------------------------------------------
UNDOING THINGS
--------------------------------------------------------------------------------

Undoing thing can cause data loss, since sometimes you cannot undo the undos.

We start with the amend command, this is used for minor changes on the last commit.
Say that I just commit something, but I forgot to add a file

	$ git commit -m 'my commit without a forgotten file'

I can run
	
	$ git add forgotten_file
	$ git commit --amend

this will open the editor, allowing us to modify the commit message if we want.
The new commit amend will replace the last one like the previous "wrong" commit had never happened.

Then we have the git restore command. This is used to unstage some files and/or restore a previous version of a file from the last snapshot.
For example, we mistakenly add a file to the staging area. git status shows

	On branch master
	Changes to be committed:
	  (use "git restore --staged <file>..." to unstage)
		modified:   main.py

Git itself provides a nice help on how to unstage the file.
We can type

	$ git restore --staged main.py

and the file will be removed from the index (index aka staging area).

Finally, in a similar fashion, we can use git restore to revert a modification to the last commit snapshot.
git status shows

	On branch master
	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git restore <file>..." to discard changes in working directory)
		modified:   main.py

The help suggests to use

	$ git restore main.py

To discard changes.
IMPORTANT NOTE: git restore <file> will permanetly discard the modification we did on <file>.
Git will replace that file with the last staged or committed version!

--------------------------------------------------------------------------------
REMOTES
--------------------------------------------------------------------------------

Remote repositories are versions of your project that are hosted on the Internet or network somewhere.
You can check which remotes are configured in your working directory

	$ git remote

If you created your local repo by using the clone command, then you should see (at least) the origin remote.

	$ git remote
		origin

This is the default name that git gives to a remote obtained with the clone command.
To get more info, you can type

	$ git remote -v
		origin	https://gitlab.com/tentacolo/hello-world.git (fetch)
		origin	https://gitlab.com/tentacolo/hello-world.git (push)
		
this gives the URL of the origin remote as well.
More than one remote is possible, for example

	$ git remote -v
	bakkdoor  https://github.com/bakkdoor/grit (fetch)
	bakkdoor  https://github.com/bakkdoor/grit (push)
	cho45     https://github.com/cho45/grit (fetch)
	cho45     https://github.com/cho45/grit (push)
	defunkt   https://github.com/defunkt/grit (fetch)
	defunkt   https://github.com/defunkt/grit (push)
	koke      git://github.com/koke/grit.git (fetch)
	koke      git://github.com/koke/grit.git (push)
	origin    git@github.com:mojombo/grit.git (fetch)
	origin    git@github.com:mojombo/grit.git (push)

The above means that we can pull contributions from any of them.
Also, we may be able to push our modifications to some of them (if we have the permission).
But we cannot tell this from here.

git clone is a short hand for adding a remote and naming it origin,
If you want to add a remote from some URL and giving it a specific name you type

	$ git remote add <name> <url>

For example

	$ git remote add pollo https://gitlab.com/tentacolo/hello-world.git
	$ git remote -v
		origin	https://gitlab.com/tentacolo/hello-world.git (fetch)
		origin	https://gitlab.com/tentacolo/hello-world.git (push)
		pollo	https://gitlab.com/tentacolo/hello-world.git (fetch)
		pollo	https://gitlab.com/tentacolo/hello-world.git (push)

Now we have multiple remotes, we can address them just by their names instead of their URL.
For example, we can fetch from a specific remote by typing

	$ git fetch pollo
		Username for 'https://gitlab.com': tentacolo
		Password for 'https://tentacolo@gitlab.com': *******
		From https://gitlab.com/tentacolo/hello-world
		 * [new branch]      main       -> pollo/main

Now the pollo master branch is accessible locally as pollo/main.

NOTE: this remote has been fetch using the https:// protocol.
There are other protocols available:
	https://
	git://
	git@gitlab.com:    <-- SSH

The command git fetch <remote> only downloads the new data of that particular remote, but does not update your working directory nor it merges those changes.
In order to fetch the changes and merge them to your current branch, you can use

	$ git pull <remote>

The opposite action is when you want to push some changes from your local repo to the online remote.
You can do this by typing

	$ git push <remote> <branch>

This will work only if you cloned from a server where you have write access and no one has pushed anything in the meantime.
NOTE: git push origin mybranch will update/create the remote branch "mybranch" on the server.

If you need information about a remote, then type

	$ git remote show <remote>
		* remote origin
		  Fetch URL: git@gitlab.com:tentacolo/hello-world.git
		  Push  URL: git@gitlab.com:tentacolo/hello-world.git
		  HEAD branch: main
		  Remote branch:
		    main tracked
		  Local branch configured for 'git pull':
		    main merges with remote main
		  Local ref configured for 'git push':
		    main pushes to main (up to date)

The output shows a number of useful info:
 - the URL of the remote
 - the name of the head branch (main in this case)
 - the default branches linked to the commands git pull and git push

To rename a remote type

	$ git remote rename <old> <new>

Finally to remove a remote, type

	$ git remote remove <remote>

--------------------------------------------------------------------------------
TAGS
--------------------------------------------------------------------------------

Tags are what people generally use to label the version of their code at a release point.
For example, v1.0, v2.0, v1.3.002.5 etc.
To list the tags just type

	$ git tag

optional flags are -l or --list. These flags are used when the user provides a wildcard pattern to match the tags.
Tags are listed in alphabetical order.

There are two types of tags:
 - lightweight
 - annotated

Lightweight tags are just pointers to a specific commit. No other info is stored.
Annotated tags instead collect tagger name, email, and date, have a tagging message and are checksummed.
Generaly you alwys want to create annotated tags.
You type

	$ git tag -a v1.0 -m "version 1.0 of my hello world"

If you want to see the info of a particular tag

	$ git show v1.0 -s    (-s, short, not verbose)					_
		tag v1.0													 |
		Tagger: tentacolo <tenobaldi@gmail.com>						 |
		Date:   Fri May 28 16:47:01 2021 +0800						 | annotation of the tag
																	 |
		version 1.0, before pulling from remote						_|
																	_
		commit 1b4b9046be1d98f6dcbae5976cbf140d2fc586ae (tag: v1.0)  |
		Author: tentacolo <tenobaldi@gmail.com>						 |
		Date:   Fri May 28 06:06:56 2021 +0000						 | usual commit info
																	 |
		    Update README.md										_|

This shows all the information about the commit the tag is pointing at.

Lightweight tags are performed by just typing

	$ git tag v1.1-lw

If you run git show v1.1-lw you get only the commit info

	$ git show v1.1-lw -s
		commit 77dad5df512f4f8f85eac9858e41c698a3f01ec4 (HEAD -> main, tag: v1.1-lw, tag: v1.1, origin/main, origin/HEAD)
		Author: tentacolo <tenobaldi@gmail.com>
		Date:   Fri May 28 14:21:24 2021 +0800

		    some change that i want to push

The git tag command only tags the current commit. If you want to tag a previous commint you have to type

	$ git tag -a v0.9 <checksum>

For example, my commit history looks like this

	$ git log --oneline
		77dad5d (HEAD -> main, tag: v1.1-lw, tag: v1.1, origin/main, origin/HEAD) some change that i want to push
		1b4b904 (tag: v1.0) Update README.md
		7fb01a6 Initial commit

I want to tag the very first commit, I type

	$ git tag -a v0.9 7fb01a6 -m "tag a previous commit"

We can display the info with git show

	$ git show v0.9 -s
		tag v0.9
		Tagger: tentacolo <tenobaldi@gmail.com>
		Date:   Tue Jun 1 12:06:12 2021 +0800

		tag a previous commit

		commit 7fb01a67ce822033d1bd79a0a43301e89f78587b (tag: v0.9)
		Author: Stefano Dal Forno <tenobaldi@gmail.com>
		Date:   Tue May 25 05:56:26 2021 +0000

		    Initial commit

Tag date and commit date are different.

When pushing to a remote server, tags are not included by default.
To push you modification AND a the tag type

	$ git push <remote_name> <tag_name>

For example

	$ git push origin v1.0

To push all the tags, type

	$ git push origin --tags

Notice that git push origin --tags only pushes the new tags

	$ git push origin v1.0
		Enumerating objects: 1, done.
		Counting objects: 100% (1/1), done.
		Writing objects: 100% (1/1), 175 bytes | 175.00 KiB/s, done.
		Total 1 (delta 0), reused 0 (delta 0)
		To https://gitlab.com/tentacolo/hello-world.git
		 * [new tag]         v1.0 -> v1.0
	$ git push origin --tags
		Counting objects: 100% (2/2), done.
		Delta compression using up to 8 threads
		Compressing objects: 100% (2/2), done.
		Writing objects: 100% (2/2), 307 bytes | 307.00 KiB/s, done.
		Total 2 (delta 0), reused 0 (delta 0)
		To https://gitlab.com/tentacolo/hello-world.git
		 * [new tag]         v0.9 -> v0.9
		 * [new tag]         v1.1 -> v1.1
		 * [new tag]         v1.1-lw -> v1.1-lw

To delete a tag just type -d or --delete

	$ git tag -d v1.1-lw

To also delete it in the remote, type

	$ git push origin --delete v1.1-lw

Easy peasy.

Finally, checkout a tag. The git checkout command is generally used to switch between branches or to create a new one.
If we use it with tags, we will be in a "detached HEAD" state

	$ git checkout v1.1

This will replace our working directory with the files of the v1.1 tag, but will not be part of any branch!
Which means that to access any commit we do here, we must access them only by hash.
Cheching out a tag is ok only if you DONT want to make changes (e.g. you want to check some files, look around before making any changes).
If you want to make changes, it is advisable to create a branch

	$ git checkout -b version1.1 v1.1

In this way, we create the new branch "version1.1" and our commits will be tracked within it.
Note that the tags will still point at the v1.1 commit. So the new branch version1.1 will eventualy diverge from the initial v1.1

--------------------------------------------------------------------------------
ALIASES
--------------------------------------------------------------------------------

Aliases are user made shortcut for commands. You create an alias using the git config command

	$ git config --global alias.pollo 'log --oneline'

So now, you can type

	$ git pollo

And the output will be the same as git log --oneline
To remove an alias type

	$ git config --global --unset alias.pollo

--------------------------------------------------------------------------------
BRANCHING
--------------------------------------------------------------------------------

When you run the git commit command, git takes a snapshot of your current working directory and stores the information in the repository.
Every commit contains the metadata (author, date, message), the pointers to the files (called blobs in git jargon) and the pointer to the parent commit.
The initial commit have no parents.
A normal commit has only one parent (the previous commit).
A merge commit has multiple parents depending on which branches joined in this commit.

When a new project is created, git initialises the "master" branch. This branch has nothing different from any other branch that the user can create later.
"master" is just the default name git gives to the first branch of the project.

What is a branch? A branch is just a pointer to a specific commit!

To create a new branch type

	$ git branch <newbranch>

This creates a branch that points at the commit i'm located at.
How does git know which brach we are? Git uses the HEAD pointer to keep track of the current branch.
For example, we create a new branch called testing

	$ git branch testing

We are located at the commit f30ab. HEAD points to master, master points to f30ab, testing also points at f30ab.
Here is a scheme:

                           HEAD
                                           ↓
                          master
                                           ↓
	98ca9 <--- 34ac2 <--- f30ab
						       ↑
						  testing

You see that creating a new branch doesnt switch the branch.

	$ git log --oneline
	77dad5d (HEAD -> main, tag: v1.1, origin/main, origin/HEAD, testing) some change that i want to push
	1b4b904 (tag: v1.0) Update README.md
	7fb01a6 (tag: v0.9) Initial commit

HEAD is pointing at main.

To switch to the testing branch we type

	$ git checkout testing
		Switched to branch 'testing'

git log now shows

	77dad5d (HEAD -> testing, tag: v1.1, origin/main, origin/HEAD, main) some change that i want to push
	1b4b904 (tag: v1.0) Update README.md
	7fb01a6 (tag: v0.9) Initial commit

HEAD now points at testing.
While in branch testing, let do some modifications and then commit.	git log shows

	d417ad1 (HEAD -> testing) first commit on the testing branch						  <---- we moved forward
	77dad5d (tag: v1.1, origin/main, origin/HEAD, main) some change that i want to push   <---- the master (main) branch is behind
	1b4b904 (tag: v1.0) Update README.md
	7fb01a6 (tag: v0.9) Initial commit

Also, note that the remote main and the remote HEAD are behind.
We can checkout back to the master branch. git log shows

	77dad5d (HEAD -> main, tag: v1.1, origin/main, origin/HEAD) some change that i want to push
	1b4b904 (tag: v1.0) Update README.md
	7fb01a6 (tag: v0.9) Initial commit

Strange! While on the main branch, we cannot see the testing branch! This is because git log only shows the parents.
To show the log for all branches, type

	$ git log --all

and to see the list of branches just type

	$ git branch --list (or -l)

Now that we are on the main branch, let's do some modfications and commit again.

	$ git log --oneline --graph --all
		* 3a82ea2 (HEAD -> main) added a file to master branch
		| * d417ad1 (testing) first commit on the testing branch
		|/  
		* 77dad5d (tag: v1.1, origin/main, origin/HEAD) some change that i want to push
		* 1b4b904 (tag: v1.0) Update README.md
		* 7fb01a6 (tag: v0.9) Initial commit

Now the project history has diverged.

                                     HEAD
                                                         ↓
                                    master
                                                         ↓
                                   3a82ea2
                                      /
	                                 /
	7fb01a6 <--- 1b4b904 <--- 77dad5d
							         \
							       	  \
							       d417ad1
						                     ↑
						            testing


All the power of git in three simple commands:

 - git branch
 - git checkout
 - git commit

Final note, to create a branch and switch to it you can use the shortcut

	$ git checkout -b <newbranch>

Also, from git 2.23, the command switch has been introduced

	$ git switch <somebranch>      checks out an already exixsting <somebranch>
	$ git switch -c <newbranch>    creates and switches to <newbranch>
	$ git switch -                 go back to the previuosly checked branch

NOTE: switch and restore have been introduced to avoid confusion of the many behaviours of the command checkout
checkout is a swill army knife, many thing can be done with a single command, and this can be confusing

	$ git checkout <branch>        ---->   git switch <branch>
	$ git checkout --pathtofile    ---->   git restore <file>
	$ git checkout -b <newbranch>  ---->   git switch -c <newbranch>


--------------------------------------------------------------------------------
BASIC BRANCHING AND MERGING
--------------------------------------------------------------------------------

When working on a project, it often happens that you want to test some code before deploying it, or while you are coding you find some bug that must be resolved immediately.
Also, it can be that those two thing happen at the same time, so you must pause from testing your code, go back to fix the bug, and then resume the testing part.
Finally, all code must be deploy into a single piece (jargon, merge to master/production).
To do this, git provides the branching and merging commands.

Example:
 - we are on the master branch
 - we switch to a new testing branch
 
 	$ git switch -c testing
 	
 - we commit some test changes
 
	* 32b034b (HEAD -> testing) some commit on testing branch
	* 5544e35 (main) some commit on main branch
	* 7fb01a6 Initial commit

 - now HEAD is on testing, main is behind
 - suddenly, we need to do a hotfix to master branch.
   We must go back to the master, and create a hotfix branch
 
 	$ git switch master
 	$ git switch -c hotfix

 - we perform the hotfix commits. The log prints out the following
 
 	$ git log
	* 0c582c0 (HEAD -> hotfix) a second hotfix commit
	* 01af1ce add a hotfix to readme
	| * 32b034b (testing) some commit on testing branch
	|/  
	*   5544e35 (main) some commit on main branch
	* 7fb01a6 Initial commit
	
 - then when we are happy with the fix, we switch back to master and merge the hotfix branch into the main
   
   	$ git switch main
   	$ git merge hotfix
   	Updating 5544e35..0c582c0
	Fast-forward         <---- NOTE THIS: fast forward, because hotfix is just two commits ahead of main, git only moves the pointer!
	 README.md   | 2 ++
	 testing.txt | 2 ++
	 2 files changed, 4 insertions(+)

 - we can now safely delete the hotfix branch
 	
 	$ git branch -d hotfix    (remeber, a branch is just a pointer to a certain commit)
 	
 - we can go back to the testing branch to continue with our work
 - after some commits we can try to merge it with the main one
 - the testing branch however will not contain the hotfix we did on the main branch
 
	$ git switch main
	$ git merge testing
	Merge made by the 'recursive' strategy.   <--- NOTE THIS: recursive strategy, testing and main are not sequential, they diverged from a common ancestor
	 hello-world.py | 4 ++++								  git merge them together, te resulting commit has more than one parent commit!
	 1 file changed, 4 insertions(+)

 - git log prints
 
 	$ git log --graph --all --oneline
 	*   ec7606f (HEAD -> main) Merge branch 'testing' into main
	|\  
	| * 398b6ba (testing) some other tests in hello-world
	| * 32b034b some commit on testing branch
	* | 0c582c0 a second hotfix commit
	* | 01af1ce add a hotfix to readme
	|/  
	*   5544e35 some commit on main branch
	* 7fb01a6 Initial commit

NOTE: after the 'recursive' merge, the testing branch is still pointing to the last testing commit (398b6ba).
On the other hand, the main branch has been updated and now points to the very last commit (ec7606f).

Merge conflicts

If two of our branches modify the same file in different ways, then merging them together willcouse a merge conflict.
Which version of the file do we keep?

Let's suppose we are in this case:

	* ad84a25 (HEAD -> conflict2) example of merge conflict 2    <--- there are two branches that commited different things on the same file
	| * 70358f0 (conflict1) example of merge conflict 1          <---
	|/  
	*   ec7606f (main) some commit

We swithc to main, merge the first branch

	$ git switch main
	$ git merge conflict1
	Updating ec7606f..70358f0
	Fast-forward
	 testing.txt | 2 ++
	 1 file changed, 2 insertions(+)

All good. Now we also want to merge the second branch into main:

	$ git merge conflict2
	Auto-merging testing.txt
	CONFLICT (content): Merge conflict in testing.txt
	Automatic merge failed; fix conflicts and then commit the result.

We got an error!
We can run a git status and obtain

	On branch main
	Your branch is ahead of 'origin/main' by 6 commits.
	  (use "git push" to publish your local commits)
	
	You have unmerged paths.
	  (fix conflicts and run "git commit")
	  (use "git merge --abort" to abort the merge)

	Unmerged paths:
	  (use "git add <file>..." to mark resolution)
		both modified:   testing.txt

	no changes added to commit (use "git add" and/or "git commit -a")

Git attempted the merge and stopped. Now it offers us to options:
 - to fix the conflicts and commit them
 - or just undo the merge with git merge --abort

Also, if we try to switch to another branch now, git will NOT allow it.

	$ git switch conflict2
	fatal: cannot switch branch while merging
	Consider "git merge --quit" or "git worktree add".
	
In this attempt to merge the two branches, git modified the files involved in the conflict.
These files are listed in the unmerged paths. In this case the conflict in the file testing.txt.
If we open it we will see something like the following

	testing file made to test git branching

	another hotfix to test branching and merging
																				   _
	<<<<<<< HEAD																	|
	i wrote this line to test a merge conflict scenario (on branch conflict1)		|
	=======																			| this is the conflict part that git has highlightened
	i wrote this line to test a merge conflict (we are on branch conflict 2)		|
	>>>>>>> conflict2															   _|

The above shows the two lines of text that differ:
 - the HEAD version is the current one (because we switch to main when we try to merge)
 - after the separator ======= we have the conflict line (that belongs to the branch named conflict2)

To resolve the conflict we simply have to modify the files and keep only one version of them.
After the modification, we must add the new file to stage (or git commit -a)

	$ git add testing.txt

After this the status should be

	On branch main
	Your branch is ahead of 'origin/main' by 6 commits.
	  (use "git push" to publish your local commits)

	All conflicts fixed but you are still merging.
	  (use "git commit" to conclude merge)

	Changes to be committed:
		modified:   testing.txt

To conclude the merging process we type commit.
Since this is a merge commit, the deault message will look different:

	Merge branch 'conflict2' into main

	# Conflicts:
	#       testing.txt
	#
	# It looks like you may be committing a merge.
	# If this is not correct, please remove the file
	#       .git/MERGE_HEAD
	# and try again.


	# Please enter the commit message for your changes. Lines starting
	# with '#' will be ignored, and an empty message aborts the commit.
	#
	# On branch main
	# Your branch is ahead of 'origin/main' by 6 commits.
	#   (use "git push" to publish your local commits)
	#
	# All conflicts fixed but you are still merging.
	#
	# Changes to be committed:
	#       modified:   testing.txt
	#

Generally you want to give some more information about the merge commit for people in the future.

--------------------------------------------------------------------------------
BRANCH MANAGEMENT
--------------------------------------------------------------------------------

The command git branch is useful to manage all our branches. Flags are

	$ git branch (no flags) lists all branches
	  conflict1
	  conflict2
	* main			<--- asterisk indicates the current branch
	  testing
	  
	$ git branch --merged       lests the branches that have beenn merged with the current one
	$ git branch --no-merged    same as above, but not merged
	
Generally, you may want to delete branches showed as merged. They job is done and no work will be lost if you remove them.
You can do this with

	$ git branch -d <branchname>

However, this command will fail with a branch that has never been merged

	$ git branch --no-merged
	pollo
	$ git branch -d pollo
	error: The branch 'pollo' is not fully merged.
	If you are sure you want to delete it, run 'git branch -D pollo'.

As you see, git is preventing us from deleting a not fully merged branch. To force the deletion we must use the -D flag.
Info of branch state are always provided wth respect to your current branch.
To ask for info about any branch, just provide its name after the command

	$ git branch --merged testing   <--- this will display which branches are merged with respect to the testing branch
	
To change a branch name you can type

	$ git branch --move <old-name> <new-name>

This changes the name of the branch locally!
To deploy this modification on the server (if any) just push it like this

	$ git push --set-upstream <remote> <new-name>

The flag --set-upstream is optional (or -u for short) and its purpose is to track the local and remote branch.
In this way future push or pull command can be run without specifying explicitly which remote or branch to push or pull from.
Finally, in order to check all our branches, local, remote and tracked type

	$ git branch --all -vv
	  conflict1              70358f0 example of merge conflict 1        <-- these branches are only local
	  conflict2              ad84a25 example of merge conflict 2
	* main                   a85a8c5 [origin/main] Update testing.txt   <-- local HEAD is here, [origin/main] means main is tracked
	  testing                398b6ba some other tests in hello-world
	  remotes/origin/HEAD    -> origin/main
	  remotes/origin/main    a85a8c5 Update testing.txt                 <-- remote HEAD is here
	  remotes/origin/testing 398b6ba some other tests in hello-world    <-- remote testing branch, not tracked (no upstream set up)

--------------------------------------------------------------------------------
BRANCHING WORKFLOW
--------------------------------------------------------------------------------

What people do when developing code is to construct a workflow with several levels of stability.
In every level there can be one or more branches. In general a workflow layout looks like

	C1 ---> C2 											master or main level
			 \
			  \
			  C3 ---> C4 ---> C5 ---> C6				develop or next level
			  				   \
			  				    \
			  				    C7 ---> C8				topic or hotfix level

The top level is the stable version aka the master/main branch. Then we have the develop/next branch where new feature of our code will go.
Finally we can have topic branches where specific issues can be addressed and resolved.
Developing a project means to steadily creating, merging and deleting low level branches into the above ones.
Eventually, the develop branch is merged into master, and a new stable version of the code becomes available.
Then the cycle repeats.

--------------------------------------------------------------------------------
REMOTE BRANCHES
--------------------------------------------------------------------------------

We saw that a branch in git is nothing but a pointer to a specific commit.
When we clone a project to our local machine, git also clones the branches defined in that remote.
Remote branches are named as

	<remote_name>/<branch_name>

By default, when we clone a project via $ git clone <URL>, the name of the main remote branch will be

	origin/main or origin/master

To list all the configured remote branches type

	$ git remote show origin
	Username for 'https://gitlab.com': tentacolo
	Password for 'https://tentacolo@gitlab.com': ******
	* remote origin
	  Fetch URL: https://gitlab.com/tentacolo/hello-world.git
	  Push  URL: https://gitlab.com/tentacolo/hello-world.git
	  HEAD branch: main
	  Remote branches:
	    main    tracked
	    testing tracked
	  Local branch configured for 'git pull':
	    main merges with remote main
	  Local refs configured for 'git push':
	    main    pushes to main    (up to date)
	    testing pushes to testing (up to date)

To list all remote and local branches type

	$ git branch --all -vv
	  conflict1              70358f0 example of merge conflict 1
	  conflict2              ad84a25 example of merge conflict 2
	* main                   a85a8c5 [origin/main] Update testing.txt
	  testing                398b6ba some other tests in hello-world
	  remotes/origin/HEAD    -> origin/main
	  remotes/origin/main    a85a8c5 Update testing.txt
	  remotes/origin/testing 398b6ba some other tests in hello-world

Finally, as always, git log will also give information about the branching network

	* a85a8c5 (HEAD -> main, origin/main, origin/HEAD) Update testing.txt					<-- HEAD, main and origin/HEAD, origin/main are here
	*   24d83a2 Merge branch 'conflict2' into main My first merge commit with conflicts
	|\  
	| * ad84a25 (conflict2) example of merge conflict 2										<-- these branches are only local
	* | 70358f0 (conflict1) example of merge conflict 1
	|/  
	*   ec7606f Merge branch 'testing' into main
	|\  
	| * 398b6ba (origin/testing, testing) some other tests in hello-world					<-- testing and origin/testing branch are both here
	| * 32b034b add print test to hello-world
	* | 0c582c0 a second hotfix commit
	* | 01af1ce add a hotfix to readme
	|/  
	*   5544e35 Merge branch 'testing' into main
	|\  
	| * d417ad1 first commit on the testing branch
	* | 3a82ea2 added a file to master branch
	|/  
	* 77dad5d (tag: v1.1) some change that i want to push
	* 1b4b904 (tag: v1.0) Update README.md
	* 7fb01a6 (tag: v0.9) Initial commit

Remote branches are useful to keep track of changes done by others on the remote repository.
NOTE: git does not update those changes automatically! Git always works locally and the communication with the server must be done with specific commands!
To update our local version of the repository we type

	$ gir fetch <remote_name>

This command will download the data that I dont have yet and will update the position of the remote branches.
The pointers will point to the newly downloaded commits.
NOTE: when fetching from a remote, the remote branches cannot be modified! Of course, these pointers only show you where the remote repository is.
In order to do some work with them, you must create a local version of that remote branch.
Once the job is done, you push your modifications to the remote branch.

	$ git push <remote_name> <local_branch>

For example

	$ git push origin test
	
This tells git to upload to the origin remote my modification on the test branch.
Git will update the remote origin/test branch with my new commits.
NOTE: writing just "test" is a shortcut! Git assumes that both the local and the remote branches have the same name (i.e. test)
If your local and remote branches have different names the syntax is

	$ git push origin local_test:remote_test

Tracking branches

Git offers the possibility of defining track branches pairs:

	local branch <---> remote branch

The local branch is called tracking branch, while the remote branch is called upstream branch.
When you clone from an online repo, git automaticlly sets the main branch to track the origin/main remote branch:

	main <--> origin/main

This is useful when performing the command pull.
git pull is a shortcut for git fetch and git merge.
If we are located in a tracking branch, we can run git pull without arguments and git will fetch and merge from the upstream branch!
To track a branch there are several options

The following create a new local branch and track a remote one

	$ git checkout -b <new_local_branch> <remote_branch_to_track>
	$ git checkout --track <remote_branch_to_track>					<-- shortcut of the above, the local branch will have the same name
	$ git checkout <new_local_branch>								<-- shortcut of the shortcut, if the local branch does not exist and the name matches a remote branch

If a local branch already exists, we can set it to track something with

	$ git branch -u origin/testing			<-- our current branch will track origin/testing
	$ git push -u testing origin/testing	<-- we push testing to origin/testing and track it

We can check which branch is tracking what with the command

	$ git branch -vv
	  conflict1 70358f0 example of merge conflict 1
	  conflict2 ad84a25 example of merge conflict 2
	  main      ff9394a [origin/main] Update hello-world.py
	* testing   18eab46 [origin/testing] merge commit with the remote branch

Finally, to delete remote branches you type

	$ git push origin --delete serverfix
	To https://github.com/schacon/simplegit
	 - [deleted]         serverfix

--------------------------------------------------------------------------------
REBASE
--------------------------------------------------------------------------------

Rebasing is a merging procedure that "rewrites" the commit history.
Rebasing a branch onto another can be done with

	$ git checkout testing
	$ git rebase master

This two lines will "append" the entire test branch after the current master pointer.
We then checkout back to master and just fastforward.

	$ git checkout master
	$ git merge testing
	
This is the scheme of the history

				master
				   |
	C1 --- C2 --- C5
			\
			C3 --- C4
				   |
				testing

Rebase:
				master		   testing
				   |			  |
	C1 --- C2 --- C5 --- C3' --- C4'

The history is rewritten, changes are merged as if they were sequential.
In the above example, rebasing is useful if you want to clean up a messy history.
A linear graph where things happen sequentially is much more readable.
However, if my repo is shared, and I rebase a branch that someone else is using, this can cause problems.
When this person pulls, he will see more than one commit with same authos, date and comment.
The history after the pull will have multiple biforcations, due to the interwined network introduced by the rebase.
As a general rule:
	
	DO NOT REBASE COMMITS THAT EXIST OUTSIDE YOUR REPOSITORY AND THAT PEOPLE MAY HAVE BASED WORK ON.

Recap:

 - use rebasing to locally clean up my history before pushing it online.
   Dont rebase commits i use by other collaborators.
   A linear history is more readable that the train of thought that brought me to the solution.

 - for everything else, use the good old merge.
 
--------------------------------------------------------------------------------
GIT PROTOCOLS
--------------------------------------------------------------------------------

To share projects with a group of developer we need a server to host our git repo.
Here we are not going to show how to setup our own private git server.
Generally, companies that dont want their source code to be host by third party, choose to set up their own git servers.
In our case, we are going to rely on platforms already available for sharing and collaborating like GitHub, GitLab, etc.
If you are still curious about setting up your own git server, visit

	https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols

Here we are only going to explain what protocols are and how to use them.

Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.

The local protocol is used for remotes located in the same host. This can be literally a repo on the very same machine or a repo on a shared file system.
To clone from a local repo just type

	$ git clone /path/to/repo.git
	
	or
	
	$ git clone file:///path/to/repo.git

You can use this to add a local repo as a remote to your project

	$ git remote add local_project /path/to/repo.git

and perform all the thing we saw already with that remote.
Pros: the local protocol is easy to use and can bypass push and pull from others.
Cons: it can be slower than other protocols since it depends on the shared filesystem.

The HTTP protocol comes in two version, the old "dumb" version and the new "smart" version.
The smart HTTP works simalarly to the git or SSH protocols. It runs over the standard HTTPS ports and has an easies authentication.
It does not require SSH key, only username and password.
The strength of HTTP is that pulling and pushing can be done using the same URL:
 - pulling can be done anonimously as in the git:// protocol
 - pushing is encrypted as in SSH
When credentials are required, the server will just prompt to insert username and password.
Cloning with HTTP can be done with

	$ git clone https://gitlab.com/tentacolo/hello-world.git

Pros are HTTP is simple tu use, does not require setting up a key authentication and has the same level of secutity and speed of SSH.
Cons: HTTP may be tricky to use on some servers and authentication with username and password can be annoying.
To avoid this git provides the credential storage tool (more on this later on).

The SSH protocol requires a private-public key to be set up.
Instructions on how to do this are available online and on the major git services.
Generally it is required to copy the public key on the server to have granted SSH access.
Cloning with SSH has the following syntax

	$ git clone git@gitlab.com:tentacolo/hello-world.git

Pros: there are many pros, SSH is secure, fast, installed almost everywhere and easy to set up.
Cons: SSH does not allow anonymous transfers, even for read-only projects. To use SSH, the user must give its public key to the server.
This means that SSH is not suitable for open-source projects where anyone can fetch the code and take a look at it.

The git protocol is similar to SSH but with absolutely NO authentication.
It listen to port 9418 and can be setup with the appropriate daemon.
Pros: it is generally use for read-only projects (because of the lack of authentication) and it's fast (no encryption overhead).
Cons: it's difficult to setup, it does not provide authentication, must be setup with other protocols for the writing permissions.

