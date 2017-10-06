# Database
## Amazon RDS: Simplif.ai's database solution

Simplif.ai uses Amazon RDS to store data about users, such as:
* email address
* notes
* summaries
* social network accounts

Our database communicates with the backend to store data when necessary, as well as retrieve information for the backend when it is requested. The class structures for our data in RDS can be found in the design document.

Note: In order to keep Amazon RDS inside the free tier, we will use less than 20GB of storage.

More information regarding the setup and use of the RDS can be found [here](https://aws.amazon.com/getting-started/tutorials/create-mysql-db/).


The database has been populated with the data as outlined in our class diagram, and can be accessed at the following location with the credentials provided to team members: simplifai.caijj6vztwxw.us-east-2.rds.amazonaws.com


MYSQL queries are required in order to interface with the database and more information about them can be found [here](https://www.w3schools.com/nodejs/nodejs_mysql_insert.asp).
