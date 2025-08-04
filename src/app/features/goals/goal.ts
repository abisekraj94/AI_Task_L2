import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class GoalService {
  private apiUrl = 'http://localhost:8000/goals';

  constructor(private http: HttpClient) {}

  getGoals(token: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  getGoal(id: number, token: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  createGoal(goal: any, token: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, goal, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  updateGoal(id: number, goal: any, token: string): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, goal, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  deleteGoal(id: number, token: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }
} 