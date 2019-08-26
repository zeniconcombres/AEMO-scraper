# AEMO-scraper
Simple python script to download AEMO FCAS data, can be used to download any files really

Create directory for files `mkdir files`

Run the scraper `python scraper.py`

Run logstash to send data into ES `./logstash -f csvparser.conf --pipeline.workers 16 pipeline.batch.size 250 --config.reload.automatic`
