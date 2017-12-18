export const FORM: any = {
    'title': 'My Test Form',
    components: [
      {
        type: 'textfield',
        key: 'nombres',
        label: 'Nombres',
        placeholder: 'Ingresa tus nombres',
        input: true
      },
      {
        type: 'textfield',
        key: 'apellidos',
        label: 'Apellidos',
        placeholder: 'Ingresa tus apellidos',
        input: true
      },
      {
        type: 'textfield',
        key: 'ciudad',
        label: 'Ciudad',
        input: true
      },
      {
        type: 'button',
        action: 'submit',
        label: 'Enviar',
        theme: 'primary'
      }
    ]
  };