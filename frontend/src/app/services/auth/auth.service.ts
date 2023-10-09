import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:80/auth';

  constructor(private http: HttpClient) { }

  getAuthToken() {
    return sessionStorage.getItem("access_token");
  }

  register(name: string, username: string, password: string) {
    const data = {
      name,
      username,
      password
    }
    return this.http.post(`${this.apiUrl}/register`, data)
  }

  login(username: string, password: string): Observable<any> {
    const formData = new FormData();

    formData.append('username', username);
    formData.append('password', password);

    return this.http.post(`${this.apiUrl}/login`, formData);
  }

  logout(): void {
    sessionStorage.removeItem('access_token');
  }

  isAuthenticated(): boolean {
    return !!sessionStorage.getItem('access_token');
  }

  getAccessToken(): string | null {
    return sessionStorage.getItem('access_token');
  }
}
