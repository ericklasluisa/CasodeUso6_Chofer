Feature: Actualizar vehículo

  Scenario: Actualizar un chofer
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón editar
    And Actualizar el campo Nombre Erick
    And Actualizar el campo Apellido Lasluisa
    And Actualizar el campo Numero 0992916611
    And Seleccionar el tipo de licencia C
    And Seleccionar el tipo de sangre A+
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un nombre incorrecto
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón editar
    And Actualizar el campo Nombre 123
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un apellido incorrecto
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón editar
    And Actualizar el campo Apellido 123
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un numero incorrecto
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón editar
    And Actualizar el campo Numero cero
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion

  Scenario: Ingresar un numero invalido
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón editar
    And Actualizar el campo Numero 1234567890
    Then Aplastar el boton para editar
    And Visualizar alerta confirmacion
