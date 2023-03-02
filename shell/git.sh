# Git branch last activity:
# Here I am starting a new category for short posts where I will give some usefull code snippet or shell
# command for every day use. So I start with a git command used to show last commit date for each branch,
# sorted by last commit date desc:

for branch in `git branch -a | grep -v HEAD`;do echo -e `git show -s --format="%ci,%cr,$branch,%an" $branch`; done | sort -r |column -t -s ","
