class SDKException(Exception):
    """The base exception class for all exceptions this library raises."""

    def __init__(self, message=None):
        message = self.__class__.__name__ if message is None else message
        super(Exception, self).__init__(message)


class AuthorizationFailure(SDKException):
    """Cannot authorize API client."""


class EndpointException(SDKException):
    """Something is rotten in Service Catalog."""


class EndpointNotFound(EndpointException):
    """Could not find requested endpoint in Service Catalog."""


class EmptyCatalog(EndpointNotFound):
    """The service catalog is empty."""


class NoMatchingPlugin(SDKException):
    """No matching plugins could be created with the provided parameters."""


class InvalidResponse(SDKException):
    """The response from the server is not valid for this request."""

    def __init__(self, response):
        super(InvalidResponse, self).__init__()
        self.response = response


class HttpException(SDKException):
    def __init__(self, message, details=None):
        super(HttpException, self).__init__(message)
        self.details = details


class MethodNotSupported(SDKException):
    """The resource does not support this operation type."""


class ResourceNotFound(SDKException):
    """The requested resource was not found."""


class DuplicateResource(SDKException):
    """More than one resource exists with that name."""


class FirebaseConnectionError(Exception):
    """
    There was an error connecting to the firebase client.
    """

    def __init__(self, obj, message="Unable to reach the firebase client"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


class PostgresConnectionError(Exception):
    """
    There was an error connecting to the postgres client.
    """

    def __init__(self, obj, message="Unable to reach the postgres client"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} [ERR] - {self.message}"


class PostgresExecutionError(Exception):
    """
    There was an error connecting to the postgres client.
    """

    def __init__(self, obj, message="You're missing a connection string"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} [ERR] - {self.message}"


class ClientSDKSetupError(Exception):
    """
    There was an error accepting your auth token.
    """

    def __init__(self, obj, message="Unable to init the headless sdk"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


class ExecutionError(Exception):
    """
    There was an error executing sql query.
    """

    def __init__(
        self, obj, message="Unable to execute query, check your connection info"
    ):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


class EmptyResultsWarning(Exception):
    """
    There were no results found.
    """

    def __init__(self, obj, message="Empty query results detected"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"
