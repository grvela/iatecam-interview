import { NgModule } from '@angular/core';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';

import { AppRoutingModule } from '../app-routing.module';

import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';
import { FormsModule } from '@angular/forms';
import { DropdownModule } from 'primeng/dropdown';
import { TagComponent } from './tag/tag.component';


@NgModule({
    declarations: [
        LoginComponent,
        SignupComponent,
        HomeComponent,
        TagComponent
    ],
    imports: [
        AppRoutingModule,
        InputTextModule,
        ButtonModule,
        FormsModule,
        DropdownModule
    ],
    exports: [
        LoginComponent,
        SignupComponent,
        HomeComponent,
        TagComponent
    ],
})
export class AppComponentsModule { }
