import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CreateOutput, Output } from '../../interfaces/output.interface'

@Injectable({
  providedIn: 'root'
})
export class OutputService {
  private apiUrl = "http://localhost:80/outputs";

  constructor(private http: HttpClient) { }

  create_output(output: CreateOutput): Observable<CreateOutput> {
    return this.http.post<CreateOutput>(this.apiUrl, output);
  }

}
