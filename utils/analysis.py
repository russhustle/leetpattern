import os


def list_files_with_string(folder, string, present=True):
    files = os.listdir(folder)
    findings = []
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(folder, file), "r") as f:
                content = f.read()
                if present:
                    if string in content:
                        findings.append(file)
                else:
                    if string not in content:
                        findings.append(file)

    return findings


findings = list_files_with_string("docs/snippets", "# ", present=True)
findings.sort()

for file in findings:
    print(file)

print(len(findings))
