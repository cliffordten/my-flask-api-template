class Error():

    def internalServerError(self):
        return {
            "message": "Something went wrong, Sever Error",
            "status": 500
        }

    def schemaValidationError(self, *fields):
        return {
            "message": "Request is missing required fields " + fields,
            "status": 400
        }

    def alreadyExistsError(self, field, _id):
        return {
            "message": field + 'with id' + _id + 'already exists',
            "status": 400
        }

    def doesNotExistsError(self, field, _id):
        return {
            "message": field + 'with id' + _id + 'does not exists',
            "status": 400
        }

    def unauthorizedError(self, *data = None):
        if(data):
            return {
                "message": "Invalid " + data,
                "status": 401
            }

        return {
            "message": "You are not authorized to make this request",
            "status": 401
        }
