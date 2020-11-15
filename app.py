from flask import Flask, jsonify, request
from service import Validation
from payment import Payment

app = Flask(__name__)


@app.route('/ProcessPayment', methods=['POST'])
def process_payment():
    response_object = dict()

    post_data = request.get_json()
    validobject = Validation(post_data)
    check_datatype = validobject.checkrequestdatatype()
    if check_datatype:
        check_param = validobject.validate_params()

        if check_param:
            payobject = Payment(post_data)
            if post_data['Amount'] < 20:
                response = payobject.CheapPaymentGateway()
                if response['ok']:
                    response_object['status'] = 'ok'
                    response_object['statusCode'] = '200'
                else:
                    response_object['status'] = 'internal server error'
                    response_object['statusCode'] = '500'

            elif post_data['Amount'] < 500:

                response = payobject.ExpensivePaymentGateway()
                if response['ok']:
                    response_object['status'] = 'ok'
                    response_object['statusCode'] = '200'

                else:
                    response = payobject.CheapPaymentGateway()
                    if response['ok']:
                        response_object['status'] = 'ok'
                        response_object['statusCode'] = '200'

                    else:
                        response_object['status'] = 'internal server error'
                        response_object['statusCode'] = '500'

            else:
                retry_counter = 3
                for _ in range(retry_counter + 1):
                    response = payobject.PremiumPaymentGateway()
                    if response['ok']:
                        response_object['status'] = 'ok'
                        response_object['statusCode'] = '200'
                        break
                    response_object['status'] = 'internal server error'
                    response_object['statusCode'] = '500'
        else:
            response_object['status'] = 'bad request'
            response_object['statusCode'] = '400'
    else:
        response_object['status'] = 'bad request'
        response_object['statusCode'] = '400'

    return jsonify(response_object)


# driver function
if __name__ == '__main__':
    app.run(debug=True)


