print('='*12,' Validação de Dados ','='*12)

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('\nSexo {} registrado com sucesso!'.format(sexo))
print('='*46)