from dataclasses import dataclass, field
from typing import Dict, List

import yaml


@dataclass
class Data:
    dir: str
    name: str
    topics: Dict[str, List[int]] = field(default_factory=dict)


def load_config_yaml(file_path: str) -> Data:
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        return Data(**data)


code = (
    lambda filename: f"""
=== "Python"

    ```python
    --8<-- "{filename}.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/{filename}.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/{filename}.ts"
    ```
"""
)
