def simplify_path_stack(path: str) -> str:
    if not path:
        return "/"

    stack = []

    for p in path.split("/"):
        if p == "" or p == ".":
            continue
        if p != "..":
            stack.append(p)
        elif stack:
            stack.pop()
    return "/" + "/".join(stack)


if __name__ == "__main__":
    assert simplify_path_stack("/home/") == "/home"
    assert simplify_path_stack("/../") == "/"
    assert simplify_path_stack("/home//foo/") == "/home/foo"
    assert simplify_path_stack("/a/./b/../../c/") == "/c"
