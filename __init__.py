from app import graph

def create_uniqueness_constraint(label, property):
    query = "CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE"
    query = query.format(label=label, property=property)
    graph.run(query)

create_uniqueness_constraint("Case", "case_id")
create_uniqueness_constraint("Crime", "crime_id")
