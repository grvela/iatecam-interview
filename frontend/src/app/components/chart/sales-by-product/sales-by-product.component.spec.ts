import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SalesByProductComponent } from './sales-by-product.component';

describe('SalesByProductComponent', () => {
  let component: SalesByProductComponent;
  let fixture: ComponentFixture<SalesByProductComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SalesByProductComponent]
    });
    fixture = TestBed.createComponent(SalesByProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
