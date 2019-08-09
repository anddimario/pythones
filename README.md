Example python app with flask and elasticsearch

### Install
- get elasticsearch docker image from [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
- install and configure [pipenv](https://github.com/pypa/pipenv/)
- install dependencies: `pipenv install`
- run flask: `FLASK_APP=app.py FLASK_DEBUG=1 flask run`

### Install seeds data
- `python seeds/...`

### Sample curl
```

curl -i -H "Content-Type: application/json" -X POST -d '{"orderId":"3","sku":"3","productName":"prova","quantity":10,"price":10.2}' http://localhost:5000/movements
curl -i -H "Content-Type: application/json" http://localhost:5000/movements/1
curl -i -H "Content-Type: application/json" http://localhost:5000/movements/orders/16
curl -i -H "Content-Type: application/json" http://localhost:5000/movements
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/best/products
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/best/buyers
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/total/price
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/total/quantity
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/total/orders/16
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/total/products/6
curl -i -H "Content-Type: application/json" http://localhost:5000/stats/movements/total/buyers/rukawa
curl -i -H "Content-Type: application/json" "http://localhost:5000/stats/movements/total/buyers/rukawa?start_date=2019-08-08&end_date=2019-08-09"
curl -i -H "Content-Type: application/json" "http://localhost:5000/stats/movements/total/products/6?start_date=2019-08-08&end_date=2019-08-09"
```

### Todo
- stats by range for all routes
- tests