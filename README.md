# coinmarketcap

Description
-----------
Coinmarketcap Client Wrapper

Installation
------------

```bash
// clone through ssh
git clone git@github.com:safari12/coinmarketcap.git 

// clone through https
git clone https://github.com/safari12/coinmarketcap.git

cd coinmarketcap
python setup.py install
```

Usage Examples
--------------

```python
from coinmarketcap import api
public_api = api.Public()

# get tickers for a coin
tickers = public_api.get_tickers(coin='bitcoin').json()

# get all tickers
tickers = public_api.get_tickers().json()

# get global stats
global_stats = public_api.get_global_stats().json()
```

Documentation
-------------

#### API Module Public Methods

`get_tickers`
- description: `gets tickers from the market`
- endpoint: `/ticker/` or `/ticker/{coin}`
- method: `get`
- optional params:
    - `(string) coin` - return ticker for a specific coin
    - `(int) start` - return results from rank start and above
    - `(int) limit` - return a maximum of limit results (default is 100 use 0 to return all results)
    - `(string) convert` - return price, 24h volume, and marketcap in terms of another currency

`get_global_stats`
- description: `gets stats for the whole market`
- method: `get`
- optional params:
    - `(string) convert` - return price, 24h volume, and marketcap in terms of another currency
