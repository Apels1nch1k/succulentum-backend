from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'A server error occurred.'

    def __init__(self, message=None):
        if message is not None:
            self.detail = message
        else:
            self.detail = self.default_detail