# FastApi Setup

A simple boilerplate setup for an extensible Python FastAPI application.

This boilerplate style separates and groups together related logic, like API-endponints from
their request handling logic

Uses tortoise ORM along with aerich for migrations.

**Note:** Aerich is not as robust as something like django's ORM system which is robust and
awesome, but if you design your Data Model good enough so you don't have to change it all
the time, it's not going to be an issue.
