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
.\nombre_del_entorno\Scripts\activate
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

Una vez que el servidor esté en funcionamiento, puedes acceder a la API GraphQL en http://localhost:4000/graphql.

Aquí tienes algunos ejemplos de consultas:

# Obtener todas las infracciones
query {
  infracciones {
    id
    fecha
    tipo
    descripcion
  }
}

# Obtener una infracción por ID
query {
  infraccion(id: 1) {
    id
    fecha
    tipo
    descripcion
  }
}

# Crear una nueva infracción
mutation {
  createInfraccion(fecha: "2023-10-26", tipo: "Exceso de velocidad", descripcion: "Exceso de velocidad en la autopista") {
    id
    fecha
    tipo
    descripcion
  }
}

## Documentación

Para más información sobre la API GraphQL, consulta el siguiente recurso:
[GraphQL](https://graphql.org/)


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.