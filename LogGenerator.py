import random
from datetime import datetime, timedelta

LEVELS = ["INFO", "WARN", "ERROR"]
ENDPOINTS = ["/login", "/home", "/profile", "/payment", "/search", "/logout"]
STATUS_CODES = {
    "INFO": [200],
    "WARN": [400, 404],
    "ERROR": [500, 502, 503]
}

def generate_logs(filename="large.log", lines=100_000):
    start_time = datetime.now() - timedelta(hours=5)

    with open(filename, "w") as f:
        for i in range(lines):
            timestamp = start_time + timedelta(seconds=i * random.randint(1, 3))
            level = random.choice(LEVELS)
            endpoint = random.choice(ENDPOINTS)
            status = random.choice(STATUS_CODES[level])
            ip = f"192.168.{random.randint(0,10)}.{random.randint(1,255)}"

            log_line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {level} {endpoint} {status} {ip}\n"
            f.write(log_line)

    print(f"Generated {lines} log entries in {filename}")

if __name__ == "__main__":
    generate_logs()

# import random
# from datetime import datetime,timedelta,time,datetime

# LEVELS=["INFO","WARN","ERROR"]

# ENDPOINTS=["/login","/home","/profile","/payment","/search","/logout"]

# STATUS_CODES={
#     "INFO":[200],
#     "WARN":[400,404],
#     "ERROR":[500,502,504]
# }

# def generate_logs(filename="large.log",lines=1000):
#     start_time=datetime.now()-timedelta(hours=5)
#     with open(filename,"w") as f:
#         for i in range(lines):
#             timestamp=start_time+timedelta(seconds=i*random.randint(1,3))
#             level=random.choice(LEVELS)
#             endpoint=random.choice(ENDPOINTS)
#             status=random.choice(STATUS_CODES[level])
#             ip=f"192.168.{random.randint(0,10)},{random.randint(1,255)}"
#             log_line=f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {level} {endpoint} {status} {ip}\n"
#             f.write(log_line)

# generate_logs()