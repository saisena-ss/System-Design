from abc import ABC, abstractmethod
from config import DATABASES

class Sharding(ABC):
    @abstractmethod
    def get_shard(self, user_name):
        pass

class RangeSharding(Sharding):
    '''
    selects the right shard based on first character of the user_name,
    if first letter starts with A or B or C, then choose first shard else second one.
    '''
    def get_shard(self, user_id):
        if user_id%2==0:
            return DATABASES[0]
        return DATABASES[1]
    

class ShardingFactory:
    @staticmethod
    def get_sharding_strategy(strategy_name):
        if strategy_name == 'range':
            return RangeSharding()
        else:
            raise ValueError(f"Unknown sharding strategy: {strategy_name}")
