# Useful script to get a Google service account access token for accessing Google APIs
Because access tokens expire, there is a need for a script that fetches new access tokens if needed.
The token information is persisted in a file, improving performance (we save one Google auth fetch token request and cut request time from 500ms to about 10ms).
The token expiry is used to determine if a new token needs to be fetched.

# Request
The request parameters are:
- file : the service account json credentials file
- scope: the google API you want access to

Ex: http://localhost:5000/token?file=gbc-yadayada-1k3lbnc-243e0cf7a5fc.json&scope=https://www.googleapis.com/auth/businessmessages
