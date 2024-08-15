# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
from decouple import config

STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default="", cast=str)

stripe.api_key = STRIPE_SECRET_KEY  

def create_custom_user(name="", email="",metadata={}, raw=False):
    response = stripe.Customer.create(
    name=name,
    metadata=metadata,
    email=email,
    )

    if raw:
        return response
    else:
        return response.id