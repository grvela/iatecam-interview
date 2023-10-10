import { TestBed } from '@angular/core/testing';

import { OutputService } from './output.service';

describe('OutputService', () => {
  let service: OutputService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OutputService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
