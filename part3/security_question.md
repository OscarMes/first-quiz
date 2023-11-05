## En base a OWASP Top 10 realizaría ciertas verificaciones o cambios como lo son:

# Fallas en el registro y monitoreo
Realizar un monitoreo a actividades criticas como lo son las ventas y quien puede acceder a ellas, se tiene claro que 13 empleados son los únicos que pueden acceder a dicho modulo pero ¿qué pasa si aparece un “empleado” no registrado número 14 o 15?, se debe hacer seguimiento de por qué logró acceder y a que tiene acceso en sí, el monitoreo es importante para evitar accesos no autorizados y a la par del monitoreo establecer limites de intentos de acceso, en caso de que se rompan este limite se registra como anomalía.

# Fallas en el software y en la integridad de los datos 
Es importante utilizar librerías o herramientas medianamente conocidas y en caso de que lo sean, asegurarnos que no tengan un historial de haber tenido ataques de contribuidores maliciosos, es importante cuidar los datos que se almacenan del startup y que no sean robados por personas mal intencionadas.

# Fallas de identificación y autenticación
Principalmente a los 12 ingenieros de software que deben estar haciendo cambios constantes a todos los módulos hay que instruirles que no creen un super usuario genérico al cual puedan ingresar a estos módulos, este tipo de super usuarios son muy cotizados por ciber delincuentes que pueden aprovechar este fallo, también tener limitante de inicio de sesión para evitar los ingresos por fuerza bruta, a la par solicitar la creación de contraseñas con caracteres especiales y que no formen un palabra en concreto, en la parte de almacenamiento de la contraseña en la base de datos es importante registrar dicha cadena de caracteres como password para una mayor seguridad.

# Componentes vulnerables y desactualizados
Al instalar paneles solares no es bueno confiarse de que no se puede ser atacado, por lo que es importante tener componentes como el gestor de base de datos MySQL en sus ultimas versiones para así estar cubiertos con los parches de seguridad, suponiendo que se implementa flutter para el desarrollo de la versión móvil es importante tener su última versión para evitar fallos de seguridad, es importante tener estos y todos los componentes que implica el desarrollo en su mejor versión.

# Configuración de seguridad incorrecta 
Dar accesos necesarios dependiendo el área para evitar problemas de seguridad, si hay 3 empleados en atención al cliente los cuales tienen la vista de información de cliente y la modificación de cuentas y pedidos, es fundamental que solo puedan tener esos accesos y no más de los necesarios, lo mismo sucede con el empleado de ventas.
Los accesos específicos benefician a la integridad del sistema ya que se conoce quienes pueden acceder a la totalidad y quienes, a ciertos puntos, por otra parte, muchas veces es necesario tener control remoto de los equipos por lo que es primordial tener las credenciales con cierto tipo de complejidad para no recibir ninguna intromisión.

# Diseño inseguro 
Debe haber una separación correcta de qué actividades se realizan en el front end y que actividades se realizan en el back end, cuando se establecen estas separaciones de manera correcta podemos evitar que alguien pueda hacer, por ejemplo, muchas solicitudes de paneles solares y al romper el limite de solicitudes por una mala comunicación entre el front y el back podría ocurrir que no se refleje un precio total correcto en la compra, lo que podría llevar a un conflicto en el área contable.

# Pérdida de control de acceso 
Cómo se implementa una interfaz web para que el cliente pueda acceder, hay que asegurarse de que este cliente junto con sus credenciales sea el único que pueda acceder a su cuenta y que sus datos se mantengan íntegros y fuera de la vista de los demás usuarios, para esto se puede implementar capaz y filtros que validen que solo el usuario con sus credenciales puede tener acceso a dicha información y así mismo poder modificarla.



