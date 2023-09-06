# Sgoluc Email Leak Checker
Olá1 Criei esse projeto para fins educacionais, mas decidi monitorar alguns e-mails de amigos e familiares de forma automatizada. Este script utiliza a API do [LeakCheck](https://leakcheck.net) para pesquisar - _dada uma lista de e-mails_ - por vazamentos envolvendo tais endereços.

## Pré-requisitos
- Uma conta no LeakCheck com uma chave de API

## Utilização
Você pode rodar o script manualmente, mas eu particularmente criei uma tarefa agendada no Windows para rodar semanalmente:
```
python selc.py
```
