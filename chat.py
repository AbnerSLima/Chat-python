import flet as ft  #importar a flet

def main(pagina): # criar a main
    texto = ft.Text("WCD Chat")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.co ntrols.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text("Bem-vindo ao Chat da WCD")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(open=False, modal=True, title=titulo_popup, content=nome_usuario, actions=[botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main, view=ft.WEB_BROWSER) # Criar o app chamando a main