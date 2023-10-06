import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  products = [
    {
      name: 'Product 1',
      price: 19.99,
      category: 'Electronics',
      amount: 10,
    },
    {
      name: 'Product 2',
      price: 29.99,
      category: 'Clothing',
      amount: 20,
    },
  ];
} 
