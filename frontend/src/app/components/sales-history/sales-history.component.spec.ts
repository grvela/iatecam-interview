import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SalesHistoryComponent } from './sales-history.component';

describe('SalesHistoryComponent', () => {
  let component: SalesHistoryComponent;
  let fixture: ComponentFixture<SalesHistoryComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SalesHistoryComponent]
    });
    fixture = TestBed.createComponent(SalesHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
