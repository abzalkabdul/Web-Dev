import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {ApiService} from '../core/services/api.service';
import {Company} from '../core/models/company';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  imports: [
    NgForOf
  ],
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];

  constructor(private apiService: ApiService, private router: Router) {
  }

  ngOnInit(): void {
    this.apiService.getCompanies().subscribe(data => {
      this.companies = data;
    });
  }

  goToVacancies(companyId: number): void {
    this.router.navigate([`/companies/${companyId}/vacancies`]);
  }
}
