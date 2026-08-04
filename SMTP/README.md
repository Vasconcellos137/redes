# Enviar gmail p poço d gmails

    nc -C localhost 1025
    EHLO cliente.exemplo.org
    MAIL FROM:<remetente@exemplo.org>
    RCPT TO:<destinatario@exemplo.com>
    DATA
    Subject: Assunto
    From: remetente@exemplo.org
    To: destinatario@exemplo.com
     
    HELL WORD .


# P/ coisa um ambiente virtual p install dotenv

    virtualenv aula
    source aula/bin/activate
    pip3 install dotenv

# P/ roda o bagulho
    python3 smtp_local.py