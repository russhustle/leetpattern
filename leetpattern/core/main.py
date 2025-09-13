from pathlib import Path
from leetpattern import ProblemSetRepository
import yaml
from tqdm import tqdm


def main():
    config_folder = Path("config")
    content_folder = "content"
    main_config = config_folder / "main.yaml"
    with main_config.open("r", encoding="utf-8") as file:
        configs = yaml.safe_load(file)
    for config in tqdm(configs):
        config_name = str(config) + ".yaml"
        config_path = config_folder / config_name
        problem_set = ProblemSetRepository(
            config_path=str(config_path), folder=str(content_folder)
        )
        problem_set.make_topics_md()
        problem_set.make_mkdocs_yaml()
        problem_set.make_readme_md()


if __name__ == "__main__":
    main()
