import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ReportService {
  private apiUrl = 'http://localhost:8000/reports';

  constructor(private http: HttpClient) {}

  getPerformanceTrends(token: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/performance-trends`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  getGoalAchievementRates(token: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/goal-achievement-rates`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }
} 