import os
import requests
from fastapi import status


class ProductController:
    product_api_base_url = os.environ.get('PRODUCT_API_BASE_URL')

    @classmethod
    def get_product_details(cls, product_id):
        url = f'{cls.product_api_base_url}{product_id}/'

        response = requests.get(url)

        response.raise_for_status()

        return response.json()

    @classmethod
    def does_product_exists(cls, product_id):
        try:
            details = cls.get_product_details(product_id)
            return details
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == status.HTTP_404_NOT_FOUND:
                return None
            raise e
