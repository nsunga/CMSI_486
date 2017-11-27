from py2neo import Graph, Node, Relationship
import csv
graph = Graph()

with open('cases.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        case = Node("Case",
                    case_id=row['case_id'],
                    date=row['date'],
                    crime_location=row['crime_location'])
        graph.create(case)

with open('crime.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        crime = Node("Crime",
                    crime_id=row['crime_id'],
                    crime_type=row['crime_type'])
        graph.create(crime)
        case = graph.find_one('Case','case_id',row['case_id'])
        rel = Relationship(crime, "HAS", case)
        graph.create(rel)

with open('persons.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        person = Node("Person",
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    age=row['age'],
                    sex=row['sex'],
                    ethnicity=row['ethnicity'])
        graph.create(person)

        if row['suspect'] == 'Y':
            crime = graph.find_one('Crime', 'crime_id', row['crime_id'])
            rel = Relationship(person, "COMMITTED_A", crime)
            graph.create(rel)

        case = graph.find_one('Case','case_id', row['case_id'])
        rel = Relationship(person, "INVOLVED_IN", case)
        graph.create(rel)
