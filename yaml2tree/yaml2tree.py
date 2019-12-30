import os
import sys
from datetime import date
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


def create_dirs(list_, stack = None):
    if type(list_) is not list:
        raise ValueError(f"bad input data: {list_}")

    if stack is None:  stack = []
    get_dir_name = lambda x: str(x) if type(x) is str or \
                                       type(x) is int or \
                                       type(x) is float or \
                                       type(x) is date \
                                    else None

    last_dir_name = None
    def clear_last_dir_name():
        nonlocal last_dir_name
        if last_dir_name is not None:
            stack.pop()
            last_dir_name = None

    for item in list_:
        dir_name = get_dir_name(item)
        if dir_name:
            clear_last_dir_name()
            stack.append(dir_name)
            create_dir(os.path.sep.join(stack))
            last_dir_name = dir_name
        elif type(item) is list:
            create_dirs(item, stack)
        else:
            raise Exception("bad item: %s" % str(item))
    clear_last_dir_name()


red_fg = "\033[31m"
green_fg = "\033[32m"
cyan_fg = "\033[36m"
default_fg = "\033[39m"

def create_dir(path):
    try:
        os.mkdir(path)
        print(f"{green_fg}created{default_fg}: {path}")
    except FileExistsError:
        print(f"{cyan_fg}exists{default_fg}: {path}")
    except Exception as e:
        print(f"{red_fg}failed{default_fg}: {path} ({type(e).__name__}: {str(e)})")
    else:
        if mode is not None:
            try:    os.chmod(path, mode)
            except: print(f"{red_fg}failed to set mode {mode} on {path}{default_fg}")


def get_yaml(filepath):
    return read_text_file(filepath)


def get_usage():
    return read_text_file(f"{os.path.dirname(__file__)}/usage.md")


def read_text_file(filepath):
    with open(filepath, "rt") as f:
        return f.read()


try:    mode = int(os.environ.get("mode"), 8)
except: mode = None
