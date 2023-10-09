import { Component, Input } from '@angular/core';
import { Storage } from '../../interfaces/storage.interface';

@Component({
  selector: 'app-card-product',
  templateUrl: './card-product.component.html',
  styleUrls: ['./card-product.component.css']
})
export class CardProductComponent {
  @Input() product: any;


}
