from flask import jsonify, make_response


def response_success(data, code=200):
    response = jsonify({
        'data': data,
        'status': "Success"
    })
    return make_response(response, code)


def response_failed(data, code=400):
    response = jsonify({
        'data': data,
        'status': "Failed"
    })
    return make_response(response, code)
