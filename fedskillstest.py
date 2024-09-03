import requests
import matplotlib.pyplot as plt
from requests.auth import HTTPBasicAuth
from datetime import datetime

url = "https://fedskillstest.coalitiontechnologies.workers.dev"

username = "coalition"
password = "skills-test"
patient_name = "Emily Williams"

response = requests.get(url, auth=HTTPBasicAuth(username, password))

graph_data = {}

if response.status_code == 200:
    data = response.json()
    for patient in data:
      if patient["name"] == patient_name:
        for history in patient["diagnosis_history"]:
          #print(history)
          #print(history["month"], history["year"], history["blood_pressure"]["systolic"]["value"],  history["blood_pressure"]["diastolic"]["value"]  )
          if not (str(history["month"]) +" "+str(history["year"])) in graph_data:
            graph_data[str(history["month"]) +" "+str(history["year"])] = (history["blood_pressure"]["systolic"]["value"],  history["blood_pressure"]["diastolic"]["value"])
#print(graph_data)
sorted_data = sorted(graph_data.items(), key=lambda x: datetime.strptime(x[0], "%B %Y"))

dates = [item[0] for item in sorted_data]
values1 = [item[1][0] for item in sorted_data]
values2 = [item[1][1] for item in sorted_data]

plt.figure(figsize=(10, 5))
plt.plot(dates, values1, marker='o', linestyle='-', color='b', label='systolic')
plt.plot(dates, values2, marker='o', linestyle='-', color='r', label='diastolic')
plt.title(patient_name +"'s History")
plt.ylabel('Heart Rate')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
