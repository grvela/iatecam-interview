import { Component } from '@angular/core';
import { TagService } from '../../services/tag/tag.service';
import { StorageService } from '../../services/storage/storage.service';
import { Storage } from '../../interfaces/storage.interface';
import { Tag } from '../../interfaces/tag.interface';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  user_storages: Storage[] = []
  to_buy: Storage[] = []
  tags: Tag[] = [];

  constructor(private tagService: TagService, private storageService: StorageService) { }

  ngOnInit() {
    this.tagService.get_tags().subscribe({
      next: (response: Tag[]) => {
        this.tags = response;
      }
    });

    this.storageService.get_user_storages().subscribe({
      next: (response: Storage[]) => {
        this.user_storages = response;
      }
    });

    this.storageService.get_products_to_buy().subscribe({
      next: (response: Storage[]) => {
        this.to_buy = response
      }
    })
  }

} 
