import { Component } from '@angular/core';
import { AuthService } from '../../services/auth/auth.service';
import { Router } from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  login() {
    this.authService.login(this.username, this.password).subscribe({
      next: (response) => {
        console.log("Login bem sucedido", response);
        this.router.navigate(["/home"])
      },
      error: (error) => {
        console.log("Erro no login", error);
      }
    });

  }
}
