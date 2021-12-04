import React from 'react';
import './App.css';
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Main from './main/Main';
import Products from "./admin/Products";
import { BrowserRouter } from 'react-router-dom';


function App() {
  return (
    <div className="App">
          <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            {/* <BrowserRouter>
              <Route path='/admin/products' exact component={Products}/>
              <Route path= '/' component={Main} />
            </BrowserRouter>  */}
            <Main />
            <Products />
            
          </main>
    </div>
  );
}

export default App;
