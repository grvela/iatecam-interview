import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SalesByTagComponent } from './sales-by-tag.component';

describe('SalesByTagComponent', () => {
  let component: SalesByTagComponent;
  let fixture: ComponentFixture<SalesByTagComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SalesByTagComponent]
    });
    fixture = TestBed.createComponent(SalesByTagComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
