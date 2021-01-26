class LogPipeError(Exception):
    pass


class UnknownFormatError(LogPipeError):
    pass


class IgnoredMessageTypeError(LogPipeError):
    pass


class UnknownMessageTypeError(LogPipeError):
    pass


class UnknownMessageVersionError(LogPipeError):
    pass


class InvalidMessageError(LogPipeError):
    pass


class MissingTopicError(LogPipeError):
    pass


class ImproperlyConfigured(Exception):
    """LogPipe is somehow improperly configured"""
    pass