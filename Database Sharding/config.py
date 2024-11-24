# config.py

DATABASES = {
    'shard1': 'postgresql://user:password@localhost/shard1',
    'shard2': 'postgresql://user:password@localhost/shard2',
}

SHARDING_STRATEGIES = {
    'range': 'range_based_sharding',
    'hash': 'hash_based_sharding'
}
