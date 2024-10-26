#!/usr/bin/env python3

import datetime as dt
from typing import Dict, List, Union

# display config
font_family: str = "Ubuntu"
font_size: int = 11

# types
Goal = Dict[str, Union[str, dt.datetime]]

# List of goals with titles and target dates for countdown tracking. The first goal
# will be shown in app bar. Rest of them will be shown in dropdown on click.
goals: List[Goal] = [
    {
        "title": "You have: ",
        "target": dt.datetime(
            year=2026,
            month=3,
            day=3,
            hour=10,
            minute=0,
            second=0,
        ),
    },
    {
        "title": "First Assignment: ",
        "target": dt.datetime(
            year=2027,
            month=11,
            day=6,
            hour=23,
            minute=59,
            second=59,
        ),
    },
]


def display_timer(goal: Goal):
    now: dt.datetime = dt.datetime.now().replace(microsecond=0)

    title: str = goal["title"]
    target: dt.datetime = goal["target"]
    target = target.replace(microsecond=0)

    time_left: dt.timedelta = target - now

    if time_left.total_seconds() < 0:
        print(f"{title}%s|font='{font_family}' size={font_size}" % "Time up!")
        return

    print(f"{title}%s|font='{font_family}' size={font_size}" % time_left)


def countdown():
    if goals is None or len(goals) == 0:
        print("You have no goals!")

    display_timer(goals[0])
    print("---")

    for i, goal in enumerate(goals):
        if i == 0:
            continue
        display_timer(goal)


countdown()
