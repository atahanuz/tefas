git clone https://github.com/atahanuz/neo.git tempfolder
rsync -a tempfolder/ .
rm -rf tempfolder
python3 server.py
