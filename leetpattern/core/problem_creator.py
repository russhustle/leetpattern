"""Problem file creation functionality."""

import os
from pathlib import Path
from typing import Optional


class ProblemCreator:
    """Creates problem files based on templates."""
    
    def __init__(self, solutions_dir: str = "leetpattern/solutions"):
        self.solutions_dir = Path(solutions_dir)
        self.python_dir = self.solutions_dir / "python"
        
    def _get_problem_range_dir(self, qid: int) -> Path:
        """Get the directory for a problem ID based on its range."""
        if 1 <= qid <= 300:
            return self.python_dir / "0001_0300"
        elif 301 <= qid <= 600:
            return self.python_dir / "0301_0600"
        elif 601 <= qid <= 900:
            return self.python_dir / "0601_0900"
        elif 901 <= qid <= 1200:
            return self.python_dir / "0901_1200"
        elif 1201 <= qid <= 1500:
            return self.python_dir / "1201_1500"
        elif 1501 <= qid <= 1800:
            return self.python_dir / "1501_1800"
        elif 1801 <= qid <= 2100:
            return self.python_dir / "1801_2100"
        elif 2101 <= qid <= 2400:
            return self.python_dir / "2101_2400"
        elif 2401 <= qid <= 2700:
            return self.python_dir / "2401_2700"
        elif 2701 <= qid <= 3000:
            return self.python_dir / "2701_3000"
        else:
            return self.python_dir / "3001_3300"
    
    def _generate_problem_template(self, qid: int, title: str, description: Optional[str] = None) -> str:
        """Generate a problem file template."""
        formatted_qid = f"{qid:04d}"
        function_name = self._title_to_function_name(title)
        
        template = f'''"""
- Problem {qid}: {title}
- {description or "TODO: Add problem description"}
- Approach: TODO: Add approach description
- Time Complexity: TODO: Add time complexity
- Space Complexity: TODO: Add space complexity
"""

from typing import List


def {function_name}():
    """TODO: Implement solution."""
    pass


if __name__ == "__main__":
    # TODO: Add test cases
    pass
'''
        return template
    
    def _title_to_function_name(self, title: str) -> str:
        """Convert problem title to function name."""
        # Convert to snake_case and remove special characters
        name = title.lower().replace(" ", "_").replace("-", "_")
        # Remove non-alphanumeric characters except underscores
        name = "".join(c for c in name if c.isalnum() or c == "_")
        # Remove multiple underscores
        while "__" in name:
            name = name.replace("__", "_")
        # Remove leading/trailing underscores
        name = name.strip("_")
        return name or "solution"
    
    def _title_to_filename(self, qid: int, title: str) -> str:
        """Convert problem title to filename."""
        formatted_qid = f"{qid:04d}"
        filename = self._title_to_function_name(title)
        return f"{formatted_qid}_{filename}.py"
    
    def create_problem_file(self, qid: int, title: str, description: Optional[str] = None, force: bool = False) -> bool:
        """Create a problem file.
        
        Args:
            qid: Problem ID
            title: Problem title
            description: Optional problem description
            force: Overwrite existing file if True
            
        Returns:
            True if file was created successfully, False otherwise
        """
        try:
            # Get the target directory
            target_dir = self._get_problem_range_dir(qid)
            
            # Create directory if it doesn't exist
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename
            filename = self._title_to_filename(qid, title)
            file_path = target_dir / filename
            
            # Check if file already exists
            if file_path.exists() and not force:
                print(f"File already exists: {file_path}")
                print("Use --force to overwrite")
                return False
            
            # Generate template content
            content = self._generate_problem_template(qid, title, description)
            
            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Created problem file: {file_path}")
            return True
            
        except Exception as e:
            print(f"Error creating problem file: {e}")
            return False
    
    def list_existing_problems(self, qid_range: Optional[tuple] = None) -> list:
        """List existing problem files.
        
        Args:
            qid_range: Optional tuple of (min_qid, max_qid) to filter results
            
        Returns:
            List of problem files with their QIDs
        """
        problems = []
        
        if not self.python_dir.exists():
            return problems
        
        for range_dir in self.python_dir.iterdir():
            if not range_dir.is_dir():
                continue
                
            for problem_file in range_dir.glob("*.py"):
                try:
                    # Extract QID from filename
                    qid_str = problem_file.name[:4]
                    qid = int(qid_str)
                    
                    # Filter by range if specified
                    if qid_range and (qid < qid_range[0] or qid > qid_range[1]):
                        continue
                    
                    problems.append({
                        'qid': qid,
                        'filename': problem_file.name,
                        'path': problem_file
                    })
                except ValueError:
                    continue
        
        return sorted(problems, key=lambda x: x['qid'])