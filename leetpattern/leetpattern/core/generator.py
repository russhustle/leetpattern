"""Main documentation generator orchestrating all components."""

from typing import Dict, List

from .config import Config, ConfigManager
from .problem import ProblemRepository
from ..processors.markdown_processor import MarkdownProcessor
from ..processors.mkdocs_builder import MkDocsBuilder


class DocumentationGenerator:
    """Main class for generating LeetCode pattern documentation."""
    
    def __init__(self, config_dir: str = "config"):
        self.config_manager = ConfigManager(config_dir)
        self.problem_repo = ProblemRepository()
        self.markdown_processor = MarkdownProcessor()
        self.mkdocs_builder = MkDocsBuilder()
    
    def generate_single_config(self, config_name: str) -> bool:
        """Generate documentation for a single configuration."""
        try:
            config = self.config_manager.load_topic_config(config_name)
            
            if not self.config_manager.validate_config(config):
                print(f"Error: Invalid configuration for '{config_name}'")
                return False
            
            print(f"Generating documentation for {config.name}...")
            
            # Create topic files
            success = True
            for topic, problem_qids in config.topics.items():
                if not self.markdown_processor.create_topic_file(config, topic, problem_qids):
                    print(f"Error: Failed to create topic file for '{topic}'")
                    success = False
            
            # Create index file
            if not self.markdown_processor.create_index_file(config):
                print(f"Error: Failed to create index file for '{config_name}'")
                success = False
            
            return success
            
        except Exception as e:
            print(f"Error generating documentation for '{config_name}': {e}")
            return False
    
    def generate_all_configs(self) -> bool:
        """Generate documentation for all configurations."""
        try:
            configs = self.config_manager.get_all_configs()
            
            if not configs:
                print("No configurations found")
                return False
            
            # Generate documentation for each config
            success = True
            for config_name, config in configs.items():
                if not self.generate_single_config(config_name):
                    success = False
            
            # Build MkDocs configuration
            config_list = list(configs.values())
            if not self.mkdocs_builder.build_mkdocs_config(config_list):
                print("Error: Failed to build MkDocs configuration")
                success = False
            
            if success:
                print("Documentation generation completed successfully!")
            else:
                print("Documentation generation completed with some errors.")
            
            return success
            
        except Exception as e:
            print(f"Error during documentation generation: {e}")
            return False
    
    def create_problem_files(self, qid: int) -> bool:
        """Create problem files for a given LeetCode question ID."""
        problem = self.problem_repo.get_problem(qid)
        if not problem:
            print(f"Error: Problem {qid} not found")
            return False
        
        print(f"Creating files for problem {qid}: {problem.title}")
        
        # Note: File creation is now disabled by default
        # This method is kept for compatibility but does nothing
        print("Auto file creation is disabled. Please create files manually if needed.")
        return True