# Choroy

[https://www.avesdechile.cl/039.htm](https://www.avesdechile.cl/039.htm)

Es un acortador de direcciones de Chaucha.
Para facilitar el compartir y usar una dirección de chauchera.

## Uso

### Crear Nueva Dirección Corta

POST `https://choroy.chaucha.cl/links`

Parámetros:

 - uid (string, opcional) : identificador único. Si no se entrega es creado aleatoriamente.
 - address (string, requerido): dirección de chaucha para acortar.

Headers:
  Content-Type: application/json

Ejemplo de Uso:

```json
  {
    "uid" : "@clsource",
    "address" : "chUZgQYe3fxNGEjyRbQyehQ3Q7mkJrTWdU"
  }
```

### Obtener Dirección para un Identificador

GET `https://choroy.chaucha.cl/{uid}`

Ejemplo de Respuesta:

```json
  {
      "data": {
          "address": "chUZgQYe3fxNGEjyRbQyehQ3Q7mkJrTWdU",
          "created_at": 1512773521.5192478,
          "_links": {
              "uri": "/@clsource",
              "url": "http://localhost:8666/@clsource"
          },
          "uid": "@clsource"
      }
  }
```