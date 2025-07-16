# Urna Eletrônica Python

Este projeto é uma simulação de **Urna Eletrônica** com interface gráfica em Python (Tkinter), permitindo votação, registro de votos, exibição de fotos dos candidatos, relatório final e funcionalidades de encerramento e limpeza de votos.

## Funcionalidades

- **Votação por número**: Digite o número do candidato, veja foto, nome e partido.
- **Voto em branco, nulo e correção**: Botões dedicados para cada ação.
- **Confirmação sonora**: Ao confirmar ou votar em branco, um som é reproduzido (`confirma.wav`).
- **Relatório final**: Exibe total de votos por candidato, brancos e nulos ao encerrar a urna.
- **Encerramento da urna**: Bloqueia a votação e exibe "FIM".
- **Limpar votos**: Botão para resetar todos os votos.
- **Fotos dos candidatos**: Exibidas ao lado das informações, a partir da pasta `imagens/`.

## Estrutura de Pastas

```
Urna-Eletronica/
├── urna.py
├── candidatos.json
├── votos.json
├── confirma.wav
└── imagens/
    ├── 13.jpg
    ├── 22.jpg
    └── ...
```

## Como usar

1. **Instale as dependências:**
   ```sh
   pip install pillow
   ```

2. **Coloque as fotos dos candidatos** na pasta `imagens/` e configure o arquivo `candidatos.json` com o nome do arquivo da foto.

3. **Adicione o arquivo de som** `confirma.wav` na mesma pasta do `urna.py`.

4. **Execute o programa:**
   ```sh
   python3 urna.py
   ```

5. **Votação:**
   - Digite o número do candidato (2 dígitos).
   - Confira as informações e foto.
   - Use os botões para votar em branco, corrigir ou confirmar.

6. **Relatório e encerramento:**
   - Clique em "Encerrar Urna" para bloquear a urna e ver o relatório final.
   - Clique em "Limpar Votos" para resetar a votação.

## Exemplo de candidatos.json

```json
{
  "13": {"nome": "João", "partido": "ABC", "imagem": "13.jpg"},
  "22": {"nome": "Maria", "partido": "XYZ", "imagem": "22.jpg"}
}
```

## Observações

- O arquivo `votos.json` armazena todos os votos.
- O som de confirmação requer o utilitário `aplay` no Linux (`sudo apt install alsa-utils`).
- O botão "Branco" registra corretamente o voto em branco.

## Licença

Projeto didático, sem fins lucrativos.
