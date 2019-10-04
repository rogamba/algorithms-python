# System Design Cloud Kit

- Order Producer (Poisson distribution) 
  - Interfaz in memory
- Order Consumer (Kitchen) -> categorize in shelves
  - Consuming type: order
  - Assign id
- Shelve (interface)
  - get next good
  - get next waste

- Waste collector
  - Constructor: lista de shelves e intervalo de tiempo de monitoreo
  - Consume y reencola mensajes, quita los de waste

(alguien llegó...)

- DriverDispatcher (interface)
  - schedule_pickup(order_id) -> assign order_id to driver 
  - assign time for pickup
  - consumer que asigna el timestamp
 
Queue de driver dispatcher con (order_id, now + random )
Proceso monitoreando queue de drivers, si el tiempo de ahora es igual el de la order, proceder

python cli dashboard


Mocks de las clases para testing


- Docker
 .pex