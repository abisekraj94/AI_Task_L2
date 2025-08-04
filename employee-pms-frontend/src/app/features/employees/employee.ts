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

  // ... other CRUD methods ...
}
