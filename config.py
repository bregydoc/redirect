import os


class Config:
    def __init__(self):
        self.focus_url = os.environ.get(
            'REDIRECT_URL', "http://www.example.com")
        self.code_redirect = os.environ.get('REDIRECT_CODE', 302)
        self.route = os.environ.get('ROUTE', '/')

        self.port = os.environ.get('PORT', 8080)
        self.instrument_port = os.environ.get("INSTRUMENT_PORT", 8000)
