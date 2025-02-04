import os
import re


def sync_sql_files(directory):
    sql_files = {
        os.path.splitext(f)[0]
        for f in os.listdir(directory)
        if f.endswith(".sql")
    }
    py_files = {
        os.path.splitext(f)[0]
        for f in os.listdir(directory)
        if f.endswith(".py")
    }
    txt_files = {
        os.path.splitext(f)[0]
        for f in os.listdir(directory)
        if f.endswith(".txt")
    }

    all_files = sql_files.union(py_files).union(txt_files)

    i = 0
    for file in all_files:
        sql_path = os.path.join(directory, file + ".sql")
        py_path = os.path.join(directory, file + ".py")
        txt_path = os.path.join(directory, file + ".txt")

        if not os.path.exists(sql_path):
            open(sql_path, "w").close()
            i += 1

        if not os.path.exists(py_path):
            open(py_path, "w").close()
            i += 1

        if not os.path.exists(txt_path):
            open(txt_path, "w").close()
            i += 1

    print(f"Created {i} files")


def sync_files(directory):
    py_folder = os.path.join(directory)
    cpp_folder = os.path.join(directory, "cpp")
    cpp_default_file_path = os.path.join("utils", "default.cc")
    ts_folder = os.path.join(directory, "ts")

    pattern = re.compile(r"^\d{4}_")

    py_files = {
        os.path.splitext(f)[0]
        for f in os.listdir(py_folder)
        if f.endswith(".py") and pattern.match(f)
    }
    cpp_files = {
        os.path.splitext(f)[0]
        for f in os.listdir(cpp_folder)
        if f.endswith(".cc") and pattern.match(f)
    }
    ts_files = {
        os.path.splitext(f)[0]
        for f in os.listdir(ts_folder)
        if f.endswith(".ts") and pattern.match(f)
    }

    all_files = py_files.union(cpp_files).union(ts_files)

    i = 0
    for file in all_files:
        py_path = os.path.join(py_folder, file + ".py")
        cpp_path = os.path.join(cpp_folder, file + ".cc")
        ts_path = os.path.join(ts_folder, file + ".ts")

        if not os.path.exists(py_path):
            open(py_path, "w").close()
            i += 1

        if not os.path.exists(cpp_path):
            with open(cpp_default_file_path, "r") as f:
                with open(cpp_path, "w") as f2:
                    f2.write(f.read())
            i += 1

        if not os.path.exists(ts_path):
            open(ts_path, "w").close()
            i += 1

    print(f"Created {i} files")


if __name__ == "__main__":
    sync_files("src")
    sync_sql_files("src/sql")
