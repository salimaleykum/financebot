# financebot
Multi-Purpose Financial Assistant Bot

We have used many APIs and methods to create a multi purpose telegram bot that will help everyone with some financial tricks.

APIs in the project:

1) EXCHANGERATE_API

To check and show the actual price of different currencies in tenge, we used the ExchangeRate-API. This API provides currency conversion rates for 161 currencies and is perfect for SaaS, dashboards, and e-commerce1. The API is easy to use and provides accurate and reliable exchange rate data from multiple sources1.

To use the API, you will need to sign up on the Finnhub website to obtain an API key1. Once you have the API key, you can use it to send an HTTP GET request to the API endpoint using the requests.get() method in Python2. The API returns the response in JSON format, which can be easily parsed and read using the json module in Python2.To check and show the actual price of different currencies in tenge, we used the ExchangeRate-API. This API provides currency conversion rates for 161 currencies and is perfect for SaaS, dashboards, and e-commerce1. The API is easy to use and provides accurate and reliable exchange rate data from multiple sources1.

To use the API, you will need to sign up on the Finnhub website to obtain an API key1. Once you have the API key, you can use it to send an HTTP GET request to the API endpoint using the requests.get() method in Python2. The API returns the response in JSON format, which can be easily parsed and read using the json module in Python

2) Alpha Vantage API

To check and show the actual price of different stocks, we used the Alpha Vantage API. This API provides real-time financial data and most used finance indicators in a simple JSON or pandas format 1. The API is free to use and provides accurate and reliable exchange rate data from multiple sources 1.

To use the API, you will need to sign up on the Alpha Vantage website to obtain an API key 1. Once you have the API key, you can use it to send an HTTP GET request to the API endpoint using the requests.get() method in Python 1. The API returns the response in JSON format, which can be easily parsed and read using the json module in Python 1.

3) min-api.cryptocompare
To check the actual cryptocurrency price, we used min-api.cryptocompare. This API provides high-quality historical and real-time trade, order book, and volume data through market-leading REST and WebSocket APIs 1.
You can use the cryptocompare Python package to get the price of a cryptocurrency. 
