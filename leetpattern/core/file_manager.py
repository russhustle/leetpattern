"""File management utilities."""

import os


class FileManager:
    """Handles file operations with proper error handling."""

    @staticmethod
    def check_create_file(file_path: str) -> None:
        """Create an empty file if it does not exist."""
        if not os.path.exists(file_path):
            try:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("")
                print(f"Created file: {file_path}")
            except Exception as e:
                print(f"Warning: Failed to create file {file_path}: {e}")
        else:
            print("File already exists.")

    @staticmethod
    def is_file_empty(file_path: str) -> bool:
        """Check if a file exists and is not empty."""
        if not os.path.exists(file_path):
            return True
        try:
            return os.path.getsize(file_path) == 0
        except OSError:
            return True

    @staticmethod
    def file_exists_and_not_empty(file_path: str) -> bool:
        """Check if a file exists and is not empty."""
        return os.path.exists(file_path) and not FileManager.is_file_empty(
            file_path
        )

    @staticmethod
    def read_file_safe(file_path: str) -> str:
        """Read file content safely with error handling."""
        if not os.path.exists(file_path):
            return ""

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Warning: Failed to read file {file_path}: {e}")
            return ""

    @staticmethod
    def write_file_safe(file_path: str, content: str) -> bool:
        """Write content to file safely with error handling."""
        try:
            # Only create directory if file_path contains a directory
            dir_path = os.path.dirname(file_path)
            if dir_path:  # Only create if there's actually a directory path
                os.makedirs(dir_path, exist_ok=True)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error: Failed to write file {file_path}: {e}")
            return False

    @staticmethod
    def extract_docstring(file_path: str) -> str:
        """Extract docstring from a Python file."""
        if not FileManager.file_exists_and_not_empty(file_path):
            return ""

        content = FileManager.read_file_safe(file_path).strip()
        if not content:
            return ""

        # Look for triple-quoted docstring at the beginning of the file
        if content.startswith('"""'):
            end_idx = content.find('"""', 3)
            if end_idx != -1:
                return content[3:end_idx].strip() + "\n\n"

        return ""

    @staticmethod
    def extract_js_comment(file_path: str) -> str:
        """Extract JSDoc comment from a JavaScript file."""
        if not FileManager.file_exists_and_not_empty(file_path):
            return ""

        content = FileManager.read_file_safe(file_path).strip()
        if not content:
            return ""

        # Look for JSDoc comment at the beginning of the file
        if content.startswith("/**"):
            end_idx = content.find("*/", 3)
            if end_idx != -1:
                # Clean up JSDoc comment formatting
                comment_content = content[3:end_idx].strip()
                lines = comment_content.split("\n")
                cleaned_lines = []
                for line in lines:
                    cleaned_line = line.strip()
                    if cleaned_line.startswith("*"):
                        cleaned_line = cleaned_line[1:].strip()
                    if cleaned_line and not cleaned_line.startswith("@"):
                        cleaned_lines.append(cleaned_line)

                if cleaned_lines:
                    return "\n".join(cleaned_lines) + "\n\n"

        return ""

    @staticmethod
    def remove_empty_files(
        directories: list[str], extensions: list[str]
    ) -> None:
        """Remove empty files from specified directories."""
        for directory in directories:
            if not os.path.exists(directory):
                continue

            try:
                for filename in os.listdir(directory):
                    if any(filename.endswith(ext) for ext in extensions):
                        file_path = os.path.join(directory, filename)
                        if FileManager.is_file_empty(file_path):
                            os.remove(file_path)
                            print(f"Removed empty file: {file_path}")
            except Exception as e:
                print(f"Warning: Failed to process directory {directory}: {e}")
