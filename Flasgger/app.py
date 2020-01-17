from src import app
from flasgger import swag_from


@swag_from('docs/home.yml')
@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
