### Assignment 1
Tasks Completed:
* Created an API which takes pincode as a query parameter and returns the city and state as a result.
* Created a Address Form which takes the input as Zipcode and automatically fills the City and State feilds coressponding to the code entered.
* FInally Stored the Data submitted by the user in the database.

### Prerequisites

Clone repository
```bash
git clone https://github.com/Ayush5120/Assignment1.git
```

Traverse to app directory
```bash
cd Form
```

Deploy MongoDB container
Ensure you have the following software installed:
* [Docker](https://docs.docker.com/engine/install/ubuntu/) (version 20.10.12) or higher

Start MongoDB Container
```bash
docker pull mongo
```
```bash
docker create -it --name MongoTest -p 27017:27017 mongo
```
```bash
docker start MongoTest
```

### Run Project Using

Create Virtual environment (optional)
```bash
virtualenv env
```
```bash
source env/bin/activate
```

Make sure to be in Forms folder
```bash
pip install -r requirements.txt
```

```bash
python3 app.py
```

Visit the Address Form at 

```bash
http://localhost:5001/forms
```

To use the Pincode API:

Get the state,city corresponding to the zip code by passing query parameter as shown:
```bash
http://localhost:5001/pincodes?pin=121004
```
