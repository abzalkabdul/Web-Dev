import { Routes } from '@angular/router';
import {CompanyVacanciesComponent} from './company-vacancies/company-vacancies.component';
import {CompanyListComponent} from './company-list/company-list.component';

export const routes: Routes = [
  {path: 'companies', component: CompanyListComponent},
  {path: 'companies/:id/vacancies', component: CompanyVacanciesComponent}
];
