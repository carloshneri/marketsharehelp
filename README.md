Este programa é para auxiliar na analise de market share realizando consultas nos arquivos da base do sicore da Receita Federal.
Baixar os arquivos da familia de NCM no site do Siscore.
Os arquivos .xlsx devem ser colocados na pasta \marketsharehelp\base de dados\CSV

Filtros:
Há alguns arquivos que são utiizados como base de dados para a realização dos filtros:


Seleção das colunas
No arquivo \marketsharehelp\json\filtros\selecao.json possivel já selecionar os dados que
será utilizado na formação do datframe.

Filtro de NCM:
\marketsharehelp\json\filtros\ncm.xlsx
Na coluna A deve ter essa estrutura abaixo com um cabeçalho com o nome ncms e abaixo os codigos NCM que deseja filtrar.

ncms
84564000
84569000

Seleção por descrição
no arquivo \marketsharehelp\json\market share\market_share.xlsx é possivel criar os 
filtros detalhados pela descrição. Nessa planilha cada aba que for criada será um filtro 
especifico que, ao final, será uma aba separada da planilha contendo os dados finais.
Aqui é interessante ser colocado os codigos dos materiais, palavras chaves etc.Isso torna a pesquisa expansivel com a inclusão das
abas na planilha.

A planilha \marketsharehelp\json\black list\blach list.xlsx foi criada para que possamos realizar uma
limpeza nos dados após a seleção pela descrição. Quando analisar os resultados finais na planilha importação é possivel que 
venha com alguns informação indesejada. Isso pode ocorrer devido a, por exemplo, duas empresas ter o mesmo codigo de peça ou
que parte do texto procurado também esteja presente no texto da descrição.


