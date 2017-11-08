# Detailed Database Design
## 2.1 Project Description
Our database holds case information for the LAPD's murder case files. The data we will be entering into the database pertains to overall case information, crime information, suspect information and victim information. The database acts as an easy and organized way to access relevant case information based on a search by the user. A search is done by either by clicking a desired keyword that is associated with information the user wishes to search, or by engaging in a more advanced search by specifying which fields the user wishes to search, and manually entering in specific attributes. The main users of this application will be a small team of LAPD detectives that require a better way to search for case information. We will be using Neo4j as the main database engine. Our database will be a web-based application so we will be using the Django framework as well. JavaScript, CSS, and HTML will be used to create the simple user interface to interact with the database. The database will implement the database standards of having the operations associated with CRUD and expectations of following the ACID framework.

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
  - suspect_id: Suspect entity identifier (Primary Key)
  - firstname: First name of suspect
  - lastname: Last name of suspect
  - ethnicity: Ethnicity of suspect
  - age: Age of suspect
  - sex: Sex or gender of suspect
  
+ Victim
  - victim_id: Victim entity identifier (Primary Key)
  - firstname: First name of victim
  - lastname: Last name of victim
  - ethnicity: Ethnicity of victim
  - age: Age of victim
  - sex: Sex or gender of suspect


 
## 2.3 Entity Relationship Diagram
![Detailed Database Design ERD](./Images/ERD_DDD.png)
