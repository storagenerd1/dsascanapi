# TrendMicro DSA Scan API  

Short description, will cleanup later

Helper script to make single file scanning available through rest api. 
Can be started from commandline for testing.  
/usr/bin/python3 dsascanapi.py  
Or installed as service:  
Create directory "/opt/dsascanapi" and copy python file the directory.  
Copy service file to systemd and reload  
Test with curl http://localhost:8081/api/v0.1/test or  
curl -X POST -H "Content-Type: application/json" http://localhost:8081/api/v0.1/scan -d '{"file": "/home"}'  
