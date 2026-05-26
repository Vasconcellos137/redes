# # FROM image-base:tag
# FROM ubuntu:24.04 

FROM python:3.12


# /app -> diretório, pode ser qualquer nome

# trabalhe nesse diretório
WORKDIR /app 

# # copie o arquivo .sh p/ diretório /app
# COPY hi.sh /app

COPY conter.py /app

# # roda o comando
# RUN chmod +x hi.sh

RUN chmod +x conter.py

# # Comando
# ENTRYPOINT [ "./hi.sh" ]
# # Vira parâmetro
# CMD [ "10" ]

# roda comando tbm, caso RUN dê erro, é o padrão
# CMD ["./hi.sh"]

CMD ["python3", "./conter.py"]