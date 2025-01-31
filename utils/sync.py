import os


def sync_files(directory):
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

    all_files = sql_files.union(py_files)

    i = 0
    for file in all_files:
        sql_path = os.path.join(directory, file + ".sql")
        py_path = os.path.join(directory, file + ".py")

        if not os.path.exists(sql_path):
            open(sql_path, "w").close()
            i += 1
            print(f"Created {sql_path}")

        if not os.path.exists(py_path):
            open(py_path, "w").close()
            i += 1
            print(f"Created {py_path}")

    print(f"Created {i} files")


if __name__ == "__main__":
    directory = "src/sql"  # Change this to your folder path
    sync_files(directory)
