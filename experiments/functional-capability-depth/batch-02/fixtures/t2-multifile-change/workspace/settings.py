DEFAULT_RETRIES = 3


def parse_retries(env):
    raw = env.get("APP_RETRIES")
    if raw is None:
        return DEFAULT_RETRIES
    return int(raw)
