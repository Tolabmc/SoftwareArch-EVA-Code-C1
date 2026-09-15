import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")
    country = eva.get("country")

    if not date_text or not duration_text:
        continue

    date = datetime.fromisoformat(date_text)
    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    records.append((date, duration_hours, country))

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

country_hours = Counter()
for date, duration_hours, country in records:

    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)
    country_hours[country] += duration_hours #Add the duration to the count for the country in the Counter Data Type



fig, ax = plt.subplots()
ax.bar(country_hours.keys(), country_hours.values())
ax.set_title("EVA duration by country")
ax.set_xlabel("Country")
ax.set_ylabel("EVA duration (hours)")
plt.tight_layout()
plt.savefig("country_duration.png")
plt.show()

plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
