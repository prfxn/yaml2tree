import os
import sys
import yaml


def main():
    num_args = len(sys.argv) - 1

    try:
        if num_args == 0:
            print(get_usage())

        elif num_args == 1:
            yaml_ = get_yaml(sys.argv[1])
            list_ = yaml.safe_load(yaml_)
            create_dirs(list_)

        else:
            raise ValueError(f"too many arguments\n{get_usage()}")

    except Exception as e:
        print(f"{type(e).__name__}:", e, file=sys.stderr)
        return 1

    return 0


def create_dirs(list_):
    if type(list_) is not list:
        raise ValueError(f"bad input data: {list_}")
    raise NotImplementedError()


def get_yaml(filepath):
    return read_text_file(filepath)


def get_usage():
    return read_text_file(f"{os.path.dirname(__file__)}/usage.md")


def read_text_file(filepath):
    with open(filepath, "rt") as f:
        return f.read()


try:    mode = int(os.environ.get("mode"), 8)
except: mode = 0o755

try:    noop = bool(os.environ.get("noop"))
except: noop = False
