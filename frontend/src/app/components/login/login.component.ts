import { Component } from '@angular/core';
import { AuthService } from '../../services/auth/auth.service';
import { Router } from '@angular/router';

import { MessageService } from 'primeng/api';
import { NgForm } from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router, private messageService: MessageService) { }

  login(loginForm: NgForm) {
    if (loginForm.valid) {
      this.authService.login(this.username, this.password).subscribe({
        next: (response) => {
          console.log("Login bem sucedido", response);

          sessionStorage.setItem("access_token", response.access_token)

          this.router.navigate(["/home"])
        },
        error: (error) => {
          console.log("Erro no login", error);
          this.messageService.add({ severity: 'error', summary: 'Error', detail: 'User or credentials are invalid' });
        }
      });

    }
  }
}
