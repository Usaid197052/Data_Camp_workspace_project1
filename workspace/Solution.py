import pandas as pd
import numpy as np

df = pd.read_csv("bank_marketing.csv")
client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']].copy()

client['education'] = client['education'].str.replace('.', '_')
client["education"] = client['education'].replace("unknown", np.NaN)

client['credit_default'] = client['credit_default'].map({
    'yes': 1,
    'no': 0,
    'unknown': 0
}).astype(bool)

client['mortgage'] = client['mortgage'].map({
    'yes': 1,
    'no': 0,
    'unknown': 0
}).astype(bool)

campaign = df[['client_id', 'number_contacts', 'contact_duration',
               'previous_campaign_contacts', 'previous_outcome',
               'campaign_outcome', 'day', 'month']].copy()

campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1, 'failure': 0, "nonexistent":0}).astype(bool)
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': 1, 'no': 0}).astype(bool)


campaign['last_contact_date'] = pd.to_datetime(
    '2022-' + campaign['month'] + '-' + campaign['day'].astype(str),
    format='%Y-%b-%d',
    errors='coerce'
)


campaign = campaign.drop(columns=['day', 'month'])


economics = df[['client_id', 'cons_price_idx', 'euribor_three_months']].copy()


client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)