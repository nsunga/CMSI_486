# Detailed Database Design
## 2.1 Project Description

## 2.2 Data Description
+ Case
  - case_id: Case entity identifier (Primary Key)
  - crime_id: Crime entity identifier 
  - victim_id: Victim entity identifier
  - suspect_id: Suspect entity identifier
  - crime_location: Location the crime took place
  - date: Date that crime occurred
  
+ Crime
  - crime_id: Crime entity identifier (Primary Key)
  - crime_type: Charge of the crime (Homicide, Robbery, Assault etc.)
  
+ Suspect
  - suspect_id: Suspect entity identifier
  - firstname: First name of suspect
  - lastname: Last name of suspect
  - ethnicity: Ethnicity of suspect
  - age: Age of suspect
  - sex: Sex or gender of suspect
  
+ Victim
  - victim_id: Victim entity identifier
  - firstname: First name of victim
  - lastname: Last name of victim
  - ethnicity: Ethnicity of victim
  - age: Age of victim
  - sex: Sex or gender of suspect


 
## 2.3 Entity Relationship Diagram
![Detailed Database Design ERD](./Images/ERD_DDD.png)
