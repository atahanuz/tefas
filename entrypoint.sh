git clone https://github.com/atahanuz/tefas.git tempfolder
rsync -a tempfolder/ .
rm -rf tempfolder
python3 alter.py
