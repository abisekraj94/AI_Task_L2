import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class SkillService {
  private apiUrl = 'http://localhost:8000/skills';

  constructor(private http: HttpClient) {}

  getSkills(token: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  getSkill(id: number, token: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  createSkill(skill: any, token: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, skill, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  updateSkill(id: number, skill: any, token: string): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, skill, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  deleteSkill(id: number, token: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }
} 