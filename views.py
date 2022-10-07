from flask import Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    """
    Perform a query against the database.
    """
    try:
        params = RequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400
    print(params)

    return params, 200

