import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class EmployeeService {
  private apiUrl = 'http://localhost:8000/employees';

  constructor(private http: HttpClient) {}

  getEmployees(token: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  getEmployee(id: number, token: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  createEmployee(employee: any, token: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/`, employee, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  updateEmployee(id: number, employee: any, token: string): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, employee, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }

  deleteEmployee(id: number, token: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`, {
      headers: new HttpHeaders({ 'Authorization': `Bearer ${token}` })
    });
  }
} 