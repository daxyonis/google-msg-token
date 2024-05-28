# Useful script to pair with an automation, for example
Because access tokens expire, there is a need for a script that fetches new access tokens if needed

# Request
The request parameters are:
file : the service account json credentials file
scope: the google API you want access to

Ex: http://localhost:5000/token?file=gbc-yadayada-1k3lbnc-243e0cf7a5fc.json&scope=https://www.googleapis.com/auth/businessmessages
