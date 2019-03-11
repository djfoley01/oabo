
# OABO Runner

testing:<br>
docker run -e OCPTOKEN=$OCPTOKEN -e OCPURL=$OCPURL -it runner bash<br>
docker run -e OCPTOKEN=$OCPTOKEN -e OCPURL=$OCPURL -it runner python app/backup.py<br>
<br>
Right now the contents of backup.py could easily be written in a bash script, in the future though I'd like for this to hit the controller API to get and put job status, logs, etc. 
