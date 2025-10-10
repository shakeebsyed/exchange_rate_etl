import requests
import pandas as pd

def fetch_exchange_data():
    url = 'https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    obs = data.get("observations",[])
    if not obs:
        print("No obs returned from API")
        return pd.DataFrame()
     # Normalize nested dictionaries like {'FXUSDCAD': {'v': '1.37'}}
    df = pd.json_normalize(obs)

    # Converting all columns ending with '.v' to float
    value_cols = [c for c in df.columns if c.endswith('.v')]
    for c in value_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df = df[['d','FXINRCAD.v','FXUSDCAD.v','FXSARCAD.v','FXAUDCAD.v']]

    print(f"Retrieved {len(df)} rows and {len(df.columns)} columns.")
    return df
