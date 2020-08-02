from app.app import api, app

from resources.hello import *


api.add_resource(Hello, '/hello')



if __name__ == '__main__':
    app.run()