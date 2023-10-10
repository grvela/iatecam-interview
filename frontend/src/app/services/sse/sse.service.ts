import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})
export class SseService {
    private eventSource: EventSource;

    constructor() {
        this.eventSource = new EventSource('http://localhost/api/sse');
    }

    getEvents(eventType: string): Observable<MessageEvent> {
        return new Observable((observer) => {
            this.eventSource.addEventListener(eventType, (event: MessageEvent) => {
                observer.next(event.data);
            });
        });
    }
}
