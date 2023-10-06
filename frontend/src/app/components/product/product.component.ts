import { Component } from '@angular/core';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css'],
})
export class ProductComponent {
  product: any = {};

  createProduct() {
    console.log('Product Data:', this.product);
    this.product = {};
  }
}
