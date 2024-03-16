# Product_BulkInsert-API

# Project set-up
create a virtual environment
install django and djangorestframework

start a django project
django-admin startproject product_insert_api

start an app
python manage.py startapp product_insert_app

# Project run
python manage.py runserver


# Project API

#

#DATA FORMAT FOR BULK DATA INSERTION
{
    "products": [
        {
            "name": "Yoghurt",
            "image": "yogurt.jpg",
            "variants": [
                {
                    "sku": "YOGURT-VANILLA",
                    "name": "Vanilla",
                    "price": 2.99,
                    "details": "Vanilla flavored yogurt"
                },
                {
                    "sku": "YOGURT-STRAWBERRY",
                    "name": "Strawberry",
                    "price": 2.99,
                    "details": "Strawberry flavored yogurt"
                }
            ]
        }
    ]
}
