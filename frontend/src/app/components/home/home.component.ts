import { Component } from '@angular/core';
import { TagService } from '../../services/tag/tag.service';
import { StorageService } from '../../services/storage/storage.service';
import { SaleService } from '../../services/sale/sale.service';
import { SseService } from '../../services/sse/sse.service';

import { Storage } from '../../interfaces/storage.interface';
import { Tag } from '../../interfaces/tag.interface';
import { Sale } from '../../interfaces/sale.interface';
import { Chart } from '../../interfaces/chart.interface';

import { ChartService } from '../../services/chart/chart.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  user_storages: Storage[] = [];
  to_buy: Storage[] = [];
  tags: Tag[] = [];
  last_sales: Sale[] = [];
  sales_by_tag: Chart[] = [];


  data: any;
  options: any;

  doughnut_labels: string[] = [];
  doughnut_amounts: number[] = []

  chart_labels: string[] = [];
  chart_amounts: number[] = []

  constructor(private tagService: TagService,
    private storageService: StorageService,
    private saleService: SaleService,
    private chartService: ChartService,
    private sseService: SseService
  ) { }

  ngOnInit() {

    this.sseService.getEvents('tag_created').subscribe((eventData) => {
      // Lide com os eventos SSE recebidos aqui
      console.log('Novo evento SSE recebido:', eventData);
      // Execute ação correspondente com os dados do evento
    });

    this.tagService.get_tags().subscribe({
      next: (response: Tag[]) => {
        this.tags = response;
      }
    });

    this.storageService.get_user_storages().subscribe({
      next: (response: Storage[]) => {
        this.user_storages = response;
      }
    });

    this.storageService.get_products_to_buy().subscribe({
      next: (response: Storage[]) => {
        this.to_buy = response;
      }
    });

    this.saleService.get_last_sales().subscribe({
      next: (response: Sale[]) => {
        this.last_sales = response;
      }
    });

    this.chartService.get_sales_by_tag().subscribe({
      next: (response: Chart[]) => {
        const data = response;

        const sortedData = data.sort((a, b) => b.amount - a.amount);

        const pairs = sortedData.map(item => [item.tag!.name, item.amount]);

        if (pairs.length > 3) {
          const extraElements = pairs.splice(3);
          const totalAmount = extraElements.reduce((total, item) => total + Number(item[1]), 0);
          pairs.push(["Outros", totalAmount]);
        }

        this.doughnut_labels = pairs.map(pair => String(pair[0]));
        this.doughnut_amounts = pairs.map(pair => Number(pair[1]));
      }
    });

    this.chartService.get_sales_by_product().subscribe({
      next: (response: Chart[]) => {
        const array = response;

        const nomesProdutos = [];
        const quantidades = [];

        for (const item of array) {
          nomesProdutos.push(item.product!.name);
          quantidades.push(item.amount);
        }

        this.chart_labels = nomesProdutos;
        this.chart_amounts = quantidades;
      }
    });


  }

} 
