import { bootstrapApplication } from '@angular/platform-browser';
import { Component } from '@angular/core';

@Component({
  selector:'app-root',
  standalone:true,
//   // template:`<h1>Hello, World!</h1>`
//   template: `<h1>Hello, {{name}}!</h1>`
  template: `
  <h3>{{ title }}</h3>
  <p>Hello {{ name}}!</p>
  <p>2 + 3 = {{ 2 + 3}}</p>
  <p>Upper: {{ name.toUpperCase() }}</p>
  `

})
// class App {name = 'Angular 20';}

export class App {
  title = 'Template & Interpolation';
  name = 'Angular';
}


bootstrapApplication(App);



