# coinmarketcap
Coinmarketcap Wrapper

## API Module

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

`get_global_stats`
- description: `gets stats for the whole market`
- method: `get`
- optional params:
    - `(string) convert` - return price, 24h volume, and marketcap in terms of another currency
