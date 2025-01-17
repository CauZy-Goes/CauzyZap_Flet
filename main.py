# pip install flet

import flet as ft

# Criar uma funcao principal para rodas o aplicativo
def main(pagina):
    # titulo
    titulo = ft.Text("CauzyZap")

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])  # linha visual

    chat = ft.Column()

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)

        pagina.add(linha_enviar)
        pagina.add(chat)

        mensagem = f"{caixa_nome.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # Criar popup
    titulo_popup = ft.Text("Bem vindo ao CauzyZap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_poppup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_poppup])

    # colocar alementos
    pagina.add(titulo)
    pagina.add(botao)

ft.app(main, view=ft.WEB_BROWSER)