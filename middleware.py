import falcon

class AuthMiddleware:
    def process_request(self, req, resp):
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')

        challenges = ['Token Type="IPINFO"']

        if token is None:
            description = "Error"

            raise falcon.HTTPUnauthorized(
                title="Auth token required",
                description=description,
            )
            
        if not self._token_is_valid(token, account_id):
            description = (
                'The provided auth token is not valid.'
                'Please request a new token and try again.'
            )

            raise falcon.HTTPUnauthorized(
                title='Authentication required',
                description=description,
            )

    def _token_is_valid(self, token, account_id):
        if token == 'batman' and account_id == 'batman':
            return True

        return False