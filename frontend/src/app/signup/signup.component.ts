import { Component } from '@angular/core';

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

  accountTypeOptions: any[] = [
    { label: 'Select Account Type', value: null },
    { label: 'Supplier', value: 'supplier' },
    { label: 'Client', value: 'client' },
  ];

  signup() {
    // Add your signup logic here
    console.log('Name:', this.name);
    console.log('Username:', this.username);
    console.log('Password:', this.password);
    console.log('Account Type:', this.accountType);
  }
}
