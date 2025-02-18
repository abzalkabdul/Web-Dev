import { Component, OnInit} from '@angular/core';
import { CommonModule } from '@angular/common';

interface Product {
  image: string;
  name: string;
  description: string;
  rating: number;
  link: string;
}



@Component({
  selector: 'app-products',
  imports: [CommonModule],
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})


export class ProductsComponent implements OnInit {
  products: Product[] = [
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/p55/p9b/5542335.png?format=gallery-medium',
      name: 'Смарт-часы Apple Watch SE"',
      description: 'Смарт-часы Apple Watch SE GPS Gen.2 2024 S/M 40 мм бежевый',
      rating: 4.9,
      link: "https://kaspi.kz/shop/p/apple-watch-se-gps-gen-2-2024-s-m-40-mm-bezhevyi-129172890/?c=750000000"
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/hec/h25/87197780049950.jpg?format=gallery-large',
      name: 'Смарт-часы Xiaomi Redmi Watch 5"',
      description: 'Смарт-часы Xiaomi Redmi Watch 5 Active 51 мм черный-черный',
      rating: 4.1,
      link: 'https://kaspi.kz/shop/p/xiaomi-redmi-watch-5-active-51-mm-chernyi-chernyi-123879372/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h1b/h3a/85300885454878.jpg?format=gallery-large',
      name: 'Смарт-часы Y-13"',
      description: 'Смарт-часы Y-13 SW 43 мм золотистый-золотистый',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/y-13-sw-43-mm-zolotistyi-zolotistyi-112273482/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h60/ha1/86079581487134.jpg?format=gallery-large',
      name: 'Смарт-часы Huawei Watch"',
      description: 'Смарт-часы Huawei Watch Fit 3 черный',
      rating: 3.9,
      link: 'https://kaspi.kz/shop/p/huawei-watch-fit-3-chernyi-119668941/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h76/h31/82569351266334.jpg?format=gallery-large',
      name: 'Смарт-часы Y-13"',
      description: 'Смарт-часы Y-13 SW 40 мм черный-черный',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/y-13-sw-40-mm-chernyi-chernyi-112224006/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h03/he3/86610193350686.jpg?format=gallery-large',
      name: 'Смарт-часы Samsung Galaxy Watch7',
      description: 'Смарт-часы Samsung Galaxy Watch7 44 мм графитовый-зеленый',
      rating: 4.4,
      link: 'https://resources.cdn-kaspi.kz/img/m/p/h66/h2b/85356927713310.jpg?format=gallery-large'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h73/h10/86078683611166.jpg?format=gallery-large',
      name: 'Смарт-часы Huawei Watch Fit 3"',
      description: 'Смарт-часы Huawei Watch Fit 3 золотистый-белый',
      rating: 4.2,
      link: 'https://kaspi.kz/shop/p/huawei-watch-fit-3-zolotistyi-belyi-119668978/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h33/h3d/83168262389790.jpg?format=gallery-large',
      name: 'Смарт-часы YUNTEKO ZWi39"',
      description: 'Смарт-часы YUNTEKO ZWi39 бежевый-бежевый',
      rating: 4.5,
      link: 'https://kaspi.kz/shop/p/yunteko-zwi39-bezhevyi-bezhevyi-112859205/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h1b/h93/64529738399774.jpg?format=gallery-large',
      name: 'Смарт-часы Apple Watch SE 2"',
      description: 'Смарт-часы Apple Watch SE 2 Gen (2022) 44 мм starlight-бежевый',
      rating: 5.0,
      link: 'https://kaspi.kz/shop/p/apple-watch-se-2-gen-2022-44-mm-starlight-bezhevyi-106362773/?c=750000000'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/he0/h86/85135995076638.png?format=gallery-medium',
      name: 'Смарт-часы Nepro100device"',
      description: 'Смарт-часы Nepro100device NPD Maks Kids Watch черный',
      rating: 4.0,
      link: 'https://kaspi.kz/shop/p/nepro100device-npd-maks-kids-watch-chernyi-116533653/?c=750000000'
    }
  ];

  constructor() { }

  ngOnInit(): void { }

  // share whatsapp
  shareOnWhatsApp(product: Product): void {
    const url = `https://wa.me/?text=${encodeURIComponent(product.link)}`;
    window.open(url, '_blank');
  }

  // share on tg
  shareOnTelegram(product: Product): void {
    const url = `https://t.me/share/url?url=${encodeURIComponent(product.link)}&text=${encodeURIComponent(product.name)}`;
    window.open(url, '_blank');
  }

}
