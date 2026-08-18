# SSH
- surgiu como solução para empregar segurança
- secure shell

- ssh -p 2222 garibaldo@192.168.246.106 -> acessar máquina criada por prof, já q as máquinas do if possuem codigo de segurança impossiblitando conectar.


- Permite conectar um cliente como um servidor
- permite utilizar a conexão como tunel e enviar qualquer tipo de coisa pra outra máquina.

- scp -> "copia e cola"

scp -P 2222 garibaldo@192.168.246.106/config/prof/pudim.jpg

dockerFile -> instruções para contruir uma img

18.08.26

## Acesso à máquina virtual
ssh nome.sobrenome@192.168.246.131

## P/ copiar arquivo p meu diretório
- Deve ser feito na máquina local
- scp origem <server> destino <local>

### comando:
scp nome.sobrenome@192.168.246.131:caminho_arquivo