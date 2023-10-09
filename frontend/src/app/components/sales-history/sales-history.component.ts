import { Component } from '@angular/core';
import { Input } from '@angular/core';

import { Sale } from '../../interfaces/sale.interface';

@Component({
  selector: 'app-sales-history',
  templateUrl: './sales-history.component.html',
  styleUrls: ['./sales-history.component.css']
})
export class SalesHistoryComponent {
  @Input() sale: Sale = {} as Sale;
}
