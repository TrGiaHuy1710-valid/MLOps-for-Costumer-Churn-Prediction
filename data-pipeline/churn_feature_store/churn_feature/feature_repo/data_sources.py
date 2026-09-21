from feast import FileSource

customer_stats_source = FileSource(
    name="customer_stats_source",
    path="data/processed_period_1.parquet",   # đường dẫn tới parquet của bạn
    timestamp_field="event_timestamp",
    created_timestamp_column="create_timestamp",
)