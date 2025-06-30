```bash
[colette.kelly@poseidon-l1 crocolake-python]$ git remote -v
origin	https://github.com/ckelly314/crocolake-python.git (fetch)
origin	https://github.com/ckelly314/crocolake-python.git (push)
[colette.kelly@poseidon-l1 crocolake-python]$ git remote add upstream https://github.com/boom-lab/crocolake-python.git
[colette.kelly@poseidon-l1 crocolake-python]$ git fetch upstream
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 3), reused 6 (delta 3), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), done.
From https://github.com/boom-lab/crocolake-python
 * [new branch]      main       -> upstream/main
[colette.kelly@poseidon-l1 crocolake-python]$ ls -l
total 40
-rw-rw-r-- 1 colette.kelly domain users   299 Jun 30 10:24 environment.yml
-rw-rw-r-- 1 colette.kelly domain users 35149 Jun 30 10:23 LICENSE
drwxrwxr-x 2 colette.kelly domain users  4096 Jun 30 10:23 notebooks
-rw-rw-r-- 1 colette.kelly domain users  3197 Jun 30 10:23 README.md
drwxrwxr-x 2 colette.kelly domain users  4096 Jun 30 10:23 scripts
-rw-rw-r-- 1 colette.kelly domain users  1093 Jun 30 10:23 setup.py
[colette.kelly@poseidon-l1 crocolake-python]$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/upstream/main
[colette.kelly@poseidon-l1 crocolake-python]$ git merge remotes/upstream/main
Auto-merging environment.yml
CONFLICT (add/add): Merge conflict in environment.yml
Automatic merge failed; fix conflicts and then commit the result.
[colette.kelly@poseidon-l1 crocolake-python]$ nano environment.yml
[colette.kelly@poseidon-l1 crocolake-python]$ git status
# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#
# Changes to be committed:
#
#	modified:   README.md
#	modified:   notebooks/Example_5_CrocoLakeBGC_Map_Temperature.ipynb
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#
#	both added:         environment.yml
#
[colette.kelly@poseidon-l1 crocolake-python]$ git add --all
[colette.kelly@poseidon-l1 crocolake-python]$ git commit --all -m "add enrico's example 5"
[main 7f30b84] add enricos example 5
[colette.kelly@poseidon-l1 crocolake-python]$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/upstream/main
[colette.kelly@poseidon-l1 crocolake-python]$ git push origin main
Counting objects: 7, done.
Delta compression using up to 36 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 322 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/ckelly314/crocolake-python.git
   0d644a4..7f30b84  main -> main
[colette.kelly@poseidon-l1 crocolake-python]$ 
```