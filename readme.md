<h1>My Gaming List</h1>

<h3>Sobre o Projeto</h3>
<p>MyGamingList é uma aplicação desenvolvida para gerenciar sua lista de jogos favoritos, 
organizando informações como nome, ano de lançamento, plataforma e nota pessoal. 
O objetivo é fornecer uma interface simples e funcional para manter seu catálogo de jogos atualizado.</p>

<h2>Como Configurar e Acessar o Projeto</h2>
<h3>Requisitos</h3>

<ul>
  <li>Docker instalado na máquina.</li>
  <li>Navegador web para acessar a aplicação (ex.: Google Chrome, Firefox, etc.).</li>
</ul>

<h2>Passos para rodar a Build</h2>

<ol>
  <li><b>Clone o Repositório</b> e certifique-se de clonar para a máquina local:
    
    git clone https://github.com/devMarlos/MyGamingList.git
    cd MyGamingList
  </li>

  <li><b>Inicie o contêiner</b> e mapeia a porta local para acessar a aplicação:
    
    docker run -p 8501:8501 mygaminglist
  </li>

  <li><b>Acesse no Navegador</b>  e abra aplicação usando a URL abaixo:
    
    http://localhost:8501
  </li>
</ol>

<h2>Persistência de Dados (Opcional)</h2>
<p>Para garantir que o banco de dados SQLite seja persistente no sistema host, use volumes ao rodar o contêiner
e garantir que os dados sejam salvos localmente e não sejam perdidos ao reiniciar o contêiner.

`docker run -v $(pwd)/app/database:/app/database -p 8501:8501 mygaminglist`
</p>

<h2>Tecnologias Utilizadas</h2>
<ul>

  <li>Python 3.9</li>
  <li>Streamlit</li>
  <li>SQLAlchemy</li>
  <li>SQLite</li>
  <li>Docker</li>
  
</ul>






