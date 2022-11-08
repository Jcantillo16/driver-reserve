# Driver-Reserve




Python 3.10

install python 3.10

install archivo requirements.txt

`pip install -r requirements.txt`

##  Descripcion

driver-reserve es un programa que te permite reservar un conductor disponible en la plataforma, para que recoja tu pedido y te lo lleve a tu destino.

##  Funcionamiento

el programa consta de 5 modulos:

   *customer
   *drivers
   *orders
   *payment
   *shedule
   
En el modulo de customer se encuentra la clase customer, que contiene los datos del cliente, como nombres, correo, telefono, direccion, etc.
aqui tambien se enuentran las funciones de registro, login, y logout.
se valida que el correo  no este registrado y que la contraseña se guarde encriptada.
para encriptar la contrasena se utiliza la libreria cryptography, que permite encriptar y desencriptar la contrasena, con la llave de Fernet.

**Dentro del modulo de customer en la carpeta test se encuentra el archivo test_customer.py, que contiene las pruebas unitarias de la clase customer.**


En el modulo de drivers se encuentra la clase driver, que contiene los datos del conductor, como nombres, estado (si esta disponble o no), etc.
tambien se encuentran las funcones de obtener la ubicacion de los conductores, y actualizarlas en la base de datos cada vez que se consuma el servicio.


En el Modulo de orders se encuentra la clase order, que contiene los datos del pedido, como el id del cliente, id del conductor, fecha, hora, etc.
aqui encontramos funciones, tales como crear un pedido y asignar el conductor disponible mas cercano al cliente.
para esto use una libreria llamada geopy, que permite calcular la distancia entre dos puntos, en este caso la distancia entre el cliente y el conductor.


En el modulo de payment se encuentra la clase payment, que contiene los datos del pago, como el id del cliente, id del pedido, metodo de pago, etc.
aqui tambien se encuentran las funciones de crear un pago y validar el pago.

En el modulo de shedule se encuentra la clase shedule, que contiene los datos del horario, como el id del conductor, hora de inicio, hora de fin, etc.
aqui tambien se encuentran las funciones de crear un horario y validar el horario.




