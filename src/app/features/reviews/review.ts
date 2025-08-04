import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ReviewService {
  private apiUrl = 'http://localhost:8000/reviews';

  constructor(private http: HttpClient) {}

  getReviews(token: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  getReview(id: number, token: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  createReview(review: any, token: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, review, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  updateReview(id: number, review: any, token: string): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, review, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  deleteReview(id: number, token: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }
} 