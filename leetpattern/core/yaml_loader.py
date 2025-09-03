"""YAML file loading utilities."""

import os
from typing import Any, Dict, List, Union

import yaml


class YamlLoader:
    """Handles YAML file loading with error handling."""

    @staticmethod
    def load_yaml(file_path: str) -> Union[Dict[str, Any], List[Any]]:
        """Load YAML file with proper error handling."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
                if data is None:
                    raise ValueError(
                        "YAML file is empty or contains only whitespace"
                    )
                return data
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format in {file_path}: {e}")
        except Exception as e:
            raise IOError(f"Failed to read {file_path}: {e}")

    @staticmethod
    def save_yaml(
        data: Union[Dict[str, Any], List[Any]], file_path: str
    ) -> None:
        """Save data to YAML file."""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as file:
                yaml.safe_dump(
                    data, file, default_flow_style=False, sort_keys=False
                )
        except Exception as e:
            raise IOError(f"Failed to write {file_path}: {e}")
