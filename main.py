import os
from flask import Flask, redirect, request

import config
import instrumenting


conf = config.Config()
inst = instrumenting.Instrument()

app = Flask(__name__)


@app.route(conf.route)
@inst.redirect_time.time()
def hello():
    inst.main_counter.inc()
    ip = request.remote_addr
    browser = request.user_agent.browser
    platform = request.user_agent.platform
    language = request.user_agent.language

    inst.users_counter.labels(ip=ip, browser=browser,
                              platform=platform, language=language).inc()
    return redirect(conf.focus_url, code=conf.code_redirect)


if __name__ == '__main__':
    inst.instrument_now(port=int(conf.instrument_port))
    app.run(host='0.0.0.0', port=int(conf.port))
