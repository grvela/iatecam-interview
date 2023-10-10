import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Sale } from '../../interfaces/sale.interface';

@Injectable({
  providedIn: 'root'
})
export class SaleService {

  private apiUrl = "http://localhost:80/outputs"

  constructor(private http: HttpClient) { }

  get_last_sales(): Observable<Sale[]> {
    return this.http.get<Sale[]>(`${this.apiUrl}/latest-sales`);
  }

}
