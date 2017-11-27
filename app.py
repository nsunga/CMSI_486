from py2neo import Graph, Node, Relationship
import csv
graph = Graph()

with open('persons.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        node = Node("Person",
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    age=row['age'],
                    sex=row['sex'],
                    ethnicity=row['ethnicity'])
        if(row['suspect'] == 'Y')
            crime = graph.find_one('Crime', 'crime_id', row['crime_id'])
            rel = Relationship(node, "COMMITTED_A", crime)
        graph.create(node)
