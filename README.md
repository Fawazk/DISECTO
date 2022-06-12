# DISECTO

# Admin user credentials <br>
username: admin <br>
password: admin <br>

# Users credentials <br>
username: sanin <br>
password: qaz123#QAZ <br>

username: user1 <br>
password: qaz123#QAZ <br>

# APIs Available (Heroku server):

=> GET method for product list https://disectoo.herokuapp.com/store/ <br>
=> POST method for admin to create new product https://disectoo.herokuapp.com/store/create-item <br>
=> PUT, DELETE and GET methods for admin to update database https://disectoo.herokuapp.com/store/item/<:slug> <br>
=> GET method for showing cart-items for current user https://disectoo.herokuapp.com/cart/ <br>
=> GET, DELETE and PUT methods for updating cart https://disectoo.herokuapp.com/cart/update/<:id> <br>
=> GET method for displaying a pdf invoice of the current cart-items https://disectoo.herokuapp.com/cart/invoice <br>

# Cron Job At every 12Am for updating expired produts:

=> GET method for expired product list https://disectoo.herokuapp.com/store/expired-items <br>

