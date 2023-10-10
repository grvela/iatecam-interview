import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { TagService } from '../../services/tag/tag.service';
import { CreateTag } from '../../interfaces/tag.interface';
import { MessageService } from 'primeng/api';


@Component({
  selector: 'app-tag',
  templateUrl: './tag.component.html',
  styleUrls: ['./tag.component.css'],
})
export class TagComponent {
  tagName: string = '';

  constructor(private tagService: TagService, private messageService: MessageService) { }

  createTag(tagForm: NgForm) {
    if (tagForm.valid) {
      const data: CreateTag = {
        name: this.tagName
      }
      this.tagService.create_tag(data).subscribe({
        next: () => {
          this.messageService.add({ severity: 'success', summary: 'Created', detail: 'Tag created successfully' })
        },
        error: () => {
          this.messageService.add({ severity: 'error', summary: 'Error', detail: 'Cant create tag' });
        }
      });
    }
  }
}
