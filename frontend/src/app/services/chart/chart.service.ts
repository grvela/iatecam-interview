import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

import { Chart } from '../../interfaces/chart.interface';

@Injectable({
  providedIn: 'root'
})
export class ChartService {
  private apiUrl = "http://localhost:80/analytics"

  constructor(private http: HttpClient) { }

  get_sales_by_tag(): Observable<Chart[]> {
    return this.http.get<Chart[]>(`${this.apiUrl}/sales/by/tag`);
  }

  get_sales_by_product(): Observable<Chart[]> {
    return this.http.get<Chart[]>(`${this.apiUrl}/sales/by/product`);
  }
}
