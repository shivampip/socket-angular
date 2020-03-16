import { TestBed } from '@angular/core/testing';

import { HiSocketService } from './hi-socket.service';

describe('HiSocketService', () => {
  let service: HiSocketService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HiSocketService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
