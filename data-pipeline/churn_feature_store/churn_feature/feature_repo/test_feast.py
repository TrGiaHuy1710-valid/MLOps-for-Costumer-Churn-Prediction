from feast import FeatureStore

store = FeatureStore(repo_path=".")   # chạy trong feature_repo

entity_rows = [{"customer_id": i} for i in range(2, 40)]

FEATURES = [
    "customer_demographics:age",
    "customer_demographics:gender",
    "customer_demographics:tenure_months",
    "customer_demographics:subscription_type",
    "customer_demographics:contract_length",
    "customer_behavior:usage_frequency",
    "customer_behavior:support_calls",
    "customer_behavior:payment_delay_days",
    "customer_behavior:total_spend",
    "customer_behavior:last_interaction_days",
]

df = store.get_online_features(entity_rows=entity_rows, features=FEATURES).to_df()
print(df)