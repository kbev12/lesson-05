import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/current_time')
def current_time():
    epoch_time = int(time.time())
    return f"Current Time: {epoch_time}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
