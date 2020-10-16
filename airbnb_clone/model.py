'''Predicts airbnb rental price based on parameters.'''


def predict_price(rental_parameters):
    """Predicts airbnb rental price based on parameters.

    Args:
        rental_parameters (list): List of user-selected parameters

    Returns:
        float: Predicted price of rental property
    """

    params = rental_parameters
    if len(params) > 0:
        return "Success"
    else:
        return "Failure" # PLACEHOLDER

