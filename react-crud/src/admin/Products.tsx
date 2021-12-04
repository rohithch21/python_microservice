// stateless react component
import React, { useEffect } from 'react'
import Wrapper from './Wrapper';

const Products = () => {
    useEffect( effect: () => {
        const getProducts = async () => {
            const response = await fetch(input: "http://localhost:8000/api/products");
            const data = await response.json();
            console.log(data);
        };
        getProducts();
    }, deps: []);
    return (
        <Wrapper>
        <div className="table-responsive">
        <table className="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1,001</td>
              <td>random</td>
              <td>data</td>
              <td>placeholder</td>
              <td>text</td>
            </tr>
          </tbody>
        </table>
      </div>
      </Wrapper>
    )
};

export default Products;