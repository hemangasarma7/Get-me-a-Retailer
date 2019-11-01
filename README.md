# Get-me-a-Retailer
getMeARetailer is a python django project using django rest framework which helps a customer to select the best online provider for a product based on price, provider rating and delivery time
It consists of three django models: Provider, Product and Logistic. With the help of django rest_framework, several REST APIs have been designed to add and list entries o each mentioned model.

Also, two more REST APIs have been designed to list the price variations of a particular product with respect to different online providers, and to list the different delivery time with respect to different logistic service providers working with the chosen online provider for the chosen product.


Sample APIs to use the application:

♦ Adding a Product:

Method: POST

Url: http://127.0.0.1:8000/getMeARetailerApp/product/

Body: JSON

{
	"title" : "iPhone XS",
	"brand" : "Apple",
	"specs" : "Mobile Phone",
	"price" : 99.00,
	"site" : 1
}


♦ Listing all products:

Method: GET

Url: http://127.0.0.1:8000/getMeARetailerApp/product/


♦ Adding a Provider:

Method: POST

Url: http://127.0.0.1:8000/getMeARetailerApp/provider/

Body: JSON

{
	"title" : "Flipkart",
	"parent" : "Walmart",
	"founded" : 2007,
	"focus_category" : "Books",
	"rating" : 4
}


♦ Listing all providers:

Method: GET

Url: http://127.0.0.1:8000/getMeARetailerApp/provider/


♦ Adding a Logistic:

Method: POST

Url: http://127.0.0.1:8000/getMeARetailerApp/logistic/

Body: JSON

{
	"title" : "Delhivery",
	"parent" : "Delhivery",
	"founded" : 2011,
	"focus_category" : "Apparels",
	"rating" : 4,
	"item" : 1,
	"delivery_time" : 5
}


♦ Listing all logistics:

Method: GET

Url: http://127.0.0.1:8000/getMeARetailerApp/logistic/


♦ Price Comparison of a product:

Method: POST

Url: http://127.0.0.1:8000/getMeARetailerApp/productPricing/

Body: JSON

{
	"title" : "iPhone XS"
}


♦ Delivery date comparison of a product for a chosen site:

Method: POST

Url: http://127.0.0.1:8000/getMeARetailerApp/deliveryTime/

Body: JSON

{
	"item" : 1
}

