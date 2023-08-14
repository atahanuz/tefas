git clone https://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@github.com/atahanuz/tefas.git tempfolder

rsync -a tempfolder/ .
rm -rf tempfolder
python3 mailer.py
python3 server.py
