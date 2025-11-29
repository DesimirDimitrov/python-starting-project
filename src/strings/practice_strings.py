"""Place for string practice exercises."""


def example_concat(first: str, last: str) -> str:
    full = first + " " + last
    return full


def example_format(name: str, age: int) -> str:
    return f"My name is {name} and I am {age} years old."


if __name__ == "__main__":
    # Try changing these values while learning
    print(example_concat("Ada", "Lovelace"))
    print(example_format("Ada", 36))
