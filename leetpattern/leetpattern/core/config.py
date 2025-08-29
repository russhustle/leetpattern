"""Configuration management for LeetPattern."""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import yaml

from ..io.yaml_loader import YamlLoader


@dataclass
class Config:
    """Configuration for a problem set."""
    category: str
    dir: str
    name: str
    topics: Dict[str, List[int]] = field(default_factory=dict)


class ConfigManager:
    """Manages configuration loading and validation."""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = config_dir
        self.yaml_loader = YamlLoader()
        
    def load_main_config(self) -> List[str]:
        """Load the main configuration file containing list of configs."""
        main_config_path = os.path.join(self.config_dir, "main.yaml")
        try:
            configs = self.yaml_loader.load_yaml(main_config_path)
            return [config for config in configs if not config.startswith('#')]
        except Exception as e:
            raise ValueError(f"Failed to load main config: {e}")
    
    def load_topic_config(self, name: str) -> Config:
        """Load configuration for a specific topic."""
        config_path = os.path.join(self.config_dir, f"{name}.yaml")
        try:
            data = self.yaml_loader.load_yaml(config_path)
            return Config(**data)
        except Exception as e:
            raise ValueError(f"Failed to load config '{name}': {e}")
    
    def get_all_configs(self) -> Dict[str, Config]:
        """Get all configurations as a dictionary."""
        config_names = self.load_main_config()
        configs = {}
        
        for name in config_names:
            try:
                configs[name] = self.load_topic_config(name)
            except ValueError as e:
                print(f"Warning: Skipping config '{name}': {e}")
                continue
                
        return configs
    
    def validate_config(self, config: Config) -> bool:
        """Validate a configuration object."""
        required_fields = ['category', 'dir', 'name', 'topics']
        
        for field_name in required_fields:
            if not hasattr(config, field_name):
                return False
                
        if config.category not in ['algorithms', 'sql']:
            return False
            
        return True