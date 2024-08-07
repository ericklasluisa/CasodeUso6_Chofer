Feature: Actualizar chofer

  Scenario: Actualizar un chofer
    Given Se inicia el navegador actualizar chofer
    When Entra a la seccion actualizar chofer
    And Aplasta el icono de editar chofer
    And Actualizar en chofer el campo Nombre Erick
    And Actualizar en chofer el campo Apellido Lasluisa
    And Actualizar en chofer el campo Numero 0992916611
    And Seleccionar en chofer el tipo de licencia C
    And Seleccionar en chofer el tipo de sangre A+
    Then Aplastar el boton para editar chofer
    And Visualizar alerta confirmacion actualizar chofer

  Scenario: Ingresar un nombre incorrecto
    Given Se inicia el navegador actualizar chofer
    When Entra a la seccion actualizar chofer
    And Aplasta el icono de editar chofer
    And Actualizar en chofer el campo Nombre 123
    Then Aplastar el boton para editar chofer
    And Visualizar alerta confirmacion actualizar chofer

  Scenario: Ingresar un apellido incorrecto
    Given Se inicia el navegador actualizar chofer
    When Entra a la seccion actualizar chofer
    And Aplasta el icono de editar chofer
    And Actualizar en chofer el campo Apellido 123
    Then Aplastar el boton para editar chofer
    And Visualizar alerta confirmacion actualizar chofer

  Scenario: Ingresar un numero incorrecto
    Given Se inicia el navegador actualizar chofer
    When Entra a la seccion actualizar chofer
    And Aplasta el icono de editar chofer
    And Actualizar en chofer el campo Numero cero
    Then Aplastar el boton para editar chofer
    And Visualizar alerta confirmacion actualizar chofer

  Scenario: Ingresar un numero invalido
    Given Se inicia el navegador actualizar chofer
    When Entra a la seccion actualizar chofer
    And Aplasta el icono de editar chofer
    And Actualizar en chofer el campo Numero 1234567890
    Then Aplastar el boton para editar chofer
    And Visualizar alerta confirmacion actualizar chofer
