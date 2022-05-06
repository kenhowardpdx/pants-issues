import sys


def say_hello(name="world"):
    try:
        if len(name) <= 2:
            raise Exception("name must be longer than 2 characters")
        print(f"hello, {name}!")
        return 0
    except (Exception) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    name = "world"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    sys.exit(say_hello(name))
