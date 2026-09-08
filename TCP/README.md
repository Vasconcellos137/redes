Protocolo d transporte

https://materiais.darlon.com.br/RC/tcp 

tshark -i lo -f "port 10100" -> 

nc -l 10100 -> Server

echo 'Aula d redes d computadores' > msg.txt 

nc -N localhost 10100 < msg.txt

dd if=/dev/zero count=1 bs=10M of=data.bin
