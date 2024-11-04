# Instruções para execução do projeto

## Passos para baixar e abrir o projeto

### 1. Baixe o arquivo *.zip* ou faça um *git clone* do repositório.

### 2. Após clonar o repositório ou extrair o conteúdo do arquivo *.zip*, abra a pasta do projeto utilizando um editor de código de sua preferência.

### 3. Com a pasta aberta no editor, crie ou acesse um terminal existente e siga os passos da seção abaixo.

## Passos para instalar as dependências e rodar o projeto

### 1. Crie um ambiente virtual:
```bash
python3 -m venv venv
```
### 2. Ative o ambiente virtual:
#### Windows: 
```
.\venv\Scripts\activate
```
#### MacOS/Linux:
```
source venv/bin/activate
```
### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 4. Execute o projeto:
```bash
python processor.py
```

### **OBS:** Caso esteja enfrentando problemas de execução devido às bibliotecas importadas no código não estarem sendo reconhecidas, certifique-se de que o interpretador Python seja o do ambiente virtual.