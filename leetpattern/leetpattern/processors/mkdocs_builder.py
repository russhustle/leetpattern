"""MkDocs configuration builder."""

import os
from typing import List

from ..core.config import Config
from ..io.file_manager import FileManager


class MkDocsBuilder:
    """Builds MkDocs configuration from project configs."""
    
    def __init__(self):
        self.file_manager = FileManager()
    
    def generate_config_section(self, config: Config) -> str:
        """Generate MkDocs navigation section for a single config."""
        mkdocs = f"  - {config.name}:\n"
        mkdocs += f"    - Home: content/{config.dir}/index.md\n"
        
        for topic in config.topics.keys():
            md_filename = topic.lower().replace(" ", "_") + ".md"
            mkdocs += f"    - {topic}: content/{config.dir}/{md_filename}\n"
        
        return mkdocs
    
    def build_mkdocs_config(self, configs: List[Config]) -> bool:
        """Build complete MkDocs configuration file."""
        default_mkdocs = os.path.join("utils", "mkdocs.yaml")
        output_mkdocs = "mkdocs.yaml"
        
        if not os.path.exists(default_mkdocs):
            print(f"Warning: Default MkDocs template not found: {default_mkdocs}")
            return False
        
        # Read default template
        lines = self.file_manager.read_file_safe(default_mkdocs).splitlines(keepends=True)
        
        # Generate navigation sections for all configs
        nav_content = ""
        for config in configs:
            nav_content += self.generate_config_section(config) + "\n"
        
        # Insert navigation content at line 3 (0-indexed)
        if len(lines) >= 3:
            lines.insert(3, nav_content)
        else:
            lines.append(nav_content)
        
        # Write output file
        content = ''.join(lines)
        return self.file_manager.write_file_safe(output_mkdocs, content)