import sentry_sdk
from sentry_sdk import capture_exception, capture_message

class SentryController:
    def __init__(self, dsn):
        sentry_sdk.init(dsn)

    def log_error(self, error_message):
        capture_message(error_message, level="error")

    def log_exception(self, exception):
        capture_exception(exception)