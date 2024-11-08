import argparse
import os


def list_files_with_string(folder: str, string: str, present: bool = True):
    files = os.listdir(folder)
    files = [file for file in files if file.endswith(".py")]
    findings = []

    for file in files:
        with open(os.path.join(folder, file), "r") as f:
            content = f.read()
            if present:
                if string in content:
                    findings.append(file)
            else:
                if string not in content:
                    findings.append(file)
    return findings


if __name__ == "__main__":
    folder = "docs/snippets"

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", type=str, default=folder)
    parser.add_argument("-s", "--string", type=str, required=True)
    parser.add_argument("-p", "--present", action="store_true")
    parser.add_argument(
        "-np", "--not-present", action="store_false", dest="present"
    )

    args = parser.parse_args()

    findings = list_files_with_string(args.folder, args.string, args.present)
    findings.sort()

    for file in findings:
        print(file)

    print(f"\nTotal files: {len(findings)}")
