# Hello world program in Python
def main():
    print("Hello, World! v1")


def print_today_and_timezone():
    # use default package for timezone
    from datetime import datetime
    import time


    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Today's date is: {today}")

    timezone = time.tzname[0]
    print(f"Current timezone is: {timezone}")

if __name__ == "__main__":
    main()
    print_today_and_timezone()
