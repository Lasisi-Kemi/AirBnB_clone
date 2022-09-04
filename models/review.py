""" the review module """

from models.base_model import BaseModel


class Review(BaseModel):
    """ the review model """
    place_id = ""
    user_id = ""
    text = ""
