import queue

global TIME_UNIT
TIME_UNIT = 1

global ORDER_Q
ORDER_Q = queue.Queue()
ORDER_Q.join()

global ORDERS
ORDERS = []


global ORDER_SERVED
ORDER_SERVED = 'ORDER_SERVED'
global SERVED_ORDERS
SERVED_ORDERS = []


global ORDER_STARS
ORDER_STARS = []

global WAITERS
WAITERS = [{
    'id': 1,
    'name': 'Robert De Niro'
}, {
    'id': 2,
    'name': 'Jack Nicholson'
}, {
    'id': 3,
    'name': 'Tom Hanks'
}, {
    'id': 4,
    'name': 'Leonardo DiCaprio'
}]


global TABLE_WAITING_FOR_ORDER_TO_BE_SERVED
global TABLE_WAITING_FOR_WAITER
global TABLE_ORDER_SERVED
global TABLE_FREE
TABLE_WAITING_FOR_ORDER_TO_BE_SERVED = 'TABLE_WAITING_FOR_ORDER_TO_BE_SERVED'
TABLE_WAITING_FOR_WAITER = 'TABLE_WAITING_FOR_WAITER'
TABLE_FREE = 'TABLE_FREE'
TABLE_ORDER_SERVED = 'TABLE_ORDER_SERVED'


global TABLES
TABLES = [{
    "id": 1,
    "state": TABLE_FREE,
    "order_id": None
}, {
    "id": 2,
    "state": TABLE_FREE,
    "order_id": None
}, {
    "id": 3,
    "state": TABLE_FREE,
    "order_id": None
}, {
    "id": 4,
    "state": TABLE_FREE,
    "order_id": None
}, {
    "id": 5,
    "state": TABLE_FREE,
    "order_id": None
}]

global FOODS
FOODS = [{
    "id": 1,
    "name": "pizza",
    "preparation-time": 20,
    "complexity": 2,
    "cooking-apparatus": "oven"
}, {
    "id": 2,
    "name": "salad",
    "preparation-time": 10,
    "complexity": 1,
    "cooking-apparatus": None
}, {
	"id": 3,
	"name": "zeama",
	"preparation-time": 7 ,
	"complexity": 1 ,
	"cooking-apparatus": "stove"
}, {
    "id": 4,
    "name": "Scallop Sashimi with Meyer Lemon Confit",
    "preparation-time": 32,
    "complexity": 3,
    "cooking-apparatus": None
}, {
    "id": 5,
    "name": "Island Duck with Mulberry Mustard",
    "preparation-time": 35,
    "complexity": 3,
    "cooking-apparatus": "oven"
}, {
    "id": 6,
    "name": "Waffles",
    "preparation-time": 10,
    "complexity": 1,
    "cooking-apparatus": "stove"
}, {
    "id": 7,
    "name": "Aubergine",
    "preparation-time": 20,
    "complexity": 2,
    "cooking-apparatus": None
}, {
    "id": 8,
    "name": "Lasagna",
    "preparation-time": 30,
    "complexity": 2,
    "cooking-apparatus": "oven"
}, {
    "id": 9,
    "name": "Burger",
    "preparation-time": 15,
    "complexity": 1,
    "cooking-apparatus": "oven"
}, {
    "id": 10,
    "name": "Gyros",
    "preparation-time": 15,
    "complexity": 1,
    "cooking-apparatus": None
}]
