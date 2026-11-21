import datetime as dt

# Validation Object -- contain Validation Functions
class ValidationFun:
    @staticmethod
    def ask_yes_no(question: str = "Answer yes or no"):
        """Prompts the user for a yes or no answer until a valid response is entered"""
        while True:
            answer = input(f"{question} [YES/NO]: ").strip().lower()
            if answer in ["yes", "y"]:
                return True
            if answer in ["no", "n"]:
                return False
            print("Not a valid option.")
        
    
    @staticmethod
    def is_empty(text: str = "Enter some text"):
        """Prompts the user to enter some text until they actually enter some text"""
        while True:
            user_input = input(f"{text}: ").strip()
            if user_input:
                return user_input
            print("Input cannot be empty.")

    
    @staticmethod
    def valid_number(text: str = "Enter a number", options: list|tuple = None):
        """Prompts for the entry of a number until a valid number or index is entered."""
        if options is not None and not options:
            print("Options cannot be an empty collection.")
            return
        while True:
            try:
                number = int(input(f"{text}: "))
                if options and number - 1 not in range(0, len(options)):
                    print(f"Number must be in range between 1 and {len(options)}")
                    continue
                return number-1 if options else number
            except ValueError:
                print("You must enter an integer number.")

    @staticmethod
    def valid_option(text: str = "Select an option.", options: list|tuple = None):
        """Prompts for input until a valid option is entered"""
        if not options:
            print("An options cannot be empty.")
            return
        options_lower = [str(opt).strip().lower() for opt in options if str(opt).strip() != ""]
        if not options_lower:
            print("An options cannot contain empty strings only.")
            return
        while True:
            option = input(f"{text} {options_lower}: ").strip().lower()
            if option in options_lower:
                return option
            print("Not a valid option.")

    @staticmethod
    def validate_date(text: str = "Enter the date"):
        """prompts the user to enter a date until they enter a date in the future in the correct format"""
        while True:
            user_input = input(f"{text} [DD.MM.YYYY.]: ").strip()
            if not user_input.endswith("."):
                user_input += "."
            try:
                date = dt.datetime.strptime(user_input, "%d.%m.%Y.").date()
            except ValueError:
                print("Date needs to be in format [DD.MM.YYYY.].")
                continue
            if date<dt.date.today():
                print("Date needs to be in future")
                continue
            return date