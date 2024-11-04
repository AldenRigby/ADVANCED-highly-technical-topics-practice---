from app import App
from csv import reader

apps = []

with open("apps.csv") as csv_file:
    csv_reader = reader(csv_file, delimiter=",")
    next(csv_reader)
    for name, description, category, in csv_reader:
        apps.append(App(name,description,category))
print(csv_reader)
for app in apps:
    print(app)