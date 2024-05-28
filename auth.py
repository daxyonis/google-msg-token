
# Copyright 2022 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START auth_cloud_idtoken_service_account]

from flask import json
import google.auth
import google.auth.transport.requests
from datetime import datetime

from google.oauth2 import service_account

class ServiceAccountAuth:    

    def __init__(self, json_credential_path: str, scope: str):
        self.json_credential_path = json_credential_path
        self.scope = scope        
        self.token_data = self.__get_token()

    def __needs_update(self, token_data):
          return (token_data is None or
                  datetime.strptime(token_data["expiry"], '%a, %d %b %Y %H:%M:%S GMT') < google.auth._helpers.utcnow() or
                  token_data["json_credential_path"] != self.json_credential_path or
                  token_data["scope"] != self.scope)

    def __get_token(self):        
      """      
      Obtains an ID token using a service account json credential file.
      *NOTE*:
      Using service account keys introduces risk; they are long-lived, and can be used by anyone
      that obtains the key. Proper rotation and storage reduce this risk but do not eliminate it.
      For these reasons, you should consider an alternative approach that
      does not use a service account key. Several alternatives to service account keys
      are described here:
      https://cloud.google.com/docs/authentication/external/set-up-adc
            
      """
      token_data = None
      # Check if the token is already available and not expired.
      try:
        with open("token.json", "r") as file:
          token_data = json.load(file)
        if self.__needs_update(token_data):
          token_data = self.new_token()
      
      except FileNotFoundError:
        # Obtain the id token by providing the json file path and target audience.
        token_data = self.new_token()        
      
      return token_data

    def new_token(self):
        credentials = service_account.Credentials.from_service_account_file(self.json_credential_path)
        scoped_credentials = credentials.with_scopes([self.scope])
        request = google.auth.transport.requests.Request()
        scoped_credentials.refresh(request)
        token_data = {"token": scoped_credentials.token, "expiry": scoped_credentials.expiry, "scope": self.scope, "json_credential_path": self.json_credential_path}
        
        with open("token.json", "w") as file:
          json.dump(token_data, file)

        return token_data

      
    