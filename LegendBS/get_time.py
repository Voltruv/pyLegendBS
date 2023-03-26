global time
global unit
def get_time(time: int):
    if time >= 86400:
        time = int(time / (60 * 60 * 24))
        unit = "days"
    elif time >= 3600 < 86400:
        time = int(time / (60 * 60))
        unit = "hours"
    elif time >= 60 < 3600:
        time = int(time / 60)
        unit = "minutes"
    return f" {time} {unit}"
