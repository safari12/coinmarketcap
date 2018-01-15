# coinmarketcap
Coinmarketcap Wrapper

## API Module

### Response Types

`Ticker`
- properties
    - `name`
    - `symbol`
    - `rank`
    - `price`
        - `usd`
        - `btc`
    - `volume`
        - `24h`
            - `usd`
    - `market_cap`
        - `usd`
    - `supply`
        - `available`
        - `total`
    - `percent_change`
        - `1h`
        - `24h`
        - `7d`
    - `last_updated`
    
`GlobalStats`
- properties
    - `total_market_cap`
        - `usd`
    - `total_volume`
        - `24h`
            - `usd`
    - `btc_percentage_market_cap`
    - `active`
        - `currencies`
        - `assets`
        - `markets`
    - `last_updated`

### Public Methods

`get_tickers`
- description: `gets tickers from the market`
- endpoint: `/ticker/` or `/ticker/{coin}`
- method: `get`
- optional params:
    - `(string) coin` - return ticker for a specific coin
    - `(int) start` - return results from rank start and above
    - `(int) limit` - return a maximum of limit results (default is 100 use 0 to return all results)
    - `(string) convert` - return price, 24h volume, and marketcap in terms of another currency
- response type: `Ticker`

`get_global_stats`
- description: `gets stats for the whole market`
- method: `get`
- optional params:
    - `(string) convert` - return price, 24h volume, and marketcap in terms of another currency
- response type: `GlobalStats`
