import { Component, Input } from '@angular/core';
import { Storage } from '../../interfaces/storage.interface';
import { OutputService } from '../../services/output/output.service';
import { CreateOutput } from '../../interfaces/output.interface';

@Component({
  selector: 'app-card-product-buy',
  templateUrl: './card-product-buy.component.html',
  styleUrls: ['./card-product-buy.component.css']
})
export class CardProductBuyComponent {
  @Input() product: Storage = {} as Storage;
  quantity: number = 0;

  constructor(private outputService: OutputService) { }

  buyProduct() {
    const data: CreateOutput = {
      user_id: this.product.user.id,
      storage_id: this.product.id,
      amount: this.quantity
    }
    console.log(this.product.id);
    this.outputService.create_output(data).subscribe({
      next: () => {
        console.log("Deu tudo certo");
      }
    });
    this.quantity = 1;
  }
}
