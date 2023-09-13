from slowapi import Limiter
from slowapi.util import get_remote_address

# This creates a rate limiter with a limit of 5 requests per minute for each IP
limiter = Limiter(key_func=get_remote_address)
