## migrations
To migrate run:

```bash
python3 manage.py migrate
```
* migrations represent a data structure for the database.

## models.py
For custom data types we will follow the same "migration process". We will be creating a model that represents what a drink looks like. The mode will be a **python class**. As we build more models our database will get a big more complex.

To see our own tables within /admin we're going to want to create a models.py file within our app.

## serializers.py
This file will describe going from python object to json.

## views.py
This is where we create out end points.