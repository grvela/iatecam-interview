import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { TagComponent } from './tag/tag.component';
import { ProductComponent } from './product/product.component';
import { CardProductComponent } from './card-product/card-product.component';
import { CardProductBuyComponent } from './card-product-buy/card-product-buy.component';
import { SalesHistoryComponent } from './sales-history/sales-history.component';

import { AppRoutingModule } from '../app-routing.module';

import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { InputNumberModule } from 'primeng/inputnumber';
import { ButtonModule } from 'primeng/button';
import { FormsModule } from '@angular/forms';
import { DropdownModule } from 'primeng/dropdown';
import { CardModule } from 'primeng/card';


@NgModule({
    declarations: [
        LoginComponent,
        SignupComponent,
        HomeComponent,
        TagComponent,
        ProductComponent,
        CardProductComponent,
        CardProductBuyComponent,
        SalesHistoryComponent
    ],
    imports: [
        CommonModule,
        AppRoutingModule,
        InputTextModule,
        InputTextareaModule,
        InputNumberModule,
        ButtonModule,
        FormsModule,
        DropdownModule,
        CardModule
    ],
    exports: [
        LoginComponent,
        SignupComponent,
        HomeComponent,
        TagComponent,
        ProductComponent,
        CardProductComponent,
        CardProductBuyComponent
    ],
})
export class AppComponentsModule { }