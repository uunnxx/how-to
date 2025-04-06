'''
Open Closed Principle
A class / function should be open for extension, and closed for modification
'''

class StorageLocker:
    '''not like this'''
    def authenticate(self, client):
        if client == 'aws':
            # some code to authenticate against aws
        elif client == 'azure':
            # some code to authenticate against azure
        elif client == 'gcp':
            # some code to authenticate against google cloud provider

        return client

    def upload(self, filename):
        if client == 'aws':
            # some code to upload a file to aws
        elif client == 'azure':
            # some code to upload a file to azure


# Open-Closed
from abc import ABC, abstractmethod


class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass


class AWS(Auth, Uploader):
    def authenticate(self):
        # some logic to authenticate against aws
        return auth_client

    def upload_file(self, filename):
        # some logic to upload file to aws
        return status_code


class Azure(Auth, Uploader):
    def authenticate(self):
        # some logic to authenticate against azure
        return auth_client

    def upload_file(self, filename):
        # some logic to upload file to azure
        return status_code


class Gcp(Auth, Uploader):
    def authenticate(self):
        # some logic to authenticate against gcp
        return auth_client

    def upload_file(self, filename):
        # some logic to upload file to gcp
        return status_code
