import prometheus_client as pc


class Instrument:
    def __init__(self):
        self.main_counter = pc.Counter(
            "main_counter", "total requests to your redirect page")
        self.redirect_time = pc.Histogram(
            "redirect_time", "this a histogram of the redirect time")
        self.users_counter = pc.Counter(
            "users_counter", "a counter of the users in our platform", ["ip", "browser", "platform", "language"])

    def instrument_now(self, port=8000, addr=''):
        return pc.start_http_server(port, addr=addr)

    def instrument_with_wsgi(self):
        return pc.make_wsgi_app()
