import { Component } from '@angular/core';

@Component({
  selector: 'app-sales-history',
  templateUrl: './sales-history.component.html',
  styleUrls: ['./sales-history.component.css']
})
export class SalesHistoryComponent {
  sales = [
    {
      date: '2023-01-15',
      hour: '09:30 AM',
      description: 'Product A',
      client: 'Client 1',
      seller: 'Seller A',
      notes: 'Sale notes for Product A',
    },
    {
      date: '2023-01-14',
      hour: '02:15 PM',
      description: 'Product B',
      client: 'Client 2',
      seller: 'Seller B',
      notes: 'Sale notes for Product B',
    },
    {
      date: '2023-01-13',
      hour: '11:45 AM',
      description: 'Product C',
      client: 'Client 3',
      seller: 'Seller C',
      notes: 'Sale notes for Product C',
    },
    {
      date: '2023-01-12',
      hour: '05:20 PM',
      description: 'Product D',
      client: 'Client 4',
      seller: 'Seller D',
      notes: 'Sale notes for Product D',
    },
  ];
}
