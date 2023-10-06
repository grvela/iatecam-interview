import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-card-product-buy',
  templateUrl: './card-product-buy.component.html',
  styleUrls: ['./card-product-buy.component.css']
})
export class CardProductBuyComponent {
  @Input() product: any;
  quantity: number = 1;

  buyProduct() {
    console.log('Buying Product:', this.product.name);
    console.log('Quantity:', this.quantity);

    this.quantity = 1;
  }
}
