import argparse


def convert_name_to_uppercase(name: str) -> str:
    return name.upper()


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a name to uppercase.")
    parser.add_argument("name", help="The name to convert")
    args = parser.parse_args()
    print(convert_name_to_uppercase(args.name))


if __name__ == "__main__":
    main()