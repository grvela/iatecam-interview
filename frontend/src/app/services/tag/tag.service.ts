import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Tag, CreateTag } from '../../interfaces/tag.interface';

@Injectable({
  providedIn: 'root'
})
export class TagService {
  private apiUrl = "http://localhost:80/tags"

  constructor(private http: HttpClient) { }

  get_tags(): Observable<Tag[]> {
    return this.http.get<Tag[]>(this.apiUrl)
  }

  create_tag(tag: CreateTag): Observable<Tag> {
    return this.http.post<Tag>(this.apiUrl, tag);
  }
}
