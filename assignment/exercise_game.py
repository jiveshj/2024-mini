"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json
import requests
import sys

database_api_url = "https://senior-design-a96f3-default-rtdb.firebaseio.com/data.json"
#flask_server_url = "http://192.168.0.74:1111/post_data"
api_key = "AIzaSyDSfGMO0UbvSRRcCq0SgVQ82493k5_G1iM"
auth_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=" + api_key



N: int = 10
sample_ms = 10.0
on_ms = 500


def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None], idToken) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    add = 0
    for i in range(len(t_good)):
      add+=t_good[i]
    data = {'minimum': min(t_good), 'maximum':max(t_good),'AvgResponseTime':add/len(t_good),'score':float((len(t)-misses)/len(t))}
    print(data['minimum'])
    print(data['maximum'])
    print(data['AvgResponseTime'])
    print(data['score'])
    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)
    
    response = requests.post(database_api_url, json=data)
    #response = requests.post(flask_server_url, json=data)

if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(11, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)
    
    user_email = input("Please enter your email: ")
    user_password = input("Please enter your password: ")
    response = requests.post(auth_url, json={"email":user_email,"password":user_password,"returnSecureToken":True})
    response_data = response.json()
    if "idToken" in response_data:
        print("Authenticated")
        print("Start playing")
        blinker(3,led)
    else:
        print("Authentication failed.")
        sys.exit(0)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t,response_data["idToken"])
