## Toda img q/ criar e jogar no DockerHub precisa seguiur esse padrão:

 user - tag - name - version 

* Ex. 777v/fusca:1.0

~•~ UserName in DockerHub -> 777v ~•~

# O conteúdo dessa pasta seraá copiado ou sobreposto na outra quando rodar:
docker run --name web -p 8080:80 -v /home/aluno/wilson:/usr/local/apache2/htdocs httpd

