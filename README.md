# Infracciones Backend con GraphQL

## Introducción

Este repositorio contiene el código del backend para una aplicación de Infracciones construida con GraphQL.

## Prerrequisitos

Python 3.x
pip (gestor de paquetes de Python)
Una base de datos PostgreSQL.

## Instalación

1. Crea un entorno virtual:
```bash
python -m venv nombre_del_entorno
```
2. Activa el entorno virtual:
```bash
cd nombre_del_entorno\Scripts
activate
cd ..
```

3. Clonar el repositorio:
```bash
git clone https://github.com/cristianchivisky/GraphQL-Infracciones.git
```

4. Instala las dependencias:
```bash
cd GraphQL-Infracciones
pip install -r requirements.txt
```

5. En el archivo __init__.py reemplaza la siguiente línea con las credenciales de tu base de datos:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://nombre_usuario:tu_contraseña@localhost/nombre_base_de_datos"


6. Iniciar el servidor:
```bash
python app.py
```

## Uso

Una vez que el servidor esté en funcionamiento, puedes acceder a la API GraphQL en http://localhost:5000/graphql.

Aquí tienes algunos ejemplos de consultas:

### Obtener todas las infracciones

```bash
query {
  infracciones {
    numeroInfraccion
    codigoInfraccion
    fecha
    hora
    observaciones
  	registro{
      numeroRegistro
      nombreyapellido
      fechaEmision
      fechaVencimiento
  	}vehiculo{
      patenteVehiculo
      domicilioPropietario
      nombreyapellidoPropietario
    }
  }
}
```

### Obtener una infracción por ID

```bash
query {
  infraccion(numeroInfraccion: 1) {
    codigoInfraccion
    hora
    fecha
    vehiculo{
      patenteVehiculo
    }registro{
      numeroRegistro
    }
  }
}
```
### Crear una nueva infracción

```bash
mutation {
  createInfraccion(codigoInfraccion: "EXC001", fecha: "2023-10-26", hora: "05:41", numeroRegistroId: 2, observaciones: "Exceso de velocidad en la autopista", patenteVehiculoId: "ABC123") {
    infraccion{
      numeroInfraccion
      fecha
      hora
      observaciones
    }
  }
}
```

## Documentación

Para más información sobre la API GraphQL, consulta el siguiente recurso:
[GraphQL](https://graphql.org/)


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.