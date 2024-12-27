Organizador de Arquivos

	Este é um simples organizador de arquivos que move automaticamente arquivos de acordo com suas extensões para pastas específicas. O programa é ideal para manter seu diretório de downloads limpo e organizado, movendo arquivos para categorias como Imagens, Documentos e Planilhas.

Funcionalidades

	Organiza arquivos de acordo com a extensão:
 
	Imagens: .jpg, .png, .gif, .webp
	Documentos: .pdf, .docx, .txt
	Planilhas: .xlsx, .csv
 
O programa oferece ao usuário um menu simples com as opções:

	Organizar a pasta de downloads
	Encerrar o programa
 
Como Usar

	Clone ou baixe o código: Copie o arquivo organizador.py para sua máquina local.

	Abra o terminal ou prompt de comando.

	Execute o programa:
 		main.py
	 
Como Funciona

	O script utiliza o módulo os para interagir com o sistema de arquivos, verificando se os diretórios existem e criando novas pastas quando necessário.
	O módulo shutil é utilizado para mover os arquivos de um diretório para outro.
	O usuário escolhe uma opção através de um simples menu exibido no terminal.
 
	O programa verifica as extensões dos arquivos e os organiza nas pastas apropriadas:
	Imagens: .jpg, .png, .gif, .webp
	Documentos: .pdf, .docx, .txt
	Planilhas: .xlsx, .csv

Requisitos

	Python 3.x
	O programa foi testado em um ambiente Windows, mas pode ser adaptado para outros sistemas operacionais.

 Observações
 
	O caminho da pasta de downloads no código é fixado como C:\Users\Seu-nome-de-usuario\Downloads. Caso esteja utilizando outro sistema operacional ou tenha o diretório de downloads em outro local, será necessário modificar o caminho no código.
	O programa não verifica se há subpastas dentro do diretório de downloads. Apenas arquivos na raiz da pasta serão movidos.
