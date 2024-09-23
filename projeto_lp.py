senha_cadastrada =''

while True:    
    senha = input('cadastre uma senha: ').strip()   
    confirm_senha = input('confirme a senha: ').strip()
    if senha == confirm_senha:
        print('senha cadastrada com sucesso!\n iniciando sistemas...\n "musica alegre"')
        senha_cadastrada = senha
        break
    else:
        print('senha incorreta tente novamente')    

for  i in range(3, -1, -1):
 senha_usuario = input('informe  a senha cadastrada: ').strip()
 if senha_cadastrada != senha_usuario:
    print(f'senha incorreta, voce tem {i} tentativas ate o bloqueio'if i > 0 else 'Aparelho Bloqueado')
    
 else:
    print('Bem Vindo!!! \n"mais musica alegre!!!"') 
    break
    