# Preliminary Database Design
## 1.1 Project Description
For our database design, we will be using Neo4j: a native graph database that is built to store, query and manage highly connected data. This will be the first time our team will be using Neo4j. If difficulty follows, we may consider switching to a more familiar DBMS. The users for this database is geared towards LAPD Detectives. It is meant to keep track of their case files. The database will implement the database standards of having the operations associated with CRUD and expectations of following the ACID framework. The database is a part of a web application built off of the Django framework.

## 1.2 Data Description
The data that will be stored is information related to case files. These case files are supplied by the LAPD and pertain to their murder case books. Specifically, the types of data will be strings. These strings encompass information such as: victim names, suspect names, weapons, dates, and other relevant LAPD murder case information.

## 1.3 Examples
##### 1. A default table that displays all case entries

##### 2. A detailed case information page that displays all attributes for a specific entry

##### 3. A filtered table that displays cases entries that match the user's search input

##### 4. All cases entries are editable and database will only accept valid inputs

##### 5. Case entries include case information such MasterDr#, Dr#, Victim Names, Location etc.

## 1.4 Preliminary Schema
#### Case

|Court Case # | Coroner Case #| Dr# (PK)| Notes          | Detail Key (FK)| Police Key (FK)|VictimID
|-------------|---------------|---------|----------------|----------------|----------------|-------|
| 31231231    | 24795739      | 2412    |  Example Note  | 0000000001     | 0000000001     |0000024123

#### Victim

|VictimID(PK)|Name | Sex | Age | Victim Description | SuspectID(FK)|
|------------|-----|-----|-----|--------------------|--------------|
|0000024123  |Rony | M   | 22  | Glasses and flannel| 39571245     |

#### Suspect

|SuspectID(PK)|Name        |          Motive    |
|-------------|------------|------------------- |
|39571245     |Nick        | Robbery            |

#### Police

| Police Key (PK)| Division   | Bureau |
|----------------|------------|--------|
|0000001         | "Southwest" | "OSB" |

#### Detail

|Detail Key (PK)|Crime Address | Date Occurred| Date Reported | Weapon     |
|---------------|------------- |--------------|---------------|------------|
|0000001        |123 Foobar Ave|12/25/16      |12/25/16       | Lorem Ipsum|

#### Book

|Master Dr # (PK)| # of Volumes | # of Associated Cases | Dr # (FK)|
|----------------|--------------|-----------------------|----------|
|92746172        | 1            | 1                     | 2412     |
|94637224/2      | 1            | 2                     | 2471     |

## 1.5 Preliminary ERD for Database
![Preliminary ERD](/Images/ERD.png)
