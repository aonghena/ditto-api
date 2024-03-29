import falcon
import bjoern
from side import detect, find, status, upload

app = falcon.API()

app.add_route('/detect/', detect())
app.add_route('/find/', find())
app.add_route('/health/', status())
app.add_route('/photo/', upload())

if __name__ == '__main__':
    print("Server Started")
    bjoern.listen(app, '0.0.0.0', 6978)
    bjoern.run()