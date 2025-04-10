import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {Vacancy} from '../core/models/vacancy';
import {ApiService} from '../core/services/api.service';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-company-vacancies',
  templateUrl: './company-vacancies.component.html',
  imports: [
    NgForOf
  ],
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {
  vacancies: Vacancy[] = [];
  companyId!: number;

  constructor(private route: ActivatedRoute, private apiService: ApiService) {}

  ngOnInit(): void {
    this.companyId = Number(this.route.snapshot.paramMap.get('id'));
    this.apiService.getCompanyVacancies(this.companyId).subscribe(data => {
      this.vacancies = data;
    });
  }
}
