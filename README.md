# dsascanapi

Helper script to make single file scanning available through rest api.  
Create directory "/opt/dsascanapi" and copy python file the directory.  
Copy service file to systemd and reload  
Test with curl http://localhost:8081/api/v0.1/test or  
curl -X POST -H "Content-Type: application/json" http://localhost:8081/api/v0.1/scan -d '{"file": "/home"}'  
