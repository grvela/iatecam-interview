import { Component } from '@angular/core';
import { Input } from '@angular/core';

@Component({
  selector: 'app-sales-by-tag',
  templateUrl: './sales-by-tag.component.html',
  styleUrls: ['./sales-by-tag.component.css']
})
export class SalesByTagComponent {
  @Input() labels: string[] = [];
  @Input() values: number[] = [];

  data: any;
  options: any;

  ngOnChanges() {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');

    this.data = {
      labels: this.labels,
      datasets: [
        {
          data: this.values,
          backgroundColor: [documentStyle.getPropertyValue('--blue-500'), documentStyle.getPropertyValue('--yellow-500'), documentStyle.getPropertyValue('--green-500')],
          hoverBackgroundColor: [documentStyle.getPropertyValue('--blue-400'), documentStyle.getPropertyValue('--yellow-400'), documentStyle.getPropertyValue('--green-400')]
        }
      ]
    };


    this.options = {
      cutout: '60%',
      plugins: {
        legend: {
          labels: {
            color: textColor
          }
        }
      }
    };

  }
}
