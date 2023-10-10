import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { CreateStorage, Storage } from '../../interfaces/storage.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StorageService {
  private apiUrl = "http://localhost:80/storages"

  constructor(private http: HttpClient) { }

  get_user_storages(): Observable<Storage[]> {
    return this.http.get<Storage[]>(`${this.apiUrl}/by/me`);
  }

  get_products_to_buy(): Observable<Storage[]> {
    return this.http.get<Storage[]>(`${this.apiUrl}/to/me`);
  }

  create_storage(storage: CreateStorage): Observable<Storage> {
    return this.http.post<Storage>(this.apiUrl, storage);
  }
}
