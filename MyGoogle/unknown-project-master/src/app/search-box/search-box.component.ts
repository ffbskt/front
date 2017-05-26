import {Component} from '@angular/core';

@Component({
  selector: 'app-search-box',
  template: `
    <div>
      <input type="search" [(ngModel)]="group_name" name="group_name">
    </div>
  `,
  styles: [`
    input {
      background: rgba(238, 238, 238, 1);
      color: rgba(33, 33, 33, 1);
      border: none;
      line-height: 40px;
      padding: 0 10px;
      width: 300px;
    }
  `]
})
export class SearchBoxComponent {
  group_name: string;
}
