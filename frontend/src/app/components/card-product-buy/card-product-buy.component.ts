import { Component, Input } from '@angular/core';
import { Storage } from '../../interfaces/storage.interface';

@Component({
  selector: 'app-card-product-buy',
  templateUrl: './card-product-buy.component.html',
  styleUrls: ['./card-product-buy.component.css']
})
export class CardProductBuyComponent {
  @Input() product: Storage = {} as Storage;
  quantity: number = 0;

  constructor() { }

  buyProduct() {
    console.log('Buying Product:', this.product.product.name);
    console.log('Quantity:', this.quantity);

    this.quantity = 1;
  }
}
