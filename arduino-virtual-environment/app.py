from flask_graphql import GraphQLView

from api_config import (
    app
)
from models.schema import schema

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return 'Hola Mundo desde Flask Server'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)