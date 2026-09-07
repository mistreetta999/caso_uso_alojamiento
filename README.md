# Caso de uso: Alojamiento

Proyecto académico para exámenes de la alumna Carolina Mistretta.

## Entrega de casos de uso (alojamientos)

### CU-01: Buscar alojamiento
- **Actor principal:** Usuario
- **Objetivo:** Encontrar alojamientos disponibles según destino, fechas y cantidad de huéspedes.
- **Precondiciones:** El usuario accede al sistema de búsqueda.
- **Flujo principal:**
  1. El usuario ingresa destino, fechas y huéspedes.
  2. El sistema valida los datos ingresados.
  3. El sistema muestra el listado de alojamientos disponibles.
- **Resultado esperado:** El usuario visualiza opciones de alojamiento filtradas.

### CU-02: Ver detalle de alojamiento
- **Actor principal:** Usuario
- **Objetivo:** Consultar información completa de un alojamiento específico.
- **Precondiciones:** Existe al menos un alojamiento publicado.
- **Flujo principal:**
  1. El usuario selecciona un alojamiento del listado.
  2. El sistema muestra fotos, descripción, servicios, precio y políticas.
- **Resultado esperado:** El usuario obtiene la información necesaria para decidir su reserva.

### CU-03: Reservar alojamiento
- **Actor principal:** Usuario
- **Actores secundarios:** Pasarela de pago, anfitrión
- **Objetivo:** Confirmar la reserva de un alojamiento.
- **Precondiciones:** El usuario seleccionó un alojamiento disponible para las fechas indicadas.
- **Flujo principal:**
  1. El usuario confirma datos de la reserva.
  2. El sistema calcula el total y solicita el pago.
  3. El usuario completa el pago.
  4. El sistema registra la reserva y envía confirmación.
- **Resultado esperado:** La reserva queda confirmada y registrada.
