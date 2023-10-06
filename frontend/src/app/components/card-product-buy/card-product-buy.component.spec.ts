import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardProductBuyComponent } from './card-product-buy.component';

describe('CardProductBuyComponent', () => {
  let component: CardProductBuyComponent;
  let fixture: ComponentFixture<CardProductBuyComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CardProductBuyComponent]
    });
    fixture = TestBed.createComponent(CardProductBuyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
