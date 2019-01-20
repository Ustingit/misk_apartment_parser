class UnparsedFlat:

    URL = None
    HTML = None
    ErrorDate = None
    Exception = None

    def __init__(self, URL=None, HTML=None, ErrorDate=None, Exception=None):
        self.URL = URL
        self.HTML = HTML
        self.ErrorDate = ErrorDate
        self.Exception = Exception
