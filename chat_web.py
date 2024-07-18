# Titulo: Chat
# Botão: iniciar chat 
    # Popup
        # Titulo: Bem vindo ao Chat
        # Campo de texto: Escreva seu nome
        # Botão: Entrar no chat
            # Fechar o popup
            # Criar o chat (com a mensagem 'nome do usuario entrou no chat')
                # Campo de texto: Digite sua mensagem

import flet as ft

# Função principal
def main(pagina):

    titulo = ft.Text('Chat')

    # Tunel
    def enviar_mensagem_tunel(mensagem):
        # Enviar mensagem
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # Criar o tunel de comunicação

    titulo_popup = ft.Text('Bem vindo ao chat')
    campo_nome = ft.TextField(label = 'Escreva seu nome')

    # Função para enviar mensagem
    def enviar_mensagem(evento):
        texto = f'{campo_nome.value}: {mensagem.value}'
       
        # Enviar uma mensagem no túnel
        pagina.pubsub.send_all(texto)

        # Limpar campo de mensagem
        mensagem.value = ''
        pagina.update()

    mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar',on_click=enviar_mensagem)
    chat = ft.Column()
    linha_mensagem = ft.Row([mensagem, botao_enviar])
    
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        # Remover popup
        popup.open = False
        # Criar Chat
        pagina.add(chat)
        # Adicionar linha de mensagem
        pagina.add(linha_mensagem)

        # Adicionar a mesagem que o usuario entrou
        texto_entrou_chat = f'{campo_nome.value} entrou no chat'
        pagina.pubsub.send_all(texto_entrou_chat)
        
        pagina.update()

    botao_entrar = ft.ElevatedButton('Entrar', on_click=entrar_chat)
    
    popup = ft.AlertDialog(title=titulo_popup, content=campo_nome, actions=[botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar chat',on_click = abrir_popup)

    # Mostrar
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Executar
ft.app(main, view=ft.WEB_BROWSER)