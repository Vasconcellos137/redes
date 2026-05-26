# FROM image-base:tag
FROM ubuntu:24.04 

# /app -> diretório, pode ser qualquer nome

# trabalhe nesse diretório
WORKDIR /app 

# copie o arquivo .sh p/ diretório /app
COPY hi.sh /app

# roda o comando
RUN chmod +x hi.sh

# roda comando tbm, caso RUN dê erro
CMD ["./hi.sh"]