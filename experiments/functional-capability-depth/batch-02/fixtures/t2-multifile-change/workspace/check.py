from settings import parse_retries
from worker import build_job

assert parse_retries({}) == 3
assert parse_retries({"APP_RETRIES": "0"}) == 0
assert parse_retries({"APP_RETRIES": "5"}) == 5
assert parse_retries({"APP_RETRIES": ""}) == 3
assert parse_retries({"APP_RETRIES": "bad"}) == 3
assert parse_retries({"APP_RETRIES": "-1"}) == 3
assert parse_retries({"APP_RETRIES": "6"}) == 3

assert build_job({"APP_RETRIES": "2"}) == {"name": "sync", "retries": 2}
assert build_job({"APP_RETRIES": "bad"}) == {"name": "sync", "retries": 3}

print("ok")
