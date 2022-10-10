import random
from typing import Any, List


def get_random_index_from_list(some_list: List[Any]) -> Any:
    random_index = random.randint(0, len(some_list) - 1)
    return some_list[random_index]
