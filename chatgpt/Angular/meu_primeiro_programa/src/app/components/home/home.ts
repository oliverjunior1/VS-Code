import { Component } from '@angular/core';

@Component({
  imports: [],
  selector: 'app-home',
  styleUrl: './home.css',
  templateUrl: './home.html',
})
export class Home {
  nome: string = "Carlos";
  idade: number = 35;
  cidade: string = "Anápolis";
}
