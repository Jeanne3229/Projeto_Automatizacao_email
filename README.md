# 💌 Automação De E-mails com Python

![Python](https://img.shields.io/badge/Python-8A2BE2?style=for-the-badge&logo=python&logoColor=white)
![Gmail](https://img.shields.io/badge/Gmail-8A2BE2?style=for-the-badge&logo=gmail&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-8A2BE2?style=for-the-badge)

| Status do Projeto: ✔️ (Concluído) |

## 📌 Tópicos
🔹 [Contexto](#-contexto)
🔹 [Funcionalidades](#-funcionalidades)
🔹 [Tecnologias Utilizadas](#-tecnologias-utilizadas)
🔹 [Como Executar](#-como-executar)

---

## 📖 Contexto
Este projeto foi criado para automatizar o envio de e-mails utilizando Python. O objetivo principal é otimizar tarefas repetitivas de comunicação, permitindo o disparo de mensagens através do servidor do Google (Gmail) de forma rápida, simples e segura. 

## ⚙️ Funcionalidades
- ✔️ Estabelecimento de conexão segura (TLS) com o servidor SMTP diretamente no python
- ✔️ Autenticação automática via Senha de Aplicativo
- ✔️ Estruturação completa do e-mail (Remetente, Destinatário, Assunto e Corpo)
- ✔️ Tratamento de erros (`try/except`) para avisar o usuário em caso de falhas (falta de @, email nao localizado etc)

## 💻 Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** `smtplib` e `email.message` (Nativas da linguagem, sem necessidade de instalações externas).

## 🚀 Como Executar

### ⤷ Pré-requisitos
- Python instalado na sua máquina.
- Uma conta do Gmail com a **Verificação em Duas Etapas** ativada.
- Uma **Senha de Aplicativo** gerada nas configurações do Google.

### ⤷ Passo a passo
1. Clone este repositório no seu computador.
2. Abra o arquivo `Inicio.py`.
3. Substitua as informações de texto falso pelas suas credenciais reais:
   - `email`: Coloque o seu e-mail remetente.
   - `receber`: Coloque o e-mail do destinatário.
   - `senha`: Coloque a sua senha de aplicativo de 16 dígitos.
4. Execute o arquivo no terminal com o comando:
   ```bash
   python Inicio.py

## Licença

MIT License

## 👩‍💻 Desenvolvedora

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Jeanne3229">
        <img src="https://github.com/Jeanne3229.png" width="120px;" alt="Jeanne"/><br>
        <sub><b>Jeanne Espíndola</b></sub>
      </a>
    </td>
  </tr>
</table>
