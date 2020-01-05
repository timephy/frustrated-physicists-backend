import sqlite3
import datetime


current_total_clicks = 900
current_day_clicks = 500
current_hour_clicks = 100


async def add_click(name: str, comment: str):
    """Stores a click to the database and returns this click object (dict)."""
    click = {"date": 123456789, "name": name, "comment": comment}
    global current_total_clicks
    global current_day_clicks
    global current_hour_clicks
    current_total_clicks += 1
    current_day_clicks += 1
    current_hour_clicks += 1
    # db.store(click)
    return click


async def get_last_clicks(count: int = 1000):
    """Returns last `count` clicks from the database."""
    # return db.last(count)
    return [{"date": 123456789, "name": "Name", "comment": "Comment"}] * 5


async def get_total_clicks():
    """Returns the total amout of clicks."""
    global current_total_clicks
    return current_total_clicks


async def get_day_clicks():
    """Returns the amout of clicks today."""
    global current_day_clicks
    return current_day_clicks


async def get_hour_clicks():
    """Returns the amout of clicks in the last hour."""
    global current_hour_clicks
    return current_hour_clicks


async def get_stats():
    # TODO: await together
    return {
        "total": await get_total_clicks(),
        "day": await get_day_clicks(),
        "hour": await get_hour_clicks()
    }
