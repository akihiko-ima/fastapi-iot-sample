import requests
import time
import random

API_ENDPOINT = "http://127.0.0.1:8000/sensor/add_data"

machineID = 1
# (None にすると無限ループ）
repetition_number = 10000
interval_sec = 1

# 送信ループ
for i in range(repetition_number):
    # 15℃を基準にランダムな温度変動
    temperature = round(15 + random.uniform(-5, 5), 2)
    params = {"machineID": machineID, "temperature": temperature}

    try:
        response = requests.get(API_ENDPOINT, params=params)
        print(
            f"[{i+1}/{repetition_number}] Sent: {params}, Response: {response.status_code}, {response.json()}"
        )
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(interval_sec)

print("Finished sending data.")
