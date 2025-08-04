import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: 'reports', loadChildren: () => import('./features/reports/reports-module').then(m => m.ReportsModule), canActivate: [AuthGuard] },
];
