dateandtime=$(date "+%Y-%m-%d %H:%M:%S")
git commit -a -m "$dateandtime, $1" 
git push
