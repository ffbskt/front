import {Component, OnInit, Input} from '@angular/core';

import {GroupsService} from './groups.service';

@Component({
  selector: 'app-groups',
  templateUrl: './groups.component.html',
  styleUrls: ['./groups.component.scss'],
})
export class GroupsComponent implements OnInit, Input {
  groups: any;
  @Input() group_name;

  constructor(private groupsService: GroupsService) {
    this.groups = [];
  }

  ngOnInit() {
    this.groupsService.getGroups()
      .subscribe(
        data => {
          this.groups = data.groups.filter(item => item.groups_name !== 'General parametrs');
          console.log(this.groups);
        }
      );
  }
}
