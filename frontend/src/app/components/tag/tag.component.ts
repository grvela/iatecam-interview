import { Component } from '@angular/core';
import { NgForm } from '@angular/forms'; // Import NgForm

@Component({
  selector: 'app-tag',
  templateUrl: './tag.component.html',
  styleUrls: ['./tag.component.css'],
})
export class TagComponent {
  tagName: string = '';

  createTag(tagForm: NgForm) {
    if (tagForm.valid) {
      console.log('Tag Name:', this.tagName);
      this.tagName = '';
    }
  }
}
