
docker run -e OCPTOKEN=$OCPTOKEN -e OCPURL=$OCPURL -it runner bash
docker run -e OCPTOKEN=$OCPTOKEN -e OCPURL=$OCPURL -it runner python app/backup.py


