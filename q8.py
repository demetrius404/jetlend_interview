from typing import Dict, List
import json


# alternative solution calculate hash for each item via pickle
def deduplicate(source: List[Dict]) -> List[Dict]:
    # dirty hack :) - serialize each item via json
    serialized_items = list()
    for item in source:
        serialized_item = json.dumps(item, sort_keys=True)
        if serialized_item not in serialized_items:
            serialized_items.append(serialized_item)
    return [json.loads(serialized_item) for serialized_item in serialized_items]


if __name__ == "__main__":
    origin = [
        {"key1": "value1"},
        {"k1": "v1", "k2": "v2", "k3": "v3"},
        {},
        {},
        {"key1": "value1"},
        {"key1": "value1"},
        {"key2": "value2"}
    ]

    expect = [
        {"key1": "value1"},
        {"k1": "v1", "k2": "v2", "k3": "v3"},
        {},
        {"key2": "value2"}
    ]

    actual = deduplicate(origin)
    print(actual)
    print(expect)
    print(json.dumps(actual, sort_keys=True) == json.dumps(expect, sort_keys=True))



