def hello(name, lang):
    greetings = {"English" : "Hello",
                 "Spanish" : "Hola",
                 "German" : "Hallo"}
    message = f"{greetings[lang]} {name}"
    print(message)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, help="The language to greet in.",
        choices=["English", "Spanish", "German"]
    )

    args = parser.parse_args()

    hello(args.name, args.lang)