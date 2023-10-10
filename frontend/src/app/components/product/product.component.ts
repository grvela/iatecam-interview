import { Component, Input } from '@angular/core';
import { StorageService } from '../../services/storage/storage.service';
import { MessageService } from 'primeng/api';
import { CreateStorage, Storage } from '../../interfaces/storage.interface';
import { Tag } from '../../interfaces/tag.interface';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css'],
})
export class ProductComponent {
  @Input() tags: Tag[] = [];
  product: CreateStorage = {} as CreateStorage;

  constructor(private storageService: StorageService, private messageService: MessageService) { }

  createProduct(productForm: NgForm) {
    if (productForm.valid) {
      this.storageService.create_storage(this.product).subscribe({
        next: () => {
          this.messageService.add({ severity: 'success', summary: 'Created', detail: 'Product created successfully' })
        },
        error: () => {
          this.messageService.add({ severity: 'error', summary: 'Error', detail: 'Cant create product' });
        }
      })
    }
  }
}
