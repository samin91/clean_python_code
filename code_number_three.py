"""
This module simulates user activity reporting.
"""

import random
import datetime


def is_active() -> bool:
    """
    Simulate checking if a user is active.
    Returns:
        bool: True if user is active, False otherwise.
    """
    return bool(random.randint(0, 1))


def get_active_user(users: list[str]) -> list[str]:
    """
    Simulate getting active users from a list.

    Parameters:
        users (list[str]): List of user names.
    Returns:
        list[str]: List of active users.
    """
    active_users = [u for u in users if is_active()]

    return active_users


def print_report(users: list[str]) -> None:
    """
    Print a report of active users.
    Parameters:
        users (list[str]): List of active user names.
    """
    today = datetime.date.today()
    print(f"Active Users Report for {today}")
    print("------------------------------")
    for u in users:
        print(f"User: {u} is active")
    print("Total active users: ", len(users))


def main():
    """
    Main function to demonstrate user activity reporting.
    """
    users = ["alice", "bob", "charlie", "dave"]
    u = get_active_user(users)
    print_report(u)


if __name__ == "__main__":
    main()
