
import { useEffect } from 'react';
import './App.css';

function App() {

  useEffect(() => {
    fetch('https://pizzariagui.herokuapp.com/api/pratos/')
      .then(resposta => resposta.json())
      .then(dados => {
        console.log(dados)
      })
  }, [])


  return (
    <div className="App">
      <div className='banner-container'>
        <img src="imagens/banner.png" alt="um banner Pizzaria gui" />
      </div>
      <div className='logo-container'>
        <img src="imagens/logo.png" alt="Logo da Pizzaria gui" />
      </div>
    </div>
  );
}

export default App;
