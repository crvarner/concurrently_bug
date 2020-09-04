from flask import Flask

import logging
import time
import sys 

app = Flask(__name__)



""" logging config """
logging.captureWarnings(True)
logging.Formatter.converter = time.gmtime

handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(logging.Formatter('%(asctime)s | %(name)10s | %(levelname)6s | %(message)s'))
handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)6s | %(message)s'))
handler.setLevel(logging.DEBUG)

main_log = logging.getLogger()
main_log.setLevel(logging.INFO)
main_log.propagate = False
main_log.addHandler(handler)

werkzeug_log = logging.getLogger('werkzeug')
werkzeug_log.setLevel(logging.ERROR)
werkzeug_log.propagate = False
werkzeug_log.addHandler(handler)

log = logging.getLogger(__name__)



@app.route('/')
def test():
    log.info("log.info")
    log.error("log.error")
    raise Exception("ERROR")
    return "test", 200
    
