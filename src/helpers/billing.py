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
    
def create_product(name="",metadata={}, raw=False):
    response = stripe.Product.create(
    name=name,
    metadata=metadata,
    )

    if raw:
        return response
    else:
        return response.id

def create_price(currency="usd",
                unit_amount="9999",
                interval="month",
                product=None,
                metadata={},
        raw=False):
    if product is None:
        return None
    response = stripe.Price.create(
            currency=currency,
            unit_amount=unit_amount,
            recurring={"interval": interval},
            product=product,
            metadata=metadata
        )
    if raw:
        return response
    stripe_id = response.id 
    return stripe_id
