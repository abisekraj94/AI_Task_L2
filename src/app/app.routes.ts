import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: 'employees', pathMatch: 'full' },
  { path: 'auth', loadChildren: () => import('./features/auth/auth-module').then(m => m.AuthModule) },
  { path: 'employees', loadChildren: () => import('./features/employees/employees-module').then(m => m.EmployeesModule) },
  { path: 'goals', loadChildren: () => import('./features/goals/goals-module').then(m => m.GoalsModule) },
  { path: 'reviews', loadChildren: () => import('./features/reviews/reviews-module').then(m => m.ReviewsModule) },
  { path: 'skills', loadChildren: () => import('./features/skills/skills-module').then(m => m.SkillsModule) },
  { path: 'reports', loadChildren: () => import('./features/reports/reports-module').then(m => m.ReportsModule) },
  { path: '**', redirectTo: 'employees' }
]; 