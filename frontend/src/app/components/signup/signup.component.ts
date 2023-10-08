import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
})
export class SignupComponent {
  name: string = '';
  username: string = '';
  password: string = '';
  accountType: string = '';

  constructor(private authService: AuthService) { }

  signup() {
    console.log('Name:', this.name);
    console.log('Username:', this.username);
    console.log('Password:', this.password);
    this.authService.register(this.name, this.username, this.password).subscribe(
      {
        next: (response) => {
          console.log("User created succesfully", response);
        },
        error: (error) => {
          console.log("Error to create user", error);
        }
      }
    )

  }
}
