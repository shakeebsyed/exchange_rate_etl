import pandas as pd

def clean_exchange_data(df):
    # Flatten columns like {'FXUSDCAD.v': value}
    df = df.rename(columns=lambda x: x.replace('.v', ''))
    df['d'] = pd.to_datetime(df['d'])

    # Convert rate columns to numeric
    rate_cols = [c for c in df.columns if c.startswith('FX')]
    for c in rate_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    # Drop empty rows
    df = df.dropna(subset=rate_cols)
    return df
