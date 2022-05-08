# FastApi Setup

A simple boilerplate setup for a Python FastAPI application.

This boilerplate style separates and groups together related logic, like API-endponints from
their request handling logic

There is another style which contains together the endpoint, handlers and it's own db schema
separately in a coupled group, if you prefer that style; then I have uploaded that [here]()

Uses tortoise ORM along with aerich for migrations.

**Note:** It's not as robust as something like django's ORM system which is robust and
awesome, but if you design your Data Model good enough so you don't have to change it all
the time, it's not going to be an issue.
