# A program that prints a welcome message and runs the interpreter.
import interpreter as reppc


def main():
    """Run the program."""

    # Print a welcome message.
    print("This program is for educational purposes only.")
    print("It is not intended to be used for malicious purposes.")
    print("-----------------------------------------------")
    print("Made by: Team 0x6861636B at arclabs")
    print("Github: github.com/proplayer/repp")
    print("Version: 1.0.0")
    print("-----------------------------------------------")

    # Run the interpreter.
    reppc.reppConsole()


if __name__ == "__main__":
    main()
