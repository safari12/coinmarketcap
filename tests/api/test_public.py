import unittest

import requests_mock

from coinmarketcap import api


class TestPublic(unittest.TestCase):

    def setUp(self):
        self.adapter = requests_mock.Adapter()
        self.public_api = api.Public(
            base_url='mock://coinmarketcap/',
            transport_adapter=self.adapter
        )

    def test_get_tickers_with_no_params(self):
        expected_response = 'test_tickers'

        self.adapter.register_uri(
            method='GET',
            url='/ticker/',
            text=expected_response
        )

        actual_response = self.public_api.get_tickers().text

        self.assertEqual(actual_response, expected_response)

    def test_get_tickers_with_coin_param(self):
        expected_response = 'test_tickers'

        self.adapter.register_uri(
            method='GET',
            url='/ticker/bitcoin/',
            text=expected_response
        )

        actual_response = self.public_api.get_tickers(
            coin='bitcoin'
        ).text

        self.assertEqual(actual_response, expected_response)
